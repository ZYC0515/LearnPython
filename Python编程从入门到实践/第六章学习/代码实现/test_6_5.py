#test_6_5.py
rivers = {'nile':'egypt',
          'yellow':'china',
          'yangzi river':'china'
          }

for river,country in rivers.items():
    print("The " + river.title() + " runs through " + country.title())

print("The following rivers have been mentioned: ")
for river in rivers.keys():
    print(river.title())

print("The following countries have been mentioned: ")
for country in set(rivers.values()):
    print(country.title())
