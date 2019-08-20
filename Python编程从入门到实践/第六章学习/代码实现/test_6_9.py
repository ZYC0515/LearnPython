#test_6_9.py
favorite_places = {
    'Judy':['tokyo','chicago'],
    'Anny':['china'],
    'Wang':['soul','Bangkok'],
    }

for name,places in favorite_places.items():
    if len(places) == 1:
        for place in places:
            print(name + "'s favorite place is " + place)
    if len(places) > 1:
        print(name + "'s favorite places are:")
        for place in places:
            print(place)
