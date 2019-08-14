#test_list_3_4.py

#3_4
people = ['Lily','Harry','James','Bryant']
print(people[0]+",why not come to my house for dinner?")
print(people[1]+",why not come to my house for dinner?")
print(people[2]+",why not come to my house for dinner?")
print(people[3]+",why not come to my house for dinner?")
print("\n")

#3_5
print(people[1]+" can't come here.")
people[1] = 'Judy'
print(people[0]+",why not come to my house for dinner?")
print(people[1]+",why not come to my house for dinner?")
print(people[2]+",why not come to my house for dinner?")
print(people[3]+",why not come to my house for dinner?")
print("\n")

#3_6
print("We found a bigger table,so we can invite more guests.")
people.insert(0,'Kobe')
people.insert(2,'Alex')
people.append('Nancy')
print(people[0]+",why not come to my house for dinner?")
print(people[1]+",why not come to my house for dinner?")
print(people[2]+",why not come to my house for dinner?")
print(people[3]+",why not come to my house for dinner?")
print(people[4]+",why not come to my house for dinner?")
print(people[5]+",why not come to my house for dinner?")
print(people[6]+",why not come to my house for dinner?")
print("\n")


#3_7
print("We had some situation and we can only invite 2 people now.")
people.pop()
people.pop()
people.pop()
people.pop()
people.pop()
print(people[0]+",hi you can be here today!")
print(people[1]+",hi you can be here today!")
print("\n")


print(str(len(people))+" people have been invited.")
print("\n")

del people[0]
del people[0]#del删除后就只剩一个元素了，要注意。

print(people)
print("\n")





