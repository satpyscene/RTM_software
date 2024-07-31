#主文件不需要这个
import os
# 获取脚本所在目录的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))
# 改变当前工作目录到脚本所在目录
os.chdir(script_dir)
# 现在尝试加载文件，应该能够找到位于同一目录下的文件了

import numpy as np
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QGraphicsScene, QGraphicsPixmapItem,QVBoxLayout, QWidget ,QGraphicsView
from PySide6.QtGui import QPixmap, QImage ,QPainter
from PySide6.QtCore import Qt, Signal ,QPoint,Slot,QTimer
from Ui_mainWindow_0428_alpha import Ui_MainWindow
import py_disort_lbl
import matplotlib
matplotlib.use('Agg') # 使用TkAgg后端
from datetime import datetime

from PySide6.QtWidgets import QFileDialog
# from qt_material import apply_stylesheet
import sys
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QLineEdit, QGraphicsView, QGraphicsScene
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor,QBrush
import csv


class Mywindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.setWindowTitle('辐射传输可视化软件')
                # 创建状态栏
        self.status_bar = self.statusBar()
        # 在状态栏上显示一条消息
        self.status_bar.showMessage('大气辐射传输软件测试版(1.2.1.240428_alpha)')
        # 假设你的主控件名为mainWidget，按钮名为pushButton
        self.mainWidget.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 200); /* 白色背景，50%透明度 */
            }
        """)


        self.drawtype = ['radiation','三角函数','悬链线']
        self.linetype = {'实线':'-','虚线':'--','点划线':'-.'}
        self.colortype = {'红色':'b','蓝色':'r','黑色':'k','绿色':'g'}
        self.comboBox_linetype.addItems(self.linetype.keys())
        self.comboBox_colortype.addItems(self.colortype.keys())



        self.graphicsView_3.setRenderHint(QPainter.Antialiasing)
        self.graphicsView_3.setRenderHint(QPainter.SmoothPixmapTransform)
        self.graphicsView_3.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphicsView_3.setResizeAnchor(QGraphicsView.AnchorViewCenter)





        
        # 探测器高度
        self.detector_slider.setMinimum(40)
        self.detector_slider.setMaximum(900)
        self.detector_slider.setValue(900)
        self.detector_slider.valueChanged.connect(self.update_scene_from_slider)
        self.detector_input.setText("900")
        self.detector_input.textChanged.connect(self.update_scene_from_input)
        # 目标物高度

        self.target_slider.setMinimum(40)
        self.target_slider.setMaximum(900)
        self.target_slider.setValue(80)
        self.target_slider.valueChanged.connect(self.update_scene_from_slider)
        self.target_input.setText("80")
        self.target_input.textChanged.connect(self.update_scene_from_input)

        # 天顶角

        self.angle_slider.setMinimum(0)
        self.angle_slider.setMaximum(90)
        self.angle_slider.setValue(20)
        
        self.angle_slider.valueChanged.connect(self.update_scene_from_slider)
        self.geo_lineEdit_angel.setText("21")
        self.geo_lineEdit_angel.textChanged.connect(self.update_scene_from_input)

        # 创建QGraphicsScene
        self.scene = QGraphicsScene(self)
        #self.scene.setSceneRect(self.graphicsView_3.viewport().rect())

        self.scene.setSceneRect(-500, -1000, 1000, 1000)
        self.graphicsView_3.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
        # 将场景设置给QGraphicsView
        self.graphicsView_3.setScene(self.scene)###3代表视角图像显示窗，2代表背景图像显示窗，不加数字表示输出图像显示窗
        # 显示初始图片
        #self.display_initial_image('./pic_resource/假视角图.png')  # 替换为您的初始图片路径
        self.update_scene()
        QTimer.singleShot(100, self.simulate_user_input)####延时输入用来刷新页面，可以暂时隐藏视角显示异常的bug
        # 更新视图






        # ## 计算时间太长，将进程杀死
        # self.pushButton_kill.clicked.connect(self.kill)
        
        self.surfaceTEMP = None ##在此将弹窗设置中的地表温度默认设置为none，在draw()中检测其值，若为none，说明用户没有设置，可以提示设置
        self.surfacereflection = None

        self.last_clicked_button = None ##用于跟踪上一个被点击的按钮（展示正在操作的参数项）
        self.bind()
    #####################作用为显示视角####################################################
    def simulate_user_input(self):
        # 模拟用户输入
        self.geo_lineEdit_angel.setText("20")
    def update_scene_from_slider(self):
        self.detector_input.setText(str(self.detector_slider.value()))
        self.target_input.setText(str(self.target_slider.value()))
        self.geo_lineEdit_angel.setText(str(self.angle_slider.value()))
        self.update_scene()

    def update_scene_from_input(self):
        try:
            self.detector_slider.setValue(int(self.detector_input.text()))
            self.target_slider.setValue(int(self.target_input.text()))
            self.angle_slider.setValue(int(self.geo_lineEdit_angel.text()))
            self.update_scene()
        except ValueError:
            pass  # 如果输入不是有效的整数，忽略更新

    def update_scene(self):
        
        detector_height = self.detector_slider.value()
        target_height = self.target_slider.value()
        angle = self.angle_slider.value()

        # 清除现有图形
        self.scene.clear()

        # 计算目标物的位置
        radian = math.radians(angle)
        x = (detector_height-target_height) * math.tan(radian)
        y = target_height-40
        # 绘制天空
        self.scene.addRect(-500, -900, 1000, 20, QPen(QColor(135, 206, 235)),QBrush(QColor(135, 206, 235)))
        # 绘制地面
        self.scene.addRect(-500, -40, 1000, 20, QPen(QColor(139, 69, 19)),QBrush(QColor(139, 69, 19)))


        # 绘制连接线
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(15)
        self.scene.addLine(10, -detector_height+20, x+10, -target_height+20, pen)
        # 绘制探测器和目标物
        self.scene.addEllipse(-10, -detector_height, 40, 40, QPen(QColor(255, 0, 0)),QBrush(QColor(255, 0, 0)))
        self.scene.addEllipse(x - 10, -target_height, 40, 40, QPen(QColor(0, 0, 255)),QBrush(QColor(0, 0, 255)))

        # 绘制法线
        self.scene.addLine(x, -40, x, -900, QPen(QColor(0, 0, 0), 1, Qt.DashLine))

        # 更新视图
        self.scene.setSceneRect(-500, -1000, 1000, 1000)
        self.graphicsView_3.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
    #####################作用为显示视角####################################################

    # def kill(self):
    #     import os
    #     import signal

    #     # 获取当前进程的 ID
    #     pid = os.getpid()
    #     # 终止进程
    #     os.kill(pid, signal.SIGKILL)

    @Slot()
    def showPage_picset(self):
        self.stackedWidget.setCurrentIndex(0)
    def showPage_putout(self):
        self.stackedWidget.setCurrentIndex(1)
    def showPage_atm(self):
        self.stackedWidget.setCurrentIndex(2)
    def showPage_cloud(self):
        self.stackedWidget.setCurrentIndex(3)
    def showPage_geo(self):
        self.stackedWidget.setCurrentIndex(4)
    def showPage_surface(self):
        self.stackedWidget.setCurrentIndex(5)
    def showPage_sp(self):
        self.stackedWidget.setCurrentIndex(6)




    def update_progress(self, value):
        self.progressBar.setValue(value)  # 假设您的进度条对象名为self.progressBar
    def bind(self):
        #self.comboBox_drawtype.currentTextChanged.connect(self.typeChanged)
        self.pushButton_creatnewcase.clicked.connect(self.create_case)
        self.pushButton_opencase.clicked.connect(self.open_case)
        self.pushButton_savecase.clicked.connect(self.save_case)
        self.pushButton_casesaveas.clicked.connect(self.save_as_case)


        self.pushButton_start.clicked.connect(lambda:(self.showPage_geo(), self.button_clicked(self.pushButton_start),self.draw()))
        self.pushButton_draw.clicked.connect(lambda:(self.button_clicked(self.pushButton_draw),self.drawplotluoluo()))
        self.pushButton_dataout.clicked.connect(lambda:(self.button_clicked(self.pushButton_dataout),self.putoutdata()))
                # 菜单栏中输入参数项跳转widget弹窗
        self.action_parameter.triggered.connect(self.showparameter_pop)
        self.pushButton_atm.clicked.connect(self.showatm_pop)
        self.pushButton_cloud.clicked.connect(self.showcloud_pop)
        self.pushButton_geo.clicked.connect(self.showgeo_pop)
        self.pushButton_surface.clicked.connect(self.showsurface_pop)
        self.pushButton_spectral.clicked.connect(self.showspectral_pop)
        # self.pushButton_atm.clicked.connect(self.showatm_pop)
                # 菜单栏中的图片另存为功能
        self.actionSaveImage.triggered.connect(self.save_image)
        self.pushButton_picout.clicked.connect(lambda:(self.button_clicked(self.pushButton_picout),self.save_image()))
                # 菜单栏中的退出功能
        self.actionexit.triggered.connect(self.close)

        self.atm.clicked.connect(lambda:(self.showPage_atm(), self.button_clicked(self.atm)))
        self.cloud.clicked.connect(lambda:(self.showPage_cloud(), self.button_clicked(self.cloud)))
        self.geo.clicked.connect(lambda:(self.showPage_geo(), self.button_clicked(self.geo)))
        self.surface.clicked.connect(lambda:(self.showPage_surface(), self.button_clicked(self.surface)))
        self.spectral.clicked.connect(lambda:(self.showPage_sp(), self.button_clicked(self.spectral)))
        self.picset.clicked.connect(lambda:(self.showPage_picset(), self.button_clicked(self.picset)))
        self.putout.clicked.connect(lambda:(self.showPage_putout(), self.button_clicked(self.putout)))
        self.lineview.clicked.connect(self.draw_T_P)









####此函数的作用为显示当前正在被操作的对象（参数项）通过将正在显示的操作项的按钮（工具栏）显示为绿色
    def button_clicked(self, button):
        # 如果有按钮之前被点击过，恢复其颜色
        if self.last_clicked_button:
            self.last_clicked_button.setStyleSheet('')

        # 设置当前被点击的按钮的颜色为绿色
        button.setStyleSheet('background-color: rgba(255, 0, 0, 127);')

        # 更新最后被点击的按钮
        self.last_clicked_button = button




    def accept_tempsurface(self,temp):
        self.surfaceTEMP = temp
        
    def accept_reflectionsurface(self,reflection):       
        self.surfacereflection = reflection

    def accept_modelatm(self,modeltype):
        self.modeltype = modeltype

    def accept_angelgeo(self,angelgeo):
        self.angelgeo = angelgeo
  
    def accept_wavminsp(self,wavminsp):
        self.wavminsp = wavminsp
    def accept_wavmaxsp(self,wavmaxsp):
        self.wavmaxsp = wavmaxsp
    def accept_resolutionsp(self,resolutionsp):
        self.resolutionsp = resolutionsp
    def accept_streamssp(self,streamssp):
        self.streamssp = streamssp



    def draw(self):
        ###此部分为设置弹窗的参数
        #####此部分为修改为切换页面参数类型后的参数读取######

        self.wavminsp = self.sp_lineEdit_wavmin.text()  # 读取lineEdit的值
        self.wavmaxsp = self.sp_lineEdit_wavmax.text()  # 读取lineEdit的值
        self.resolutionsp = self.sp_comboBox_resolution.currentText()  # 读取lineEdit的值
        self.streamssp = self.sp_comboBox_streams.currentText()  # 读取lineEdit的值
        self.modeltype = self.atm_comboBox_model.currentText()
        self.angelgeo = self.geo_lineEdit_angel.text()  # 读取lineEdit的值
        self.surfaceTEMP = self.surface_lineEdit_TEMP.text()  # 读取lineEdit的值
        self.surfacereflection = self.surface_lineEdit_reflection.text()  # 读取lineEdit的值
        self.cloudheight = self.cloud_lineEdit_height.text()
        self.cloudwidth = self.cloud_lineEdit_width.text()
        ##############################################若后续需要将弹窗添加，只需将此部分禁用，将右侧隐藏部分的工具栏替代当前工具栏即可实现弹窗功能
        wav_min = float(self.wavminsp)
        wav_max = float(self.wavmaxsp)
        resolution = float(self.resolutionsp)
        wav_total = int((wav_max-wav_min)/resolution+1)
        streams = int(self.streamssp)
        angle = float(self.angelgeo)

        cloudheight = float(self.cloudheight)
        cloudwidth = float(self.cloudwidth)
        if self.surfacereflection == None:
            self.append_output('地面参数设置项中的地面反射率未设置，请填入反射率值并点击完成！')
            raise ValueError('反射率值未设置')
        reflection = self.surfacereflection
        if self.surfaceTEMP == None:
            self.append_output('地面参数设置项中的地表温度未设置，请填入温度并点击完成！')
            raise ValueError('地表温度未设置')
        surfaceTEMP = self.surfaceTEMP
        modeltype = {'用户自定义':'GAS_OD_PROFILE_0001'}
        ###



        self.start_time = datetime.now()  # 记录开始时间

        self.progressBar.setValue(0)



        print_tag=[False, False, False, False, False]

        flags={'usrang':True,'usrtau':True,'lamber':True,'plank':True,'onlyfl':False}

        pydom1=py_disort_lbl.PyDOM(wav_min,resolution,wav_total,100,streams,1,angle,reflection,surfaceTEMP,1,1,flags,print_tag,\
            'LBLRTM+DISORT',modeltype[self.modeltype],'Profile_0001')
        # pydom1=py_disort_lbl.PyDOM(500,0.5,3001,100,32,1,0.0,0.02,500,1,1,flags,print_tag,\
        #                             'LBLRTM+DISORT','GAS_OD_PROFILE_0001','Profile_0001')
        


                # 设置进度回调函数
        pydom1.set_progress_callback(self.update_progress)
        #可以为PyDOM添加修改nlyr和相应数组的函数，这样可以在程序中重新计算？
        self.append_output('正在拼命计算，请等待……')
        if self.cloud_switch.isChecked():

            cloud_switch = 'on'
        else:
            cloud_switch = 'off'
        self.x,self.y,self.data=pydom1.solve(cloudheight,cloudwidth,cloud_switch)
        # csv_file = 'output.csv'
        # with open(csv_file, 'w', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerows(self.data)
        # self.append_output('保存数据成功！！')

        self.append_output('计算完成！！')
        self.end_time = datetime.now()
        duration = self.end_time - self.start_time
        seconds = duration.total_seconds()
        self.append_output(f'用时: {seconds:.2f}秒\n')  # 显示运行时长，保留两位小数


    def putoutdata(self):
        csv_file = self.putoutpath_lineEdit.text()
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)
        self.append_output('保存数据成功！！')


    def drawplotluoluo(self):
        self.line_type = self.comboBox_linetype.currentText()
        self.color_type = self.comboBox_colortype.currentText()
        self.x1=self.lineEdit_x1.text()
        self.x2=self.lineEdit_x2.text()
        self.y1=self.lineEdit_y1.text()
        self.y2=self.lineEdit_y2.text()
        self.dpi=self.lineEdit_dpi.text()
        # # im = self.plt_sin(value_a,value_b,self.linetype[line_type],self.colortype[color_type],x1,x2,y1,y2)
        im=self.plt(self.x[:],self.y[0,0,:],self.linetype[self.line_type],self.colortype[self.color_type],self.x1,self.x2,self.y1,self.y2,self.dpi)
        

        self.append_output('绘制成功！！！')


            # pydom1.solve()
            # im=pydom1.plot()
        
        
        window.display_image(im)  # 替换为您的图像
    
    def append_output(self, text):
        
        # 获取当前时间并格式化
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 将时间和文本合并，然后添加到输出框
        self.textEdit_output.append(f"{current_time} - {text}")


    def display_initial_image(self, image_path):
        pixmap = QPixmap(image_path)
        item = QGraphicsPixmapItem(pixmap)
        self.scene.clear()
        self.scene.addItem(item)
        item.setTransform(item.transform().translate(-230, -115))
        #self.graphicsView_3.fitInView(item, Qt.KeepAspectRatio)  # 确保适应item
        self.graphicsView_3.scale(0.43, 0.43)  # sx, sy是缩放因子，根据需要调整

    def display_image(self,im):
        
        # pixmap = QPixmap.fromImage(im)
        
        # # self.label_display.setPixmap(pixmap)
        # scaled_pixmap = pixmap.scaled(self.label_display.size(), Qt.KeepAspectRatio)
        # self.label_display.setPixmap(scaled_pixmap)
        # # 显示 QLabel
        # # self.label_display.setPixmap(pixmap)
        # #self.label_display.show()
                # 将QImage转换为QPixmap
        self.scene_1 = QGraphicsScene(self)
        # 将场景设置给QGraphicsView
        self.graphicsView.setScene(self.scene_1)
        pixmap = QPixmap.fromImage(im)
        # 创建图形项
        item = QGraphicsPixmapItem(pixmap)
        # 清除场景中之前的所有项
        self.scene_1.clear()
        # 将图形项添加到场景中
        self.scene_1.addItem(item)
        # 可选：调整视图的缩放以适应图像
        self.graphicsView.fitInView(item, Qt.KeepAspectRatio)
        # self.graphicsView.scale(1.1, 0.95)  # sx, sy是缩放因子，根据需要调整
        self.current_image = im # 更新当前图像.当用户选择菜单中的"图片另存为"选项时，save_image函数将能够访问当前显示的图像并将其保存到用户指定的路径。确保在调用display_image函数显示图像时，self.current_image已经被正确设置。
    
    def draw_T_P(self):
        import pandas as pd
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
        # 读取数据文件
        # 假设数据文件是以空格或制表符分隔的文本文件
        if self.atm_comboBox_model.currentText() == "美国标准大气":
            df = pd.read_csv('usstand_change.dat', delim_whitespace=True, names=['Height', 'Pressure', 'Temperature', 'A', 'B'])
        else:
            df = pd.read_csv('Profile_0001', sep='\s+', header=None)
            df.columns = ['Pressure', 'Temperature', 'H2O', 'CO2', 'O3']
        profiletype = self.comboBox_profile.currentText()
        profiletype_dic = {'温度':'Temperature','水汽':'H2O','二氧化碳':'CO2','臭氧':'O3'}
        title_dic = {'温度':'Temperature Profile','水汽':'H2O Profile','二氧化碳':'CO2 Profile','臭氧':'O3 Profile'}
        xlabel_dic = {'温度':'Temperature ($K$)','水汽':'H2O Concentration($g/m³$)','二氧化碳':'CO2 Concentration($ppmv$)','臭氧':'O3 Concentration($ppmv$)'}
        # 为列命名，这里假设文件没有列标题
        
        dpi=float(600)
        fig = plt.figure(figsize=(8.8763, 5.4),dpi=dpi)
        ax = fig.add_subplot(111)

        # 绘制温度随气压变化的廓线图
        # 假设气压列代表高度，这通常是倒过来的，即气压越低，高度越高
        ax.plot(df[profiletype_dic[profiletype]],df['Pressure'], c='r')
        # plt.plot(df['H2O'], df['Pressure'])
        # plt.plot(df['CO2'], df['Pressure'])
        # plt.plot(df['O3'], df['Pressure'])
        # 因为气压与高度成反比，所以我们需要反转y轴
        plt.gca().invert_yaxis()

        # 添加图表标题和轴标签
        plt.title(title_dic[profiletype], fontsize=18)
        plt.xlabel(xlabel_dic[profiletype], fontsize=18)
        plt.ylabel('Pressure (hPa)', fontsize=18)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        canvas = FigureCanvas(fig)
        canvas.draw()
        
        width, height = fig.get_size_inches() * fig.get_dpi()
        im = QImage(canvas.buffer_rgba(), int(width), int(height), QImage.Format_ARGB32)
        # plt.show()
        window.display_image(im)  # 替换为您的图像
    


    def plt(self,x,y,linetype,colortype,x1,x2,y1,y2,dpi):
        import numpy as np
        # import matplotlib
        matplotlib.use('Qt5Agg') # 使用TkAgg后端
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

        # 验证 value_a 和 value_b 是否可以转换为浮点数
        # try:
        #     value_a = float(value_a)
        #     value_b = float(value_b)
        # except ValueError:
        #     print("请输入有效的数字。")
        #     return  # 输入无效时提前返回8.0763, 5  9.95, 6.16
        dpi=float(dpi)
        fig = plt.figure(figsize=(8.0763, 5),dpi=dpi)
        ax = fig.add_subplot(111)
        # fig.subplots_adjust(left=0.12, right=0.92, bottom=0.12, top=0.92)
        #plt.tight_layout()
        # pic_type=self.comboBox_drawtype.currentText()
        # if pic_type == 'radation':
        plt.xlabel('Wavenumber   $cm^{-1}$', fontsize=18)
        plt.ylabel('Brightness temperature   $K$', fontsize=18)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.title('Brightness temperature spectrum', fontsize=20)
        # pi = np.pi
        # x = np.arange(-pi, pi, 0.01)
        
        # y =value_a* np.sin(value_b*x)
# 此处有bug，应该是matplotlib应用在ui中出现的，红色为b，蓝色为r。
        ax.plot(x, y,c=colortype,linestyle=linetype)
        # 找到最大y值及其对应的x值
        index_of_max_y = np.argmax(y)
        max_x = x[index_of_max_y]
        max_y = np.max(y)
        # 在最大值点处添加一个标记
        ax.scatter(max_x, max_y, color='red')  # 使用红色标记最大值点
        ax.axvline(x=max_x, color='red', linestyle='--')  # 垂直线
        ax.axhline(y=max_y, color='red', linestyle='--')  # 水平线
        ax.text(max_x, max_y, f'({max_x:.1f}, {max_y:.1f})', color='red', verticalalignment='bottom', horizontalalignment='right',fontsize=15)



        x1=float(x1)
        x2=float(x2)
        y1=float(y1)
        y2=float(y2)
        
        plt.xlim((x1,x2))
        plt.ylim((y1,y2))
        #plt.savefig('sine_wave.png')
        #plt.close()
        canvas = FigureCanvas(fig)
        canvas.draw()
        
        width, height = fig.get_size_inches() * fig.get_dpi()
        im = QImage(canvas.buffer_rgba(), int(width), int(height), QImage.Format_ARGB32)
        # plt.show()
        return im
    def save_image(self):
    # 弹出文件保存对话框
        file_path, _ = QFileDialog.getSaveFileName(self, "保存图片", "", "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)")
        if file_path:
            self.append_output(f"保存图像至: {file_path}")  # 调试信息
            if self.current_image:
                #print("当前图像有效")  # 额外的调试信息
                self.append_output("当前图像有效")
                result = self.current_image.save(file_path)
                if result:
                    self.append_output("图像保存成功")  # 调试信息
                else:
                    self.append_output("图像保存失败")  # 调试信息
            else:
                self.append_output("无法保存，当前图像为空或不可用")  # 调试信息
        else:
            self.append_output("保存操作取消")  # 调试信息

    #####案例管理功能实现####
    def create_case(self):
        path, _ = QFileDialog.getSaveFileName(self, "创建案例", "", "Text Files (*.txt)")
        if path:
            self.casefile_path = path
            with open(self.casefile_path, 'w') as file:
                pass  # 创建一个空文件
            print("案例已创建：", self.casefile_path)

    def open_case(self):
        path, _ = QFileDialog.getOpenFileName(self, "打开案例", "", "Text Files (*.txt)")
        if path:
            with open(path, 'r') as file:
                self.read_parameters = list(map(str, file.readlines()))
            self.set_openparameters()
            # self.sp_lineEdit_wavmin.setText(self.read_parameters[0])
            print("案例已打开，参数：", self.read_parameters)
    def set_openparameters(self):
        #self.sp_comboBox_resolution.setCurrentIndex(1)       {'实线':'-','虚线':'--','点划线':'-.'}
        resolution_dic = {'0.5':0,'0.1':1,'0.05':2,'0.01':3}
        stream_dic = {'32':0,'24':1,'12':2,'8':3}
        model_dic = {'用户自定义':0,'热带':1,'中纬度夏天':2,'中纬度冬天':3,'亚北极夏天':4,'亚北极冬天':5,'美国标准大气':6}
        self.sp_lineEdit_wavmin.setText(self.read_parameters[0])
        self.sp_lineEdit_wavmax.setText(self.read_parameters[1])
        # self.sp_comboBox_resolution.setCurrentIndex(1)
        self.sp_comboBox_resolution.setCurrentIndex(resolution_dic[str(self.read_parameters[2]).strip()])
        self.sp_comboBox_streams.setCurrentIndex(stream_dic[str(self.read_parameters[3]).strip()])
        self.atm_comboBox_model.setCurrentIndex(model_dic[str(self.read_parameters[4]).strip()])
        self.geo_lineEdit_angel.setText(self.read_parameters[5])
        self.surface_lineEdit_TEMP.setText(self.read_parameters[6])
        self.surface_lineEdit_reflection.setText(self.read_parameters[7])
        
    def save_case(self):
        wavminsp = self.sp_lineEdit_wavmin.text()  # 读取lineEdit的值
        wavmaxsp = self.sp_lineEdit_wavmax.text()  # 读取lineEdit的值
        resolutionsp = self.sp_comboBox_resolution.currentText()  # 读取lineEdit的值
        streamssp = self.sp_comboBox_streams.currentText()  # 读取lineEdit的值
        modeltype = self.atm_comboBox_model.currentText()
        angelgeo = self.geo_lineEdit_angel.text()  # 读取lineEdit的值
        surfaceTEMP = self.surface_lineEdit_TEMP.text()  # 读取lineEdit的值
        surfacereflection = self.surface_lineEdit_reflection.text()  # 读取lineEdit的值
        saveparameters = [wavminsp,wavmaxsp,resolutionsp,streamssp,\
                      modeltype,angelgeo,surfaceTEMP,surfacereflection]
        with open(self.casefile_path, 'w') as file:
            file.write('\n'.join(map(str, saveparameters)))
        print("案例已保存")

    def save_as_case(self):
        path, _ = QFileDialog.getSaveFileName(self, "另存为案例", "", "Text Files (*.txt)")
        wavminsp = self.sp_lineEdit_wavmin.text()  # 读取lineEdit的值
        wavmaxsp = self.sp_lineEdit_wavmax.text()  # 读取lineEdit的值
        resolutionsp = self.sp_comboBox_resolution.currentText()  # 读取lineEdit的值
        streamssp = self.sp_comboBox_streams.currentText()  # 读取lineEdit的值
        modeltype = self.atm_comboBox_model.currentText()
        angelgeo = self.geo_lineEdit_angel.text()  # 读取lineEdit的值
        surfaceTEMP = self.surface_lineEdit_TEMP.text()  # 读取lineEdit的值
        surfacereflection = self.surface_lineEdit_reflection.text()  # 读取lineEdit的值
        saveas_parameters = [str(wavminsp).strip(),str(wavmaxsp).strip(),str(resolutionsp).strip(),str(streamssp).strip(),\
                      str(modeltype).strip(),str(angelgeo).strip(),str(surfaceTEMP).strip(),str(surfacereflection).strip()]
        if path:
            with open(path, 'w') as file:
                file.write('\n'.join(map(str, saveas_parameters)))
            print("案例已另存为：", path)
    #######################



    def showparameter_pop(self):
        self.parameterPopInstance = parameter_pop()  # 创建弹窗实例
        self.parameterPopInstance.show()  # 显示弹窗
    def showatm_pop(self):
        self.atmPopInstance = atm_pop()  # 创建弹窗实例
        self.atmPopInstance.modelChanged.connect(self.accept_modelatm)
        self.atmPopInstance.show()  # 显示弹窗
    def showcloud_pop(self):
        self.cloudPopInstance = cloud_pop()  # 创建弹窗实例
        self.cloudPopInstance.show()  # 显示弹窗
    def showgeo_pop(self):
        self.geoPopInstance = geo_pop()  # 创建弹窗实例
        self.geoPopInstance.angelChanged.connect(self.accept_angelgeo)  # 连接信号到槽函数
        self.geoPopInstance.show()  # 显示弹窗    
    def showsurface_pop(self):
        self.surfacePopInstance = surface_pop()  # 创建弹窗实例
        self.surfacePopInstance.tempChanged.connect(self.accept_tempsurface)  # 连接信号到槽函数
        self.surfacePopInstance.reflectionChanged.connect(self.accept_reflectionsurface)
        self.surfacePopInstance.show()  # 显示弹窗


    def showspectral_pop(self):
        self.spectralPopInstance = spectral_pop()  # 创建弹窗实例
        self.spectralPopInstance.wavminChanged.connect(self.accept_wavminsp)
        self.spectralPopInstance.wavmaxChanged.connect(self.accept_wavmaxsp)
        self.spectralPopInstance.resolutionChanged.connect(self.accept_resolutionsp)
        self.spectralPopInstance.streamsChanged.connect(self.accept_streamssp)
        self.spectralPopInstance.show()  # 显示弹窗


####此处为弹窗，类型为Widget,作用为修改参数
from Ui_parameter_pop import Ui_widgettestpop
from Ui_inputsetone_atm import Ui_Widget_atm
from Ui_inputsettwo_cloud import Ui_Widget_could
from Ui_inputsetthree_geo import Ui_Widget_geo
from Ui_inputsetfour_surface import Ui_Widget_surface
from Ui_inputset_sp import Ui_Widget_spectral
class parameter_pop(QWidget, Ui_widgettestpop):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_closeparameterpop.clicked.connect(self.close)
class atm_pop(QWidget, Ui_Widget_atm):
    modelChanged = Signal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.atm_pushButton_cancel.clicked.connect(self.close)
        self.atm_pushButton_ok.clicked.connect(self.emitatmSignal)
    def emitatmSignal(self):
        modeltype = self.atm_comboBox_model.currentText()
        self.modelChanged.emit(modeltype)
        self.close()




class cloud_pop(QWidget, Ui_Widget_could):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class geo_pop(QWidget, Ui_Widget_geo):
    angelChanged = Signal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.geo_pushButton_cancel.clicked.connect(self.close)
        self.geo_pushButton_ok.clicked.connect(self.emitgeoSignal)
    def emitgeoSignal(self):
        angel = self.geo_lineEdit_angel.text()  # 读取lineEdit的值
        self.angelChanged.emit(angel)  # 发射信号，传递温度值
        self.close()  # 可选：点击完成后关闭窗口
        #print(geoangel)
class surface_pop(QWidget, Ui_Widget_surface):
    tempChanged = Signal(str)
    reflectionChanged = Signal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.surface_pushButton_cancel.clicked.connect(self.close)
        self.surface_pushButton_ok.clicked.connect(self.emitsurfaceSignal)

    def emitsurfaceSignal(self):
        temp = self.surface_lineEdit_TEMP.text()  # 读取lineEdit的值
        reflection = self.surface_lineEdit_reflection.text()  # 读取lineEdit的值
        self.tempChanged.emit(temp)  # 发射信号，传递温度值
        self.reflectionChanged.emit(reflection)  # 发射信号，传递温度值,然后在主程序最后的弹窗实例中，将信号与接受信号的槽连接
        self.close()  # 可选：点击完成后关闭窗口

#######哈哈哈哈，wk，这个真的笑死人了
# class int(int):
#     def __new__(cls,*args, **kwargs):
#         res = super().__new__(cls, *args, **kwargs)
#         import random
#         if random.random() < 0.1:
#             res+=10000
#         return res        
#         #print(surfaceTEMP)
#######真的幽默####################
class spectral_pop(QWidget, Ui_Widget_spectral):
    wavminChanged = Signal(str)
    wavmaxChanged = Signal(str)
    resolutionChanged = Signal(str)
    streamsChanged = Signal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sp_pushButton_cancel.clicked.connect(self.close)
        self.sp_pushButton_ok.clicked.connect(self.emitspSignal)
    def emitspSignal(self):
        wavmin = self.sp_lineEdit_wavmin.text()  # 读取lineEdit的值
        wavmax = self.sp_lineEdit_wavmax.text()  # 读取lineEdit的值
        resolution = self.sp_comboBox_resolution.currentText()  # 读取lineEdit的值
        streams = self.sp_comboBox_streams.currentText()  # 读取lineEdit的值
        self.wavminChanged.emit(wavmin)  # 发射信号，传递温度值
        self.wavmaxChanged.emit(wavmax)  # 发射信号，传递温度值
        self.resolutionChanged.emit(resolution)  # 发射信号，传递温度值
        self.streamsChanged.emit(streams)  # 发射信号，传递温度值
        self.close()  # 可选：点击完成后关闭窗口
        #print(surfaceTEMP)






if __name__ =='__main__':
    app = QApplication([])
    window = Mywindow()
    #apply_stylesheet(app, theme='light_teal.xml')#应用别人的主题
    
    window.show()
    app.exec()
