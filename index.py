#!/bin/bash
LENGTH_OF_ROW = 0
LENGTH_OF_COLUMN = 0

with open('sample.txt', 'r') as file:
    with open('new_sample.txt', 'w') as newfile:
        for newdata in file:
            data_info = newdata.split(' ')
            data_count = len(data_info)
            for index, newdimension in enumerate(data_info):
                if newdimension!='' and newdimension!='\n':
                    if index<(data_count-2):
                        newfile.write(newdimension.strip()+',')
                    else:
                        newfile.write(newdimension.strip()+'\n')
with open('new_sample.txt', 'r') as file:
    for data in file:
       datainfo = data.split(',')
       for index, newdata in enumerate(datainfo):
           datainfo[index] = int(datainfo[index])**2
           print(str(datainfo[index])+' ', end='')

        
