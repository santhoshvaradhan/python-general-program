# program for insertion sort
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
for i in range(1,n,1):
    minv=i
    # for loop cannot iterate using negative vlaue so use while loop 
    j=i-1
    while j>-1:
        if list1[j]>list1[minv]:
            temp=list1[j]
            list1[j]=list1[minv]
            list1[minv]=temp
            minv=minv-1
        j-=1
print("After sorting")
print(list1)
