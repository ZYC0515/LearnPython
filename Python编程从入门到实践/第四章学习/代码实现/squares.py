#squares.py

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    
print(squares)
print("\n")

squares = []
for value in range(1,11):
    squares.append(value**2)
    
print(squares)
print("\n")

digits = [1,2,3,4,5,66,7,8,8,9,0,-1,3,5,6,44,67,54,78,46,24,94,63,99]

print(max(digits))
print(min(digits))
print(sum(digits))
print("\n")


#列表解析法生成数字列表
squares = [value**2 for value in range(1,11)]
print(squares)
print("\n")
