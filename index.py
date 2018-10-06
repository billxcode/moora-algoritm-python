#!/bin/bash
LENGTH_OF_ROW = 0
LENGTH_OF_COLUMN = 0

with open('data/sample.txt', 'r') as file:
    with open('result/clean.txt', 'w') as newfile:
        for newdata in file:
            data_info = newdata.split(' ')
            data_count = len(data_info)
            for index, newdimension in enumerate(data_info):
                if newdimension!='' and newdimension!='\n':
                    if index<(data_count-2):
                        newfile.write(newdimension.strip()+',')
                    else:
                        newfile.write(newdimension.strip()+'\n')

print('success clean dimension!')

with open('result/clean.txt', 'r') as file:
    with open('result/sqr.txt', 'w') as newfile:
        for data in file:
            datainfo = data.split(',')
            datacount = len(datainfo)
            for index, newdata in enumerate(datainfo):
                datainfo[index] = int(datainfo[index])**2
                if index<(datacount-1):
                    newfile.write(str(datainfo[index])+' ') 
                else:
                    newfile.write('\n')

print('success sqr dimension')

with open('result/sqr.txt') as file:
    with open('result/sumrow.txt', 'w') as newfile:
        for data in file:
            datainfo = data.split(' ')
            datacount = len(datainfo) 
            sum_row = 0
            for index, newdata in enumerate(datainfo):
                if newdata!='\n':
                    sum_row += int(newdata)
            # print('=> '+str(sum_row))
            newfile.write(str(sum_row).rstrip('\n')+',')

print('success sum all rows')


# with open('total_perbaris.txt', 'r')
