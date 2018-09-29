num=int(input("Pascal how many?"))
# for i in range(0,num):
#     for j in range(0,(i+1)):
#         print("0")
#         if j==i or j==0:
#             print('1')
#     print()
#list=[]
# for i in range(0, num+1):
#     list.append([])
#     for j in range(0, i+1):
#         if j == i or j == 0:
#             list.append('1')
#         else:
#             list.append(list[i-1][j]+list[i-1][j-1])
#     print(list)

pascal = []
for x in range(num+1):

    if x == 0:
        list = [1]
        pascal.append(list)
        continue
    if x==1:
        list = [1,1]
        pascal.append(list)
        continue

    list = [l for l in range(x+1)]
    for y in range(1,x):
        list[0] = 1
        list[x] = 1
        list[y] = pascal[x-1][y] + pascal[x-1][y-1]

    pascal.append(list)
for i in pascal:
    print(i)