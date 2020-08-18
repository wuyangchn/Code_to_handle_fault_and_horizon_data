# -*- coding: utf-8 -*-
# Author: Wuy
# Python 3.6

#拆分地层数据，查找关键词为“2019_zblq_”

from datetime import datetime

target_dir = 'Y:/地层数据处理/'
key = '2019_zblq_'

def Fun():
    line_num = 0
    output_num = 0
    key_line_list = []
    get_key_list = []
    print('开始')
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    f = open('Y:/zblq_TJ_hor_2019.txt','r')

    data = f.readlines()

    f.close()
    
    for eachline in data:
        
        if key in eachline:
            key_line_list.append(line_num)
            text = eachline[eachline.rfind(key):79]
            get_key_list.append(text)
            print('第%s行：%s' % (line_num + 1,text))

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
    

    print('完成')
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    Fun()
