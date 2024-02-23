'''
Book Cipher Encryption
AP Computer Science Principles Submission
Python, the Language
'''


#import modules "sys" and "os"
import sys, os


#The copy of the Great Gatsby used in this program is located here
#https://www.gutenberg.org/cache/epub/64317/pg64317.txt


#definition of the main function
def main():
    #call upon the function "welcome" and store its returned value in encryptOrDecrypt
    encryptOrDecrypt=welcome()
    #call upon the function "userInput", passing the parameter "encryptOrDecrypt", storing its returned list in myWordList
    myWordList=userInput(encryptOrDecrypt)
    #if the variable "encryptOrDecrypt" is storing a value of "Encryption"...
    if (encryptOrDecrypt=="Encryption"):
        #...call upon the function "encryptTheList", passing a parameter of list "myWordList"
        encryptTheList(myWordList)
    #else if the variable "encryptOrDecrypt" is storing a value of "Decryption"...
    elif (encryptOrDecrypt=="Decryption"):
        #... call upon the function "decryptTheList, passing a parameter of list "myWordList"
        decryptTheList(myWordList)
    #in any other situations where the previous conditionals have not been met...
    else:
        #...print an error message
        print("error has occured. Please try again.")
    #thank you and credits
    print("\nThank you for using "+'\033[1;32m'+"Book Cipher."+'\033[1;m'+"\nIf you would like to access the Great Gatsby version used in this program, please go here "+'\033[1;32m'+"https://www.gutenberg.org/cache/epub/64317/pg64317.txt"+'\033[1;m')
    #exit the program.
    sys.exit(0)


#welcome Screen function
def welcome():
    #clear the screen
    os.system('clear')
    #Welcomes the User and explains the Book Cipher to the User
    print("Welcome to the "+'\033[1;32m'+"Book Cipher."+'\033[1;m'+"\nThe book we will be using to"+'\033[1;32m'+" encrypt"+'\033[1;m'+" (words --> secret code) and "+'\033[1;32m'+"decrypt"+'\033[1;m'+" (secret code --> words)\nis "+'\033[1;32m'+"The Great Gatsby by F. Scott Fitzgerald "+'\033[1;m'+"(Sourced from gutenberg.org).\n\nThe encrypted code might look like this: "+'\033[1;32m'+ "456.7"+'\033[1;m'+"\n456 represents the "+'\033[1;32m'+"456th line "+'\033[1;m'+"of the Great Gatsby\n7 represents the "+'\033[1;32m'+"7th word"+'\033[1;m'+" of that line\nso 456.7 means the 7th word of the 456th line of the Great Gatsby which is 'Can't' \n"+'\033[1;32m'+"Not all words "+'\033[1;m'+"will be encrypted; there are a limited number of words in the book\n")
    #declare empty variable "userFinalChoice"
    userFinalChoice=""
    #while loop- it keeps on iterating as long as variable "userFinalChoice" is not set to "Encryption" or "Decryption"
    while ((userFinalChoice!="Encryption") or (userFinalChoice!="Decryption")):
        #Asks user for an input using the "input()" function, the result is stored in the variable "userInput"
        userInput=input('\033[1;34m'+"Would you like to encrypt or decrypt a string today? "+'\033[1;m')
        #if the userInput dictates that the User would like to encrypt...
        if ((userInput=="e")or(userInput=="encrypt")or (userInput=="E") or(userInput=="Encrypt")):
            #... set the variable "userFinalChoice" to "Encryption"
            userFinalChoice="Encryption"
            #break out of the loop
            break
        #if the userInput dictates that the User would like to decrypt...
        elif ((userInput=="d")or (userInput=='decrypt')or (userInput=='D') or (userInput=='Decrypt')):
            #... set the variable "userFinalChoice" to "Decryption"
            userFinalChoice="Decryption"
            #break out of the loop
            break
        #if the userInput does not meet any of the previous conditions...
        else:
            #... print an error
            print("error! please input a valid answer: encrypt or decrypt\n")
            #continue the loop
            continue
    #at the end of the loop, return a value with variable "userFinalChoice"
    return userFinalChoice


#function named "encryptTheList" with a parameter of "myPlainTextWordList", to encrypt the list that is given as the parameter
def encryptTheList(myPlainTextWordList):
    #Establishes an empty list "myEncryptedWordList"
    myEncryptedWordList=[]
    #for each element "plainTextWord" in the list "myPlainTextWordList"...
    for plainTextWord in myPlainTextWordList:
        #...call upon the function "findWord" with parameters "plainTextWord" and "encrypt", storing the result in the variable "encryptedWord".
        # The plainTextWord has now been encrypted, if the word is available in the Great Gatsby Book's text file.
        encryptedWord=findWord(plainTextWord, "encrypt")
        #add the encrypted word "encryptedWord" to the end of list "myEncryptedWordList"
        myEncryptedWordList.append(encryptedWord)
    #print the final encrypted string:
    print("\nHere is your final encrypted string: ")
    #print out each element in the list "myEncryptedWordList" seperated by a space, replicating the original message sent.
    print(*myEncryptedWordList, sep = " ")


#function named "decryptTheList" with a parameter of "myEncodedWordList", to decrypt the list that is given as the parameter
def decryptTheList(myEncodedWordList):
    #establishes empty list "myDecryptedWordList"
    myDecryptedWordList=[]
    #for each element "encryptedWord" in the list "myEncodedWordList"...
    for encryptedWord in myEncodedWordList:
        #call upon the function "findWord" with parameters "encryptedWord" and "decrypt", storing the results in variable "decryptedWord"
        # The encoded Book Cipher word has now been decrypted, if the word was in encoded Book Cipher form.
        decryptedWord=findWord(encryptedWord, "decrypt")
        #add the decryptedWord to the end of list "myDecryptedWordList"
        myDecryptedWordList.append(decryptedWord)
    #print the final decrypted string:
    print("\nHere is your final decrypted string: ")
    #print out each element in the list "myDecryptedWordList" seperated by a space, replicating the original message sent.
    print(*myDecryptedWordList, sep = " ")


#function "userInput" has a parameter of "encryptOrDecrypt", to denote whether or not the program should prompt the user for a string that will be encrypted or decrypted
def userInput(encryptOrDecrypt):
    #if the variable "encryptOrDecrypt" stores a value of "Encryption"
    if (encryptOrDecrypt=="Encryption"):
    #Prompts user for the input of a string, the string input is stored in variable "plainTextString"
        plainTextString=input('\033[1;34m'+"\nPlease enter the string you want encrypted: "+'\033[1;m')
        #Splits apart the string "plainTextString" into a list "myPlainTextWordList"
        myPlainTextWordList=plainTextString.split(" ")
        #return the list "myPlainTextWordList"
        return myPlainTextWordList
    #if the variable "encryptOrDecrypt" stores a value of "Decryption"
    elif (encryptOrDecrypt=="Decryption"):
        #Prompts user for the input of a string, the string input is stored in variable "encryptedString"
        encryptedString=input('\033[1;34m'+"\nPlease enter the string you want decrypted: "+'\033[1;m')
        #split apart the string "encryptedString" into a list "myEncryptedWordList"
        myEncryptedWordList=encryptedString.split(" ")
        #return the list "myEncryptedWordList"
        return myEncryptedWordList


#function "findWord" with parameter "stringWord"
def findWord(stringWord, encryptOrDecrypt):
    #set variable "LinePosition" to 0
    linePosition=0
    #FILTERS FOR DECRYPT. if variable "encryptOrDecrypt" is set to "decrypt"...
    if (encryptOrDecrypt=="decrypt"):
        #empty list "myPositionList"
        myPositionList=[]
        #split the encrypted word (for example, '456.7') into two strings ('456.7'-->'456' and '7') and store the value(s) into list "myPositionList"
        myPositionList=stringWord.split(".")
        #if the length of "myPositionList" is equal to 1, that means that the word is already in plain text, so there's no need to decrypt further.
        if (len(myPositionList)==1):
            #return the variable "stringWord" because it is in its plain text form already.
            return stringWord
    #opens file "Great_Gatsby.txt" with "Great_Gatsby.txt" being now referred to as "myBookFile"
    with open("Great_Gatsby.txt" , encoding='utf-8') as myBookFile:
        #iterate through every line "bookLine" in the file "myBookFile"
        for bookLine in myBookFile:
            #increase the variable "LinePosition" by +1 everytime the loop is iterated
            linePosition+=1
            #set the variable "WordPosition" to 0 everytime the loop is iterated. This is meant to reset the variable "wordPosition" so that we can now count a new line of words.
            wordPosition=0
            #splits each line into words. These words are now stored in the list "WordList"
            wordList=bookLine.split(" ")
            #iterate through every word "bookWords" in the list "wordList"
            for bookWord in wordList:
                #increase variable "WordPosition" by +1 everytime the loop is iterated
                wordPosition+=1
                #if the word in the file "bookWord" matches the word the program wants to encrypt...
                if (bookWord==stringWord):
                    #...store the final position "finalPosition" of the word using "LinePosition" and "WordPosition"
                    finalPosition=str(linePosition)+"."+str(wordPosition)
                    #then return the "finalPosition", completing its role as a function.
                    return finalPosition
                #if the program is meant to to decrypt...
                elif (encryptOrDecrypt=="decrypt"):
                    #... and if the numbers in the encrypted code match up with the line number and word number...
                    if (linePosition==int(myPositionList[0]) and wordPosition==int(myPositionList[1])):
                        #... then return the variable "bookWord", as it is the word that the numbers in the encrypted code refer to.
                        return bookWord
                #if the word in the file "bookWord" does *NOT* match the word the program wants to encrypt,
                else:
                    #continue the loops
                    continue
    #at the end of all the iterating loops, and no matching word is found, return the unencrypted word. This is the problem with book ciphers. Books don't contain ALL the words you need sometimes.
    return stringWord


#run the main function
if(__name__=="__main__"):
    #run main function
    main()