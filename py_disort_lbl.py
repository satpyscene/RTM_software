import os
# 获取脚本所在目录的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))
# 改变当前工作目录到脚本所在目录
os.chdir(script_dir)
# 现在尝试加载文件，应该能够找到位于同一目录下的文件了
import re
import numpy as np
import math as math
import matplotlib.pyplot as plt
# import disort
import matplotlib
matplotlib.use('TkAgg') # 使用TkAgg后端

#print(disort.__doc__)

#https://github.com/SeregaOsipov/pyDISORT/blob/master/disotest.py

class RadBC:
    def __init_(self,fbeam,fisot,umu0,phi0,ibcnd,temis,ttemp,albedo):
        self.FBEAM = fbeam
        self.FISOT = fisot
        self.UMU0=umu0
        self.PHI0=phi0
        self.IBCND=ibcnd
        self.TEMIS = temis
        self.TTEMP = ttemp  
        self.ALBEDO = albedo

class PyDOM:
    
    c1 = 1.1910659e-8
    c2 = 1.438786

    def __init__(self,wav_min,resolution,n_wvn,nlyr,nmom,ntau,direction,reflection,surfaceTEMP,numu,nphi,flags,prnt,header,trans_file,profile):
        self.WAV_MIN=wav_min
        self.N_WVN=n_wvn
        self.N_WVN_CL=n_wvn
        self.N_DE=1
        self.NLYR=nlyr  #最好是根据profile的层数确定！如果是标准大气层数，直接给定？如果是自定义，那就len方法获得？

        self.NMOM=nmom  #disort 流数
        self.NSTR=nmom 
        self.N_LEVEL=nlyr+1
        self.NTAU=ntau  #光学厚度个数
        self.N_UTAU = 1 
        self.NUMU=numu  #观测方向方向个数
        self.NPHI=nphi

        self.temp_flt=np.zeros((n_wvn,nlyr))  
        self.got_layer=np.zeros((nlyr,n_wvn))
        self.trans_layer=np.zeros((nlyr,n_wvn))

        self.USRTAU=flags['usrtau']
        self.USRANG=flags['usrang']
        self.LAMBER=flags['lamber'] #朗伯体假设
        self.PLANK =flags['plank']
        self.ONLYFL=flags['onlyfl']


        self.DTAUC=np.zeros(nlyr)
        self.SSLAB=np.zeros(nlyr)
        self.PMOM=np.zeros((nmom+1,nlyr))
        self.TEMPER=np.zeros(nlyr+1)
        self.UTAU=np.zeros(ntau)
        self.UMU=np.zeros(numu)
        self.PHI=np.zeros(nphi)
        self.H_LYR=np.zeros(nlyr+1)


        self.RFLDIR=np.zeros(ntau)
        self.RFLDN=np.zeros(ntau)
        self.FLUP=np.zeros(ntau)
        self.DFDT=np.zeros(ntau)
        self.UAVG=np.zeros(ntau)
        self.ALBMED = np.zeros(numu)
        self.TRNMED = np.zeros(numu)
        self.UU = np.zeros((numu, ntau, nphi)) #输出的辐射强度

        self.bt=np.zeros((numu,ntau,n_wvn))  #辐射亮温
        self.wvn=np.zeros(n_wvn)  #波数

        self.PRNT = np.array(prnt)

        #read optical properties from files
        self.trans_file=trans_file
        self.profile=profile

     #   self.temp_flt=np.loadtxt(self.trans_file)
     #   self.got_layer=self.temp_flt.T  #列是波数
     #   self.got_layer=-np.log(self.got_layer)
        self.got_layer=np.loadtxt(self.trans_file).T

        self.TEMPER=np.loadtxt(self.profile)[:,1]  #temperature 
        self.TEMPER=np.flip(self.TEMPER)  #逆序，数组开始的对应地面？和LBL的结果对应？
        

        self.modtau = 2.00
        self.moddeff = 50.0
        self.cbase = 1500.00

        self.vza = direction #观测方向

        self.UMU[1-1] = math.cos(self.vza*math.pi/180) 
        self.PHI[1-1] = 0.0
        self.ALBEDO = reflection #反射率

        self.FBEAM = 0.0
        self.FISOT = 0.0
        self.UMU0=1.0
        self.PHI0=0.0

        #要不要为编辑条件、入射条件分别设置个类或字典文件，以减少函数参数个数？

        self.IBCND=0
        self.ACCUR = 1.0E-05
        self.BTEMP = surfaceTEMP#地表温度
        
        self.TEMIS = 0.0
        self.TTEMP = 0.0
        self.WVNMLO = 0.0
        self.WVNMHI = 0.0
        self.EARTH_RADIUS = 6371.0
        self.HEADER=header

        #PMOM=np.ones((NMOM+1, NLYR))
        #PMOM[:,0]=disort.getmom(1,0,NMOM)

        self.DTAUC[0:nlyr]=self.got_layer[0:nlyr,0] #注意：0:NLYR实际上是0~NYLR-1；可以把NYLR理解成个数

        self.dwvnm=resolution  #光谱分辨率


        #####用于进度回调的属性
        self.progress_callback = None  # 添加一个用于进度回调的属性

    def set_progress_callback(self, callback):
        self.progress_callback = callback
    def process_data_files(self, directory):
        """
        处理指定目录下的数据文件，计算每个数据除以均值后乘以3的结果。
        
        参数:
        directory (str): 数据文件所在的目录路径。
        """
        # 获取所有符合条件的文件
        files = [f for f in os.listdir(directory) if f.startswith('WVN') and f.endswith('.dat')]

        # 定义一个函数来从文件名中提取波长数值
        def extract_wavelength(filename):
            match = re.search(r'(\d+p\d+)', filename)
            if match:
                return float(match.group(1).replace('p', '.'))
            else:
                return 0

        # 根据波长对文件进行排序
        sorted_files = sorted(files, key=extract_wavelength)

        # 用于存储提取的数据
        extracted_data = []
        sinref_data = []
        # 遍历排序后的文件列表
        for filename in sorted_files:
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                first_line = file.readline()
                data_items = first_line.split()
                if len(data_items) >= 3:
                    four_data = float(data_items[3])
                    five_data = float(data_items[4])
                    extracted_data.append(four_data)
                    sinref_data.append(five_data)

        # 计算数据的均值
        if extracted_data:
            mean_value = sum(extracted_data) / len(extracted_data)

            # 将每个数据除以均值并乘以3
            adjusted_data = [(data / mean_value) * 3 for data in extracted_data]
            return adjusted_data,sinref_data
        else:
            return []

    def solve(self,cld_height,cld_width,cloud_switch):
        self.RFLDIRlist = []
        self.RFLDNlist = []
        self.FLUPlist = []
        self.DFDTlist = []
        self.UAVGlist = []
        self.ALBMEDlist = []
        self.TRNMEDlist = []
        directory = '/media/bubble/65b27829-3c2d-4862-9190-09e1c0c31194/bubble/GUI/RTSW_1.2.1.240428_alpha/OUTPUT/C8R050/BSD'  # 设置数据文件所在的目录
        CLD,omega = self.process_data_files(directory)
        for iwvn in range(1,self.N_WVN+1):
            WVNMLO =float(self.WAV_MIN)-self.dwvnm/2+self.dwvnm*(iwvn-1)
            WVNMHI =float(self.WAV_MIN)+self.dwvnm/2+self.dwvnm*(iwvn-1)
            wvnmct=(WVNMLO+WVNMHI)/2
            
            self.DTAUC[0:self.NLYR]=self.got_layer[0:self.NLYR,iwvn-1] #光学厚度
            if cloud_switch == 'on':
                for i in range(0,int(cld_width*12)) :
                    self.DTAUC[i+int((cld_height/1000)*100)]+=CLD[iwvn-1]

                    self.SSLAB[i+int((cld_height/1000)*100)]=omega[iwvn-1]

                for i in range(0,self.NLYR):
                    if self.DTAUC[i]<1e-6:
                        self.DTAUC[i]=0.0
            
            self.SSLAB[:]=0.0
            self.UTAU[1-1] = 0.0  #观测光学厚度
            
            self.RFLDIR, \
            self.RFLDN, \
            self.FLUP, \
            self.DFDT, \
            self.UAVG, \
            self.UU, \
            self.ALBMED, \
            self.TRNMED = disort.disort(self.NLYR,self.DTAUC,self.SSLAB,self.NMOM,self.PMOM,self.TEMPER,WVNMLO,WVNMHI,\
                                        self.USRTAU,self.NTAU,self.UTAU,self.NSTR,self.USRANG,self.NUMU,self.UMU,self.NPHI,\
                                        self.PHI,self.IBCND,self.FBEAM,self.UMU0,self.PHI0,self.FISOT,self.LAMBER,self.ALBEDO,\
                                        self.BTEMP,self.TTEMP,self.TEMIS,self.PLANK,self.ONLYFL,self.ACCUR,self.PRNT,self.HEADER)
            self.bt[0,0,iwvn-1]=self.c2*wvnmct/(math.log(1.0+self.c1/(self.UU[0,0,0]/self.dwvnm)*wvnmct**3))
            self.wvn[iwvn-1]=wvnmct
            progressValue=(iwvn/self.N_WVN)*100
            if self.progress_callback is not None:
                self.progress_callback(progressValue)  # 调用回调函数更新进度
            #print(UU[0,0,0])
            self.RFLDIRlist.append(self.RFLDIR)
            self.RFLDNlist.append(self.RFLDN)
            self.FLUPlist.append(self.FLUP)
            self.DFDTlist.append(self.DFDT)
            self.UAVGlist.append(self.UAVG)
            self.ALBMEDlist.append(self.ALBMED)
            self.TRNMEDlist.append(self.TRNMED)
            self.data = [self.RFLDIRlist, self.RFLDNlist, self.FLUPlist,self.DFDTlist, self.UAVGlist, self.ALBMEDlist,self.TRNMEDlist]
        return self.wvn,self.bt,self.data
        
    #wvn from 680 to 1130
    def plot(self):
        from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
        from PySide6.QtGui import QPixmap,Qt, QImage
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(self.wvn[:],self.bt[0,0,:])
        plt.xlabel('Wavenumber')
        plt.ylabel('Brightness temperature')
        plt.xlim([500,2000])
        plt.ylim([200,300])
        canvas = FigureCanvas(fig)
        canvas.draw()
        width, height = fig.get_size_inches() * fig.get_dpi()
        im = QImage(canvas.buffer_rgba(), int(width), int(height), QImage.Format_ARGB32)

        plt.show()
        return im

if __name__=='__main__':
    
    print_tag=[False, False, False, False, False]
   
    flags={'usrang':True,'usrtau':True,'lamber':True,'plank':True,'onlyfl':False}

    pydom1=PyDOM(500,0.5,3001,100,32,1,0.0,0.02,500,1,1,flags,print_tag,\
        'LBLRTM+DISORT','GAS_OD_PROFILE_0001','Profile_0001')
    
    #可以为PyDOM添加修改nlyr和相应数组的函数，这样可以在程序中重新计算？
    pydom1.solve()
    
    pydom1.plot()
