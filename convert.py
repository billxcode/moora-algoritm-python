
FILE_NAME = input('Tuliskan nama filenya: ')

result_convert = open('result/result_convert.txt', 'w+')
with open('data/'+FILE_NAME+'.csv', 'r') as smartdata:
	for line in smartdata:
            index = 0
            panjang = line.split(',')
            for perline in panjang:
                    perline = perline.strip()
                    if((perline == '-') or (perline == '#DIV/0!') or (perline == '#REF!') or (perline == '')):
                        perline = 0	
                    perline = str(perline).replace(",", ".")
                    if(index<(len(panjang)-1)):
                        cetak = str(perline) + ','
                    else:
                        cetak = str(perline)
                    index+=1
                    result_convert.write(cetak)
            result_convert.write('\n')
result_convert.close()

result_final = open('result/result_final.txt', 'w+')

with open('result/result_convert.txt', 'r') as result_convert:
    for line in result_convert:
        index = 0
        for perline in line.split('"'):
            if(index>0):
                if(index%2!=0):
                    perline = perline.replace(',', '.')
            index+=1
            result_final.write(perline)
result_final.close()

real_final = open('result/csv/'+FILE_NAME+'_RESULT.csv', 'w+')
hitung_jumlah = 0
with open('result/result_final.txt', 'r') as result_final:
    for line in result_final:
        index = 0
        panjang = line.split(',')
        for perline in panjang:
            datahasil = 0
            panjang_perline = len(perline.split('.'))
            if(panjang_perline > 2):
                bantuan = perline.split('.')
                if(len(bantuan[panjang_perline-1].split('\n'))>1):
                    datahasil = bantuan[0]+'.'+bantuan[1]+'\n'
                else:
                    datahasil = bantuan[0]+'.'+bantuan[1]
            else:
                datahasil = perline
            index += 1
            if(index<len(panjang)):
                cetak = str(datahasil) + ','
            elif(index>len(panjang)):
                cetak = '\n'
            else:
                cetak = str(datahasil)
            if(index%3==0):
                real_final.write(cetak)
real_final.close()





