#mountain_poll.py

responses = {}

polling_active = True

while polling_active :
    # 提示输入被调查人的名字和回答
    name = input("\nWhat is your name?")
    response  = input("Which mountain would you like to climb someday?")

    #将答案存储在字典中
    responses[name] = response

    #看看是否还有人需要调查
    repeat = input("Would you like to let another person respond? (YES/NO)")
    if repeat == 'NO':
        polling_active = False

#调查结束，显示结果
print("\n---Poll Results---")
for name,response in responses.items():
    print(name + " would like to climb " + response + ".")
