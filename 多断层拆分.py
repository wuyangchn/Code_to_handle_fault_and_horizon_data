# -*- coding: utf-8 -*-
# Author: Wuy
# Python 3.6

# 主要实现目的：
# 拆分地层数据，以关键词“n5w3d_6_F”切分txt文件，并将每一个分段单独保存为以特定名字命名的txt文本中
# 第一个关键词之前的内容不用保存

from datetime import datetime

target_dir = 'Y:/断层拆分/'
key = 'n5w3d_6_F'

def Fun():
    line_num = 0
    output_num = 0
    key_line_list = []
    get_key_list = []
    print('开始')
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    f = open('Y:/n5w3d_fault - 副本.txt','r')

    data = f.readlines()

    f.close()

    find_list = []
    
    for eachline in data:
        
        if key in eachline:
            key_line_list.append(line_num)
            text = eachline[eachline.rfind(key):15]
            get_key_list.append(text)
            print('第%s行：%s' % (line_num + 1,text))
            find_list.append('第%s行：%s' % (line_num + 1,text))

            n = len(key_line_list)

            if n >= 2:
                output_num += 1
                output_lines = data[key_line_list[n-2]:key_line_list[n-1]]

                output_path = target_dir + get_key_list[n-2] + '-' + str(output_num) + '.txt'
                with open(output_path,'w') as v:
                    for line in output_lines:
                        v.write(line)
                print('---------------------------------------------')
                print('保存文件：%s' % (get_key_list[n-2] + '-' + str(output_num) + '.txt'))
                print('---------------------------------------------')
                    
        line_num += 1

    output_num += 1
    output_lines = data[key_line_list[n-1]:]

    output_path = target_dir + get_key_list[n-1] + '-' + str(output_num) + '.txt'
    with open(output_path,'w') as v:
            for line in output_lines:
                v.write(line)
    print('---------------------------------------------')
    print('保存文件：%s' % (get_key_list[n-1] + '-' + str(output_num) + '.txt'))
    print('---------------------------------------------')

    with open('Y:/Projects/2020-07南黄海盆地与上扬子地台对比/0 数据/歧口凹陷地层和断层数据？/关键词出现行数.txt','w') as v:
            for line in find_list:
                v.write(line + '\n')

		# 记录关键词出现行数，仅用于后期检验数据
    print('---------------------------------------------')
    print('保存文件：%s' % (target_dir + '关键词出现行数.txt'))
    print('---------------------------------------------')
    

    print('完成')
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    Fun()
