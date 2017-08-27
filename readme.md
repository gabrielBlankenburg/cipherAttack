# CipherAttack

    This is a simple studying tools. To use it I recommed a list of frequency of the words in the choosen language.
    
## Methods

### getCryptedText(filePath)
    
    It just opens a file in filePath and removes the \n returning the text


### getFrequency(cryptedText)

    It returns a dictionary of the frequency of each character in cryptedText


### replaceStr(string, toReplace, replace)

    Returns a string replacing the characters toReplace for replace in the var string. If you want 
    to save it in a variable do it in an aux variable. Notice that if you already know the ENTIRE 
    key use decrypt method
    
### findSequence(cryptedText, sequence)
    
    Returns a dictionary of frequency of given sequence in cryptedText. Notice that in THIS CASE the 
    character "@" replaces any character
        
### decrypt(cryptedText, dictionaryKey)
    
    Returns a string decrypted. In cryptedText use the text to be decrypted and in dictionaryKey use 
    a dictionary where the index is the crypted character and the value is the character in the alfabet. 
    Notice that to use it. make sure the dictionaryKey is complete with the ENTIRE key, if not use 
    replaceStr to do some tests.
    
    
        

