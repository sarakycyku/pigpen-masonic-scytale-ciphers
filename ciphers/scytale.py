class ScytaleCipher:
    def __init__(self, rows):
        self.rows = rows

    def encrypt(self, text):
        text = text.replace(" ", "").upper()

        while len(text) % self.rows != 0:
            text += "X"

        cols = len(text) // self.rows

        result = ""

        for j in range(cols):
            for i in range(self.rows):
                index = i * cols + j
                result += text[index]

        return result

    def decrypt(self, text):
        text = text.replace(" ", "").upper()
        
        cols = len(text) // self.rows
        
        matrix = [['' for _ in range(cols)] for _ in range(self.rows)]
        
        index = 0
        for j in range(cols):
            for i in range(self.rows):
                matrix[i][j] = text[index]
                index += 1
        
        result = ""
        for i in range(self.rows):
            for j in range(cols):
                result += matrix[i][j]
        
        return result


if __name__ == "__main__":
    cipher = ScytaleCipher(rows=3)
    
    tekst = "HELLO WORLD"
    
    enc = cipher.encrypt(tekst)
    dec = cipher.decrypt(enc)
    
    print("Teksti:", tekst)
    print("Enkriptuar:", enc)
    print("Dekriptuar:", dec)