'''Pigpen Cipher'''
'''Kthimi i shkronjave ne simbole'''
pigpen = {
    'A':'⟂','B':'⌐','C':'¬',
    'D':'└','E':'┴','F':'┘',
    'G':'├','H':'┼','I':'┤',
    'J':'⟂.','K':'⌐.','L':'¬.',
    'M':'└.','N':'┴.','O':'┘.',
    'P':'├.','Q':'┼.','R':'┤.',
    'S':'△','T':'▷','U':'▽',
    'V':'◁','W':'◇','X':'◆',
    'Y':'○','Z':'●'
}

'''Kthimi nga simboli në shkronjë '''
reverse = {}
for key, value in pigpen.items():
    reverse[value] = key


'''Enkriptimi'''
def encrypt(text):
    result = ""
    for char in text.upper():
        if char in pigpen:
            result += pigpen[char] + " "
        else:
            result += char + " "
    return result


''' Dekriptimi'''
def decrypt(text):
    result = ""
    for symbol in text.split():
        if symbol in reverse:
            result += reverse[symbol]
        else:
            result += symbol
    return result


'''Test i thjeshtë'''
text = input("Shkruaj tekst: ")

enc = encrypt(text)
print("Encrypted:", enc)

dec = decrypt(enc)
print("Decrypted:", dec)