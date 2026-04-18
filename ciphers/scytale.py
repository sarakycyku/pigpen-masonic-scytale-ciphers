class ScytaleCipher:
    def __init__(self, rows):
        self.rows = rows

    def encrypt(self, text):
        original_length = len(text.replace(" ", ""))
        
        text = text.replace(" ", "").upper()

        while len(text) % self.rows != 0:
            text += "X"

        cols = len(text) // self.rows

        result = ""

        for j in range(cols):
            for i in range(self.rows):
                index = i * cols + j
                result += text[index]

        return result, original_length

    def decrypt(self, text, original_length):
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
        
        result = result[:original_length]
        return result


# if __name__ == "__main__":
#     cipher = ScytaleCipher(rows=3)
    
#     tekst = "EXAMPLE"
    
#     enc, orig_len = cipher.encrypt(tekst)
#     dec = cipher.decrypt(enc, orig_len)
    
#     print("Teksti origjinal:", tekst)
#     print("Enkriptuar:", enc)
#     print("Dekriptuar:", dec)