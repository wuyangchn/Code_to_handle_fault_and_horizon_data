# -*- coding: utf-8 -*-
# Author: Wuy
# Python 3.6

import os
import shutil

def all_files_path(rootDir):
    filepaths = []
    for root, dirs, files in os.walk(rootDir):     # 分别代表根目录、文件夹、文件
        for file in files:                         # 遍历文件
            file_path = os.path.join(root, file)   # 获取文件绝对路径  
            filepaths.append(file_path)            # 将文件路径添加进列表
    return filepaths

def merge_file(path_list,save_path):
    data = []
    for each_file in path_list:
        f = open(each_file,'r')
        each_data = f.readlines()
        for eachline in each_data[2:-1]:
            data.append(eachline)
        f.close()

    with open(save_path,'w') as v:
        for line in data:
            v.write(line)
    print('---------------------------------------------')
    print('保存文件：%s' % (save_path))
    print('---------------------------------------------')

            
if __name__ == "__main__":
    name_list = ['2019_zblq_T20','2019_zblq_Tc40','2019_zblq_Te60',
                 '2019_zblq_Tg','2019_zblq_Tp20','2019_zblq_Ts40',
                 '2019_zblq_Ts60','2019_zblq_Tt20','2019_zblq_Tt60']
    for each_name in name_list:
        dirpath = 'Y:/地层分层数据/' + each_name
        save_path = 'Y:/地层分层数据/' + each_name + '.txt'
        filepaths = all_files_path(dirpath)
        merge_file(filepaths,save_path)
