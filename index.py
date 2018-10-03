#!/bin/bash

with open('sample.txt', 'r') as file:
    for data in file:
        genap=0
        for info in data.split(" "):
            if info.strip()!='':
                if int(info)%2!=0:
                    genap+=1
        print(data+" => "+str(genap))
