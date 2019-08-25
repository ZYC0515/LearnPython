#test_8_8.py

def make_album(singer,album,numbers=''):
    if numbers:
        album_info = {"singer":singer.title(),
                      "album_name":album.title(),
                      'numbers':numbers
                      }
    else:
       album_info = {"singer":singer.title(),
                     "album_name":album.title()
                     } 
    return album_info


while True:
    print("Hello! \n(Please enter 'q' at any time to quit.)")
    singer = input("Tell me the singer's name: ")
    if singer == 'q':
        break
    album = input("Tell me the album's name: ")
    if singer == 'q':
        break
    numbers = input("How many songs do we have in this album ? ")
    if singer == 'q':
        break

    album_info = make_album(singer,album,numbers)
    print("\n------album information------")
    print(album_info)
    print("------album information------\n")
