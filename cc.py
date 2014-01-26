from pushover import sendNotification

def words(fileobj):
    for line in fileobj:
        for word in line.split():
            yield word



foundwords = ''

with open("test.txt") as wordfile:
    wordgen = words(wordfile)
    for word in wordgen:
        if 'establecimiento' in word:
            foundwords+=next(wordgen, None)

            for word in wordgen:
                if 'por' in word:
                    break
                else:
                    foundwords += ' '
                    foundwords += word
            break

sendNotification(foundwords)
print foundwords
print len(foundwords)