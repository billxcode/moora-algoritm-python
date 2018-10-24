#!/bin/bash
from math import sqrt
from cmath import sqrt

NILAI_BOBOT = [0.1, 0.2, 0.3, 0.2, 0.2]

FILE_NAME = input('Tulis nama filenya : ')

# clean data from dirty file text
with open('result/csv/'+FILE_NAME+'.csv', 'r') as file:
    with open('result/clean.txt', 'w') as newfile:
        for newdata in file:
            data_info = newdata.split(',')
            data_count = len(data_info)
            for index, newdimension in enumerate(data_info):
                filterdimension = newdimension.replace('\n', '');
                if filterdimension!='' and filterdimension!='\n':
                    if index<data_count-1:
                        newfile.write(newdimension.strip()+',')
                    else:
                        newfile.write(newdimension.strip()+'\n')
print('success clean dimension!')

# create sqr.txt file that contain sqr for all element dimension
with open('result/clean.txt', 'r') as file:
    with open('result/sqr.txt', 'w') as newfile:
        for data in file:
            datainfo = data.split(',')
            datacount = len(datainfo)
            for index, newdata in enumerate(datainfo):
                filterdimension = newdata.replace('\n', '');
                newdata = float(filterdimension)**2
                if index<=datacount-1:
                    newfile.write(str(newdata)+',') 
            newfile.write('\n')
print('success sqr dimension')

# create file sumrow.txt that contain sum of all rows
with open('result/sqr.txt') as file:
    with open('result/sumrow.txt', 'w') as newfile:
        for data in file:
            datainfo = data.split(',')
            datacount = len(datainfo) 
            sum_row = 0
            for index, newdata in enumerate(datainfo):
                if newdata!='\n':
                    sum_row += float(newdata)
            newfile.write(str(sum_row).rstrip('\n')+',')
print('success sum all rows')

# create normalization file that contain all element that have been normalize
with open('result/sumrow.txt', 'r') as file:
    with open('result/normalization.txt', 'w') as newfile:
        with open('result/sqr.txt', 'r') as sqr:
            for sumrow in file:
                splitIntoColumn = sumrow.split(',')
                indexColumn = 0
                for row in sqr:
                    datainfo = row.split(',')
                    for index, newdata in enumerate(datainfo):
                        if newdata!='\n':
                            if splitIntoColumn[indexColumn]!='':
                                resultPerElement = float(splitIntoColumn[indexColumn])-float(newdata)
                            else:
                                resultPerElement = 0
                            if resultPerElement>0:
                                sqrtElement = sqrt(float(newdata))
                                resultPerElement = sqrt(resultPerElement)
                                result = sqrtElement/resultPerElement
                            else:
                                sqrtElement = 0
                                resultPerElement = 0 
                                result = 0
                            newfile.write(str(result.real)+',')
                    newfile.write('\n')
                    indexColumn += 1
print('success normalized!')

# create file matrix terbobot
newfile = open('result/matrixterbobot.txt', 'w')
with open('result/normalization.txt', 'r') as file:
    for bobot in NILAI_BOBOT:
        for normalization in file:
            splitNormalization = normalization.split(',')
            for index, normalization in enumerate(splitNormalization):
                if normalization!='\n':
                    matrixTerbobot = bobot*float(normalization)
                    if matrixTerbobot==0:
                        newfile.write(str(0)+',')
                    else:
                        newfile.write(str(matrixTerbobot)+',')
            newfile.write('\n')
newfile.close()
print('success create matrixterbobot')

#create file preferensi
newfile = open('result/preferensi_'+FILE_NAME+'.txt', 'w')
with open('result/matrixterbobot.txt', 'r') as datafile:
    for test in datafile:
        datainfo = test.split(',')
        nilaiPreferensi = 0
        for index, preferensi in enumerate(datainfo):
            if preferensi!='\n':
               nilaiPreferensi += float(preferensi)
        if datainfo[0]!='' and datainfo[0]!='\n':
            newfile.write(str(nilaiPreferensi-(float(datainfo[0])*2))+'\n')
newfile.close()
print('success calculate preferensi')
