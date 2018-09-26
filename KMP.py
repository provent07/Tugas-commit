name=str(input("Input name of system: "))
list=[]
for i in name:
     if i.isupper():
         list.append(i)
print("".join(list))


