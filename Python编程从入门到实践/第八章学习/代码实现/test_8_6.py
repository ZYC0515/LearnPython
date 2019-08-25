#test_8_6.py
def city_country(city_name,country):
    sant = city_name + "," + country
    return sant.title()


test = city_country("shanghai",'china')
print(test)

test = city_country("qingdao",'china')
print(test)

test = city_country("hainan",'china')
print(test)
