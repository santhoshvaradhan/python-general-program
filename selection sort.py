# program for selection sort
# n is number of elements
n=int(input("Enter the number of elements: "))
list1=[]
for i in range(n):# loop used get elements for user
    print("enter the element",i+1,":")
    a=int(input())
    # append function will add elements in list1 it is list
    list1.append(a)
print("Before sorting")
print(list1)
for i in range(n):
    minv=i
    for j in range(i+1,n):
        if list1[j]<list1[minv]:
            minv=j
    temp=list1[i]
    list1[i]=list1[minv]
    list1[minv]=temp
print("After sorting")
print(list1)
