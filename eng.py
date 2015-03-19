import edit

with open("english_words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def closest(word):
	dist = []
	l = len(word)
	for x in english_words:
		dist.append((x,edit.LD(word,x)))
	least = min(dist,key = lambda t : t[1])
	return least[0]

#ans = closest("gyrosc")
#print ans