

name = input("Enter the name to be displayed : ")
iteration = len(name)
for i in range(0, iteration):
    for j in range(0, iteration):
        if(i == j):
            print(name[j],sep=" ",end=" " )
        else:
            print("*",sep=" ",end=" ")
    print()

