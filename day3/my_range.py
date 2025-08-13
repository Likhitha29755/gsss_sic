import sys
def my_range(*var_args):
    if len(var_args) < 1 or len(var_args) > 3:
        print('TypeError.you gave either 0 or more than 3 args')
    elif len(var_args)==1:
        i=0
        while i< var_args[0]:
            yield i  #yeild: some one ask you you give that value
            i+=1          
    elif len(var_args)==2:
        i=var_args[0]
        while i< var_args[1]:
            yield i  
            i += 1
    elif len(var_args) == 3 and var_args[0] < var_args[1]:
        i=var_args[0]
        while i < var_args[1]:
            yield i  
            i += var_args[2]
    elif len(var_args) == 3 and var_args[0] > var_args[1]:
        i=var_args[0]
        while i > var_args[1]:
            yield i  
            i += var_args[2]
    else:
        print('Invalid input')

numbers=list(map(int,sys.argv[1:]))
'''
num =10
for i in my_range(num,20,3):
    print(i,end=',')
'''