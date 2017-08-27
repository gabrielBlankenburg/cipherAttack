import collections

# Returns a dictionary with the frequencies of each character of the crypted text
def getFrequency(cryptedText):
    return collections.Counter(cryptedText)

# Returns all the text from a file
def getCryptedText(filePath):
    filePath = open(filePath, "r")
    cryptedText = ''
    for i in filePath:
        # Removes the \n
        cryptedText = cryptedText + i.replace('\n', '')
    return cryptedText

# Replace the characters of a string
def replaceStr(string, toReplace, replace):
    return string.replace(toReplace, replace)

# Finds out a given sequence (use @ to replace ANY char). Notice that if you already know the ENTIRE key use decrypt
def findSequence(cryptedText, sequence):
    # Saves the characters that matches
    dic = {}
    # i is the index of cryptedText and j is the character
    for (i, j) in enumerate(cryptedText):
        if j == sequence[0] or sequence[0] == "@":
            aux = ""
            # k is the index of sequence, l is the character
            for (k, l) in enumerate(sequence):
                # Verify if it isn't the end of the cryptedText
                if (len(cryptedText) >= i + k + 1):
                    # Check if the characteres match
                    if cryptedText[i+k] == l or l == "@":
                        aux = aux + cryptedText[i+k]
                    else:
                        aux = ""
                        break
                elif len(sequence) != k + 1 or l != "@":
                    aux = ""
                    break
            if aux != "":
                # If there is the key, it sums one else it becomes one
                if not aux in dic:
                    dic[aux] = 1
                    aux = ""
                else:
                    dic[aux] += 1
                    aux = ""
    return dic

# It decrypts all the text, to use it be sure that the dictionary key have the ENTIRE key, if you want to replace some characters use replaceStr instead
def decrypt(cryptedText, dictionaryKey):
    for i in cryptedText:
        i = dictionaryKey[i]
    return cryptedText
    
print
print "Some Hints: "
print
print "First finds out the frequency of each character using getFrequency"
print 
print "Then try to find out some usual words in the language. e.g. in english 'the' is often used"
print
print "If you want to visualize better the text use replaceStr. I DO RECOMENDO to do it in an aux variable, so it won't affect the text that you are dealing with"
print 
print "If you want to know more about each method, check out this on github: https://github.com/gabrielBlankenburg/cipherAttack"
print
