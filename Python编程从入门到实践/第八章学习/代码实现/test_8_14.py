#test_8_14.py
def build_profile(maker,car_id,**car_info):
    car_profile = {}
    car_profile[maker] = maker
    car_profile[car_id] = car_id
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile

car_profile = build_profile('KOZ','112017',
                            color='red',
                            tow_package=True)
print(car_profile)
