f=open('Perepis.txt','r')
L=list()

a1=int(input('Укажите 1 границу диапазона'))
a2=int(input('Укажите 2 границу диапазона'))

for i in f:
    s=i
    names=str(s.split(' ')[0])



    dates=(str(s.split('.')[2]))
    datesInt=int(dates)
    L.append(datesInt)
    b=0
    for i in L:
        if i<1978:
            b+=1

print('Раньше 1978г: ',b)
f.close()

f=open('Perepis.txt','r')
for i in f:
    s=i
    names=str(s.split(' ')[0])
    dates=(str(s.split('.')[2]))
    datesInt=int(dates)

    if a1<=datesInt<=a2:
        print(s)

f.close()

