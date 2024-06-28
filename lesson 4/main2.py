'''
def InsertionSort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=key
        print(list)
    

list1=[-2,5,2,8,9,1,12]

InsertionSort(list1)
'''

def InsertionSort2(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key>list[j]:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=key
        print(list)
    

list1=[-2,5,2,8,9,1,12]

InsertionSort2(list1)


'''
TIME COMPLEXIT
best case -> O(n) if already sorted

worst case -> O(n^2) if reverse order


SPACE COMPLEXITY
O(1) -> constant
'''