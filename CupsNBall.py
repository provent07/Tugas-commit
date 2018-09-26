rotate=input("Put rotation in caps: ")
list=['ball','empty1','empty2']
a=list.index('ball')
b=list.index('empty1')
c=list.index('empty2')
for i in rotate:
    if i=='A':
        list[a],list[b]=list[b],list[a]
    elif i=='B':
        list[b],list[c]=list[c],list[b]
    else:
        list[a],list[c]=list[c],list[a]

if list.index('ball')==0:
    print("Left")
elif list.index('ball')==1:
    print("Middle")
else:
    print("Right")
