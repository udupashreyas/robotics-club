path = "C:\Users\udupa\Downloads\Music\Bombay Vikings - Chhod Do Aanchal (Apniisp.Com).mp3"
from mutagen.id3 import ID3
audio = ID3(path)

print "Artist : %s" % audio["TPE1"].text[0]
print "Track: %s" % audio["TIT2"].text[0]
print "Release Year: %s" % audio["TDRC"].text[0]
