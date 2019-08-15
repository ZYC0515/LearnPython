#test_for_4_3.py

for num in range(1,21):
    print(num)

print("\n")

#4_4
#numbers = [value for value in range(1,1000001)]
#for number in numbers:
#    print(number)

print("\n")

#4_5
numbers = [value for value in range(1,1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print("\n")

#4_6
numbers = [value for value in range(1,20,2)]
for number in numbers:
    print(number)
print("\n")


#4_7
numbers = [value for value in range(3,30,3)]
for number in numbers:
    print(number)
print("\n")


#4_8
numbers = []
for value in  range(1,11):
    number = value**3
    numbers.append(number)

for number in numbers:
    print(number)


print("\n")

#4_9
numbers = [value**3 for value in range(1,11)]
for number in numbers:
    print(number)



