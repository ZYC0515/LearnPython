#test_list_3_10.py

list = ['mountain tai','hongkong','tokyo','yangzi river','English','Chinese']

print(list[0])
print(list[-2])
print('I am a '+list[-1]+'.')
list[1] = 'tai pei'
print(list)

list.append('American')

print(list)

list.insert(0,'Alex')
print(list)

del list[0]
print(list)

list_poped = list.pop(1)
print('I love '+list_poped.title()+' forever!')

list.remove('tokyo')
print(list)

list.sort(reverse = True)
print(list)

print(sorted(list))

list.reverse()
print(list)

print(len(list))

