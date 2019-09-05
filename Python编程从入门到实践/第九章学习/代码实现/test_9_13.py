from collections import OrderedDict

vocabulary_book = OrderedDict()
vocabulary_book['print'] = '打印输出信息'
vocabulary_book['del'] = '删除信息'
vocabulary_book['def'] = '定义函数'

for key,value in vocabulary_book.items():
    print(key + ":" + value)