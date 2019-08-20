#favorite_languages.py
favorite_languages = {
    'jen':'python',
    'Sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }


print("Sarah's favorite language is " +
      favorite_languages['Sarah'].title() +
      ".")

for name,language in favorite_languages.items():
    print(name + "'s favorite language is " + language.title() + '.')


for name in favorite_languages.keys():
    print(name.title())

friends = {'phil','Sarah'}
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi "+name.title()+
              ",I see your favorite language is"+
              favorite_languages[name].title()+".")

if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())



people_required = ['jen','Sarah','kris','phil','edward','eason']
people_done = []

for people in favorite_languages.keys():
    people_done.append(people)

for people in people_required:
    if people in people_done :
        print(people.title() + ",thank you for your apartment.")
    else:
        print(people.title() + ",please take our poll!")


#p96

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'adward':['ruby','go'],
    'phil':['python','haskell'],
    }

for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


        
