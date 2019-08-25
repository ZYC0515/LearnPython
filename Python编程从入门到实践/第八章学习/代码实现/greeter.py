#greeter.py

def greeter_user():
    """显示见答案的问候语"""
    print("Hello!")

greeter_user()

def greeter_user(username):
    """显示简单的问候语"""
    print("Hello, " + username + ".")


greeter_user('esaon')

def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()


#这是一个无限循环！
while True:
    print("\nPlease tell me your name: ")

    f_name = input("First name:")

    l_name = input("Last_name:")

    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")




while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last_name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")
