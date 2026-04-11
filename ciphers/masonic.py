"""
Masonic Cipher -  Enkriptimi
"""

class MasonicCipher:
    def __init__(self):
        self.encrypt_map = {}
        self._build_maps()

    def _build_maps(self):
        # Grid 1: A-I
        g1_symbols = ['┌', '┬', '┐', '├', '┼', '┤', '└', '┴', '┘']
        g1_letters = list("ABCDEFGHI")

        # Grid 2: J-R me pika
        g2_symbols = ['┌•', '┬•', '┐•', '├•', '┼•', '┤•', '└•', '┴•', '┘•']
        g2_letters = list("JKLMNOPQR")

        # Grid 3: S-Z
        g3_symbols = ['╱', '╲', '╳', '◣', '◢', '◤', '◥', '◆']
        g3_letters = list("STUVWXYZ")

        for l, s in zip(g1_letters, g1_symbols):
            self.encrypt_map[l] = s
        for l, s in zip(g2_letters, g2_symbols):
            self.encrypt_map[l] = s
        for l, s in zip(g3_letters, g3_symbols):
            self.encrypt_map[l] = s

        self.encrypt_map[' '] = ' '

    # Enkriptimi
    def encrypt(self, text):
        return ' '.join(self.encrypt_map.get(ch.upper(), ch) for ch in text)


# Testimi 
if __name__ == "__main__":
    cipher = MasonicCipher()

    tekst = "programim ne python"

    enc = cipher.encrypt(tekst)

    print("Teksti:", tekst)
    print("Enkriptuar:", enc)