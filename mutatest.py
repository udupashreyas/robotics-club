from mutagen.mp3 import MP3
audio = MP3("C:\Users\udupa\Downloads\Music\Bombay Vikings - Chhod Do Aanchal (Apniisp.Com).mp3")
minutes = audio.info.length / 60.0
kbps =  audio.info.bitrate / 1000.0
print "length : " + str(minutes) + " mins"
print "bitrate : " + str(kbps) + " kbps"