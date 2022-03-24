import random
def rand_elem(array):
    a=random.choice(array)
    b=random.choice(array)
    c=random.choice(array)
    print(a,b,c)

array=[2,6,4,8,35,0,17,23,45,56,82]
rand_elem(array)
