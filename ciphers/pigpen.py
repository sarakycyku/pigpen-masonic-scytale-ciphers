'''Pigpen Cipher'''
pigpen = {
    'A':'⟂','B':'⌐','C':'¬',
    'D':'└','E':'┴','F':'┘',
    'G':'├','H':'┼','I':'┤',
    'J':'◰','K':'◱','L':'◲',
    'M':'◳','N':'◴','O':'◵',
    'P':'◶','Q':'◷','R':'◸',
    'S':'△','T':'▷','U':'▽',
    'V':'◁','W':'◇','X':'◆',
    'Y':'○','Z':'●'
}

reverse = {v: k for k, v in pigpen.items()}


def encrypt(text):
    result = ""
    for char in text.upper():
        if char in pigpen:
            result += pigpen[char] + " "
        else:
            result += char + " "
    return result.strip()


def decrypt(text):
    result = ""
    for symbol in text.split():
        if symbol in reverse:
            result += reverse[symbol]
        else:
            result += symbol
    return result


print("Zgjedh opsionin:")
print("1 - Encrypt")
print("2 - Decrypt")

choice = input("Zgjedh (1/2): ")

if choice == "1":
    text = input("Shkruaj tekstin për enkriptim: ")
    print("Encrypted:", encrypt(text))

elif choice == "2":
    text = input("Shkruaj tekstin e enkriptuar: ")
    print("Decrypted:", decrypt(text))

else:
    print("Opsion i pavlefshëm!")