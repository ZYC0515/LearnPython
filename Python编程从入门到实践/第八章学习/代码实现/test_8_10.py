#test_8_10.py

magicians = ["eason zhu",'qian liu']

def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = "the Great " + magician
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
    
make_great(magicians)
show_magicians(magicians)
