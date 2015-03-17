import musicbrainzngs
from mutagen.id3 import ID3
import edit

path = "C:\Users\udupa\Downloads\Music\Hindi\Chaar Botal Vodka.mp3"
audio = ID3(path)

musicbrainzngs.set_useragent("trial",1,contact=None)

track = audio["TIT2"].text[0]

list_record = []
result = musicbrainzngs.search_releases(release = audio["TIT2"].text[0])
for artist in result['release-list']:
    #print(u"{id}: {title}".format(id=artist['id'],title=artist['title']))
    dist = edit.LD(track, artist['title'])
    #print(u"{title}:{dist}".format(title = artist['title'], dist = dist))
    list_record.append((artist['id'],dist))

least = min(list_record,key = lambda t : t[1])
#print list_record
#print least
#print least[0]
with open("next.jpeg","wb") as img:
   img.write(musicbrainzngs.get_image_front(least[0], size = None))