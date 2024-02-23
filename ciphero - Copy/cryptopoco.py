'''
Michelle Luo
Master Project POCO (cryptopoco.py)
Spring to Winter of 2023
'''

class CryptoPoco:
    def __init__(self, accountID, username, password, id_user_specific_in_tableID, plainText, cipherText, encryption1,encryption2):
        self.accountID=accountID
        self.username=username
        self.password=password
        self.id_user_specific_in_tableID=id_user_specific_in_tableID
        self.plainText=plainText
        self.cipherText=cipherText
        self.encryption1=encryption1
        self.encryption2=encryption2
        
    def getAccountID(self):
        return self.accountID
    def setAccountID(self, accountID):
        this.accountID=accountID
    def getusername(self):
        return self.username
    def setusername(self, username):
        this.username=username
    def getpassword(self):
        return self.password
    def setpassword(self, password):
        self.password=password

    def getId_user_specific_in_tableID(self):
        return self.id_user_specific_in_tableID
    def setId_user_specific_in_tableID(self, id_user_specific_in_tableID):
        this.id_user_specific_in_tableID=id_user_specific_in_tableID
    def getPlainText(self):
        return self.plainText
    def setPlainText(self, plainText):
        this.plainText=plainText
    def getCipherText(self):
        return self.cipherText
    def setCipherText(self, cipherText):
        this.cipherText=cipherText
    def getEncryption1(self):
        return self.encryption1
    def setEncryption1(self, encryption1):
        this.encryption1=encryption1
    def getEncryption2(self):
        return self.encryption2
    def setEncryption2(self, encryption2):
        this.encryption2=encryption2
