'''
Michelle Luo
Cmdr. Schenk
AP Computer Science
Master Project Encryption methods (encryption.py)
Spring of 2023
'''

#imports
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b32encode
import random, math

#global public_key, private_key, n, prime

#Encryption class
class Encryption:
    def __init__(self):
        self.bs = AES.block_size
        self.key = ""#hashlib.sha256(key.encode()).digest()
    #function for encrypting with caesar cipher
    def caesar(self, plainText, key):
        cipherText=""
        # traverse text
        for i in range(len(plainText)):
            char = plainText[i]
            # Encrypt uppercase characters
            if (char.isupper()):
                cipherText+= chr((ord(char) + key-65) % 26 + 65)
            # Encrypt lowercase characters
            elif (char==" "):
                cipherText+=char
            else:
                cipherText += chr((ord(char) + key - 97) % 26 + 97)
        return cipherText
    
    #function for encrypting with book cipher
    def bookCipher(self, plainText, bookFileAddress):
        self.cipherTextList=[]
        self.linePosition=0
        self.wordPosition=0
        self.plainTextList=plainText.split(" ")
        for stringWord in self.plainTextList:
            self.finalPosition=self.bcFindWord(stringWord, bookFileAddress)
            if self.finalPosition=="NOT A WORD FOUND":
                self.cipherTextList.append(stringWord)
            else:
                self.cipherTextList.append(self.finalPosition)
        self.cipherText=" ".join(self.cipherTextList)
        return self.cipherText
    
    #used with book cipher to find word in text files
    def bcFindWord(self, stringWord, bookFileAddress):
        with open(bookFileAddress, encoding='utf-8') as myBookFile: 
            self.linePosition=0
            for bookLine in myBookFile: 
                self.linePosition+=1
                self.wordPosition=0
                wordList=bookLine.split(" ") 
                for bookWord in wordList: 
                    self.wordPosition+=1
                    if (bookWord==stringWord): 
                        self.finalPosition=str(self.linePosition)+"."+str(self.wordPosition) 
                        return self.finalPosition
                    else:
                        continue
        return "NOT A WORD FOUND"
    
    #function for encrypting with hex
    def hexString(self, plainText):
        cipherText=plainText.encode().hex()
        return cipherText
    
    #function for encrypting with base32
    def b32(self, plainText):
        cipherText=b32encode(plainText.encode())
        return cipherText

    def AESencrypt(self, raw, key):
        self.key=hashlib.sha256(key.encode()).digest()
        raw = self.AES_pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def AESdecrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.AES_unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def AES_pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def AES_unpad(s):
        return s[:-ord(s[len(s)-1:])]