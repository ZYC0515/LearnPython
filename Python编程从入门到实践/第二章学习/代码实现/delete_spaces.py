#delete_space.py

#删除开头和末尾多余的空白
favorite_language = 'Python      '
print(favorite_language)

print(favorite_language.rstrip())#rstrip()是去除末端空白

#这是一种暂时的删除，变量中的空白没有真的被删除
#如果要真的被删除，需要将改变后的值存入变量中
favorite_language = favorite_language.rstrip()
print(favorite_language)


favorite_language = '    Python      '
favorite_language.rstrip()#rstrip()是去除末端空白
favorite_language.lstrip()#lstrip()是去除开头端空白
favorite_language.strip()#strip()是去除两端空白
