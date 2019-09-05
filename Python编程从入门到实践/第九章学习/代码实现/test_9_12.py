"""
由于该题和test_9_11 相冲突，故不演示代码。

大致就是，将User类放在 user.py,将Privilege类放在privilege.py中，将Admin类放在admin.py类中
由于User类是Admin类的父类，因此在admin.py中要from user import User
在实例文件中，直接 from user import user
                 from admin import Admin
                 from privilege import Privilege
其余部分类同前面的操作，不再赘述。
"""