
import os
import numpy as np
from scipy.interpolate import interp1d


epsilon = 1e-8


def main(particleType:str, band_mode:int,
         outRad:list or np.ndarray,
         wl_or_wn:int=1, wl_start:float=0, wl_end:float=0, wl_step:float=0,
         nstr:int=128):
    """
    :param particleType: 粒子类型(与数据文件夹名一致)
    :param band_mode: 是否执行波段响应函数积分，0 or 1
    :param outRad: 指定的粒子有效半径列表
    :param wl_or_wn: 输入变量为波长还是波数, 1: wl; 2: wn
    :param wl_start, wl_end, wl_step: 波长(或波数)起始、结束、步长
    :param nstr: Legendre展开项数
    """
    inputDir = r'./INPUT/'
    inSsdDir = fr'./DATABASE/SSD/{particleType}/'
    outSsdDir = fr'./OUTPUT/{particleType}/SSD/'
    # 创建输出文件夹
    if not os.path.exists(outSsdDir):
        os.makedirs(outSsdDir)

    # SSD
    if not band_mode:
        if wl_start == wl_end == 0:
            raise ValueError('Band mode is False, but the wavelength input is empty.')
        outWl = np.arange(wl_start, wl_end + epsilon, wl_step)
    else:
        band_info = np.loadtxt(r'./INPUT/input_band.dat', skiprows=1, usecols=(1, 2, 3))
        outWl = np.empty((0,), dtype=float)
        for i in range(band_info.shape[0]):
            bandWl = np.arange(band_info[i, 0], band_info[i, 2] + epsilon, band_info[i, 1])
            outWl = np.append(outWl, bandWl)
        outWl = np.unique(outWl)

    # 检查输入模式为波长还是波数
    if wl_or_wn == 2:
        # 波数转为波长
        outWl = 10000.0 / outWl
    if (outWl > 99).any():
        # 默认波长不超过99
        raise ValueError('The maximum wavelength is greater than 99.')

    gene_wl_file(inputDir, outWl)            # 写入波长文件
    gene_re_file(inputDir, outRad)           # 写入有效半径文件
    process_ssd(inSsdDir, outSsdDir, outWl)  # 插值并写入单散射特性文件

    # BSD
    outBsdDir = fr'./OUTPUT/{particleType}/BSD/'
    if not os.path.exists(outBsdDir):
        os.makedirs(outBsdDir)
    single_to_bulk(outSsdDir, outBsdDir)

    # CSD
    outCsdDir = fr'./OUTPUT/{particleType}/CSD/'
    if band_mode:
        if not os.path.exists(outCsdDir):
            os.makedirs(outCsdDir)
        bulk_to_band(outBsdDir, outCsdDir)

    # ESD
    outEsdDir = fr'./OUTPUT/{particleType}/ESD/'
    if not os.path.exists(outEsdDir):
        os.makedirs(outEsdDir)
    if band_mode:
        bulk_to_expansion(outCsdDir, outEsdDir, band_mode, nstr)
    else:
        bulk_to_expansion(outBsdDir, outEsdDir, band_mode, nstr)


def gene_wl_file(inputDir:str, wavelength):
    radFile = os.path.join(inputDir, 'wl.dat')
    with open(radFile, 'w') as f:
        f.write(f'{len(wavelength):d}\n')
        for i in range(len(wavelength)):
            f.write(f'{wavelength[i]:10.4f}\n')


def gene_re_file(inputDir:str, rad):
    radFile = os.path.join(inputDir, 'input_re.dat')
    with open(radFile, 'w') as f:
        f.write(f'{len(rad):d}\n')
        for i in range(len(rad)):
            f.write(f'{rad[i]:d}\n')


def process_ssd(inSsdDir, outSsdDir, outWl):
    """
    插值并写入单散射特性文件
    :param inSsdDir:
    :param outSsdDir:
    :param outWl:
    :return:
    """
    # SSD 单散射数据
    infile = os.path.join(inSsdDir, 'isca.dat')
    outfile = os.path.join(outSsdDir, 'isca.dat')

    isca_data = np.loadtxt(infile)
    totalWl = isca_data[:, 0].reshape((445, 189))[:, 0]
    rad = isca_data[:, 1].reshape((445, 189))[0, :]
    volume = isca_data[:, 2].reshape((445, 189))[0, :]
    area = isca_data[:, 3].reshape((445, 189))[0, :]
    qext = isca_data[:, 4].reshape((445, 189))
    ssa = isca_data[:, 5].reshape((445, 189))
    g = isca_data[:, 6].reshape((445, 189))
    f_q = interp1d(totalWl, qext, axis=0, kind='linear')
    out_q = f_q(outWl)
    f_w = interp1d(totalWl, ssa, axis=0, kind='linear')
    out_w = f_w(outWl)
    f_g = interp1d(totalWl, g, axis=0, kind='linear')
    out_g = f_g(outWl)
    with open(outfile, 'w') as f:
        for i in range(len(outWl)):
            for j in range(len(rad)):
                f.write(f'{outWl[i]:18.8e}{rad[j]:18.8e}{volume[j]:18.8e}{area[j]:18.8e}'
                        f'{out_q[i, j]:18.8e}{out_w[i, j]:18.8e}{out_g[i, j]:18.8e}\n')

    for p_file in ['P11.dat', 'P12.dat', 'P22.dat', 'P33.dat', 'P43.dat', 'P44.dat']:
        infile = os.path.join(inSsdDir, p_file)
        outfile = os.path.join(outSsdDir, p_file)
        p_data = np.loadtxt(infile)
        p = p_data[1:, :].reshape((445, 189, 498))  # todo 水云数据量大小有不同445*3000*721
        f_p = interp1d(totalWl, p, axis=0, kind='linear')
        out_p = f_p(outWl)
        with open(outfile, 'w') as f:
            ang = p_data[0, :]
            for i in range(len(ang)):
                f.write(f'{ang[i]:18.8e}')
            f.write(f'\n')

            for i in range(len(outWl)):
                for j in range(out_p.shape[1]):
                    for k in range(out_p.shape[2]):
                        f.write(f'{out_p[i, j, k]:18.8e}')
                    f.write('\n')


def single_to_bulk(ssdDir, bsdDir):
    os.system(f'./Single_To_Bulk.out {ssdDir} {bsdDir}')


def bulk_to_band(bsdDir, csdDir):
    os.system(f'./Bulk_To_Band.out {bsdDir} {csdDir}')


def bulk_to_expansion(inDir, esdDir, band_mode, nstr):
    os.system(f'./Expansion.out '
              f'{inDir} {esdDir} {band_mode} {nstr}')


if __name__ == '__main__':
    # 第一行 粒子类型
    particleType = 'C8R050'

    # 第二行 粒子有效半径
    # 第一位：输入类型，1：首+尾+步长（共3个输入量）；2：指定序列（不定长）
    # 第二位开始：如类型指定格式
    # rad = np.array([2,4,6,8,10,12,14,16,18,20,
    #                 24,28,32,36,40,44,48,52,56,60])
    rad = np.arange(5, 90 + epsilon, 5)

    # 第三行 波长
    # 第一位：wl_or_wn
    wl_or_wn = 1  # 1: wl; 2: wn
    # 第二位开始：首+尾+步长（共3个输入量）
    wl_start = 0.3
    wl_end = 1.0
    wl_step = 0.1

    # 第四行 带模式
    band_mode = 1  # 1：on；0：off

    main(particleType, band_mode,
         rad,
         wl_or_wn, wl_start, wl_end, wl_step)

    # 第五行 粒子尺度分布类型（主程序不读取）
    # 第一位：分布类型，1：gamma；2：lognormal
    # 第二位开始：相关输入参数（预留3个）
    # gamma分布：只有一个输入参数b，其余置0
    # lognormal分布：只有一个输入参数sigma_g，其余置0
