#test_8_7.py

def make_album(singer,album):
    album_info = {"singer":singer.title(),"album_name":album.title()}
    return album_info


album_1 = make_album('zhu','first_album')
print(album_1)
album_2 = make_album('eason','seconf_album')
print(album_2)
album_3 = make_album('kris','fantastic_album')
print(album_3)


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

album_1 = make_album('zhu','first_album',55)
print(album_1)
album_2 = make_album('eason','seconf_album')
print(album_2)
album_3 = make_album('kris','fantastic_album',2)
print(album_3)
