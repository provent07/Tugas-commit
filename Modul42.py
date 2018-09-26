dict={}
list=[]
count=0
while count<10:
    num=int(input("Input number: "))
    list.append(num)
    count+=1
for i in list:
    result=i%42
    dict[result]=0
print(len(dict.keys()))

