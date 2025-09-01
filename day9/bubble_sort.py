def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                array[j]=array[j+1]
                array[j+1]=array[j]
            else:


array=[45,32,23,50,1,11,99,50,30,55]
