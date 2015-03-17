import musicbrainzngs
from mutagen.id3 import ID3

path = "C:\Users\udupa\Downloads\Music\Jaadu Hai Nasha Hai.mp3"
audio = ID3(path)

musicbrainzngs.set_useragent("trial",1,contact=None)

list_record = []
result = musicbrainzngs.search_releases(artist = audio["TPE1"].text[0])
for artist in result['release-list']:
#    print(u"{id}: {title}".format(id=artist['id'],title=artist['title']))
    list_record.append(artist['id'])

print list_record
#with open("next.jpeg","wb") as img:
#    img.write(musicbrainzngs.get_image_front(list_record[6], size = None))
