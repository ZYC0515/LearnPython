#test_8_11.py

def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = "the Great " + magician
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ["eason zhu",'qian liu']
show_magicians(magicians)

print("\n")

great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\n")

show_magicians(magicians)
