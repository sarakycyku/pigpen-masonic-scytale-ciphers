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
# if __name__ == "__main__":
#     cipher = ScytaleCipher(3)
#     print(cipher.encrypt("HELLO WORLD"))