#!/bin/bash
LENGTH_OF_ROW = 0
LENGTH_OF_COLUMN = 0

with open('sample.txt', 'r') as file:
    for data in file:
        genap=0
        for info in data.split(" "):
            if info.strip()!='':
                if int(info)%2!=0:
                    genap+=1
        print(data+" => "+str(genap))
        LENGTH_OF_COLUMN = len(info)
    LENGTH_OF_ROW = len(data)

    print("PANJANG KOLOM = "+str(LENGTH_OF_COLUMN))
    print("PANJANG BARIS = "+str(LENGTH_OF_ROW))
        
