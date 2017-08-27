import collections

# Returns a dictionary with the frequences of each character of the crypted text
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

# Finds out a given sequence (use @ to replace ANY char)
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

print "#To open a file that contains the crypted text, use getCryptedText(filepath)"
print "#To see the frequency of words, use the getFrequency(cryptedText), where cryptedText is the string to find the frequency"
print "#To find a sequence, use findSequence(string, cryptedText), where string is the pattern you want to find out and cryptedText the own crypted text (in this case @ means any char)"
print "#To replace a string, use replaceStr(string, toReplace, replace), string is the string that you want to change, to replace is the characters that you want to replace and replace is the replacement"
