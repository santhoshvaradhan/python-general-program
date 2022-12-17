# program for bubble sort
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
for i in range(0,n):
    for j in range(0,n-1):
        if list1[j]>list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
print("After sorting")
print(list1)
