class AddCipher():
    def __init__(self):
        self.plaintext=""
        self.ciphertext=""
        self.key=0
        self.name="Additive"
    def encrypt(self,plain,key):
        self.key=key
        self.ciphertext=""
        self.plaintext=plain
        self.plaintext=self.plaintext.split()
        self.temp=""
        for i in self.plaintext:
            self.temp=self.temp+i.upper()
        self.plaintext=self.temp
        for i in self.plaintext:
            self.chara=chr((((ord(i)-65)+self.key)%26)+65)
            self.ciphertext=self.ciphertext+self.chara
        return self.ciphertext
    def decrypt(self,cipher,key):
        self.key=key
        self.plaintext=""
        self.ciphertext=cipher.upper()
        for i in self.ciphertext:
            self.chara=chr((((ord(i)-65)-self.key)%26)+65)
            self.plaintext=self.plaintext+self.chara
        return self.plaintext
