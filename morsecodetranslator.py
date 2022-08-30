#https://morsecode.world/international/morse2.html

#dict
MORSE_CODE_DICT={
  'A':'.-',
  'B':'-...',
  'C':'-.-.',
  'D':'-..',
  'E':'.',
  'F':'..-.',
  'G':'--.',
  'H':'....',
  'I':'..',
  'J':'.---',
  'K':'-.-',
  'L':'.-..',
  'M':'--',
  'N':'-.',
  'O':'---',
  'P':'.--.',
  'Q':'--.-',
  'R':'.-.',
  'S':'...',
  'T':'-',
  'U':'..-',
  'V':'...-',
  'W':'.--',
  'X':'-..-',
  'Y':'-.--',
  'Z':'--..',
  '1':'.----',
  '2':'..---',
  '3':'...--',
  '4':'....-',
  '5':'.....',
  '6':'-....',
  '7':'--...',
  '8':'---..',
  '9':'----.',
  '0':'-----',
  ',':'--..--',
  '.':'.-.-.-',
  '?':'..--..',
  '/':'-..-.',
  '-':'-....-',
  '(':'-.--.',
  ')':'-.--.-',
  '!':'-.-.--',
  '@':'.--.-.',
  '&':'.-...',
  '?':'..--..'
  }


#enc 
def encrypt(pt):
    ct = ''
    for letter in pt:
        if(letter != ' '):
            #uses dictionary
            ct += MORSE_CODE_DICT[letter] + ' '
        else:
            #1 space indicates different characters(letters), 2 indicates different words
            ct += ' '
    return ct


#dec
def decrypt(message):
    message += ' ' #extra space added at the end to access the last morse code
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0 #counter to keep track of spaces
            citext += letter #storing morse code of a single character
        else:
            i += 1
            #if i = 1 that indicates a new character
            #if i = 2 that indicates a new word
            if i == 2 :
                decipher += ' ' #adding space to separate words
            else:
                #accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher



#Hard-coded driver()
def main():
    choice=int(input("Greetings SPY69420; \n\n1-> Encrypt from ENG to Morse. \n2-> Decrypt from Morse to ENG: "))
    if(choice==1):
        plaintext=input("\n\nSplendid. \nEnter message to be encrypted here: ")
        ciphertext=encrypt(plaintext.upper())
        print(ciphertext)
    elif(choice==2):
        ciphertext=input("\n\nSplendid. \nEnter message to be descrypted here: ")
        plaintext=decrypt(ciphertext)
        print(plaintext)
    else:
        print("\n\nDon't become a saucy boy, agent.")
        

if __name__ == '__main__':
    main()
#a dedicated main() can be useful if running as a script. doesn't hurt to include it
