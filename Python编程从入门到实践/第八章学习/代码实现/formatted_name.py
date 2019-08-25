#formatted_name.py

def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name("jimi",'hendrix')
print(musician)

def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


name = get_formatted_name('Eason','zhu','Li')
print(name)

name = get_formatted_name('Eason','zhu')
print(name)
