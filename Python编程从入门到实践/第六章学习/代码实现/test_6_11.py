#test_6_11.py

cities = {
    
    'shanghai':{
        'country':"china",
        'population':5000000,
        'fact':'beautiful'
        },

    'beijing':{
        'country':"china",
        'population':5000000,
        'fact':'nice'


        },


    }

for city,city_info in cities.items():
    print("\nCity: "+city)
    print("Country: "+city_info['country'])
    print("Population: "+str(city_info['population']))
    print("Fact: "+city_info['fact'])



