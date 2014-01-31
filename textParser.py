def words(fileobj):
    for line in fileobj:
        for word in line.split():
            yield word

def getService(fileName, keyword):

    foundwords = ''

    with open(fileName) as wordfile:
        wordgen = words(wordfile)
        for word in wordgen:
            if keyword in word:
                foundwords+=next(wordgen, None)

                for word in wordgen:
                    if 'por' in word:
                        break
                    else:
                        foundwords += ' '
                        foundwords += word
                break

    return foundwords

def getValue(fileName):

    foundwords = ''

    with open(fileName) as wordfile:
        wordgen = words(wordfile)
        for word in wordgen:
            if '$' in word:
                foundwords+="$"
                foundwords+=next(wordgen, None)
                break

            if 'u$s' in word:
                foundwords+="u$s"
                foundwords+=next(wordgen, None)
                break

    return foundwords

def createMessage(service, value):
    return "New expense added. Service: " + service + ". Value: " + value
