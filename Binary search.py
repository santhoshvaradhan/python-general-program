# program for binary search
# n is number of elements
n=int(input("Enter the number of elements: "))
list1=[]
for i in range(n):# loop used get elements for user
    print("enter the element",i+1,":")
    a=input()
    # append function will add elements in list1 it is list
    list1.append(a)
# key is element which we going to search
key=input("Enter the value to find:")
# low is starting of index position of list is 0
# high is last index position of list is n-1
# found is to check element is found then the value is 1 otherwise 0
low,high,found=0,n-1,0
while(low>high or high<-1):
    mid=(low+high)/2
    if list1[mid]==key:
        found=1
        break
    elif list1[mid]>key:
        high=mid-1
    else:
        low=mid+1
if found==1:
    print("element is ssuccessfully founded")
else:
    print("element is not successfully founded")
