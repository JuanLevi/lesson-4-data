
'''
def BubbleSort(list):

    for i in range(len(list)):

        for j in range(len(list)-1):

            if list[j]>list[j+1]:

                temp=list[j]

                list[j]=list[j+1]
                list[j+1]=temp

list1=[-2,5,2,8,9,1,12]

BubbleSort(list1)

print(list1)
'''

def BubbleSort(list):

    for i in range(len(list)):

        for j in range(len(list)-1):

            if list[j]<list[j+1]:

                temp=list[j]

                list[j]=list[j+1]
                list[j+1]=temp
        print(list)

list1=[-2,5,2,8,9,1,12]

BubbleSort(list1)


'''
TIME COMPLEXIT
best case -> O(n) if already sorted

worst case -> O(n^2) if reverse order


SPACE COMPLEXITY
O(1) -> constant
'''