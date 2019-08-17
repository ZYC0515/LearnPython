#conditional_tests.py

txt_0 = 'ABCDefG'
txt_1 = 'abcdefg'

if txt_0.lower() == txt_1.lower():
    print("In some way,they are the same.")
if txt_0 == txt_1:
    print("Actually,they are the same.")
else:
    print("In some way,they are different.")

num_0 = 123
num_1 = 456

if num_0 >= 122 and num_1 >= 457:
    print("Yes!!")
else:
    print("Sorry,wrong numbers.")

if num_0 >= 122 or num_1 >= 457:
    print("emmmm,Yes!")
else:
    print("Sorry,wrong numbers.")


names = ['Eason','Andy','Judy']

name = 'zhu'

if name in names:
    print('Here you are!')
else:
    print('I am waiting for you!')

name = 'Eason'
if name not in names:
    print('Sorry!'+name+",you are not in the list!")
else:
    print('Nice!'+name+",Welcome back!")
    
