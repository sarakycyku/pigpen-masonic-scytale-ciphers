import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ciphers.scytale import ScytaleCipher
from ciphers.pigpen import encrypt as pigpen_encrypt, decrypt as pigpen_decrypt
from ciphers.masonic import MasonicCipher
class Color:
    RED = '\033[91m'
    RESET = '\033[0m'


def valido_shkronja(text):
    for char in text:
        if not (char.isalpha() or char.isspace()):
            return False
    return True


def shfaq_menu():
    print("Zgjidh nje nga opsionet: \n")
    print("1. Pigpen")
    print("2. Scytale")
    print("3. Masonic")
    print("4. Krahaso")
    print("5. Dil")

def main():
    print("=" * 30)
    print("ALGORITMET KLASIKE")
    print("=" * 30)
    shfaq_menu()
    
    while True:
        choice = input("Zgjidh (1-5): ").strip()
        
        if choice == "5":
            print("Mirupafshim!")
            break
        
        if choice not in ["1", "2", "3", "4"]:
            print(f"{Color.RED}Zgjedhje e pavlefshme!{Color.RESET}")
            continue
            
        if choice == "1":
            print("\n PIGPEN CIPHER")
            print("1. Enkripto")
            print("2. Dekripto")
            
            option = input("Zgjidh opsionin: ").strip()
            
            if option == "1":
                text = input("Shkruaj plain text: ").strip()
                
                if not text:
                    print(f"{Color.RED}Mesazh i zbrazet!{Color.RESET}")
                    shfaq_menu()
                    continue
                
                if not valido_shkronja(text):
                    print(f"{Color.RED}Gabim: Lejohen vetem shkronja!{Color.RESET}\n")
                    shfaq_menu()
                    continue
                
                enc = pigpen_encrypt(text)
                print("Ciphertext:", enc)
                
            elif option == "2":
                text = input("Shkruaj tekstin e enkriptuar: ").strip()
                
                if not text:
                    print(f"{Color.RED}Mesazh i zbrazet!{Color.RESET}")
                    shfaq_menu()
                    continue
                
                dec = pigpen_decrypt(text)
                print("Plaintext:", dec)
                
            else:
                print(f"{Color.RED}Opsion i pavlefshem!{Color.RESET}")
            
            shfaq_menu()
                
        elif choice == "2":
            print("\n SCYTALE TRANSPOSITION ")
            print("1. Enkripto")
            print("2. Dekripto")
            
            option = input("Zgjidh opsionin: ").strip()
            text = input("Shkruaj tekstin: ").strip()
            
            if not text:
                print(f"{Color.RED}Mesazh i zbrazet!{Color.RESET}")
                shfaq_menu()
                continue
            
            try:
                rows = int(input("Numri i rreshtave: ").strip())
                if rows <= 0:
                    print(f"{Color.RED}Numri i rreshtave duhet te jete me i madh se 0!{Color.RESET}")
                    shfaq_menu()
                    continue
            except ValueError:
                print(f"{Color.RED}Gabim: Duhet te jepni nje numer te plote!{Color.RESET}")
                shfaq_menu()
                continue
            
            cipher = ScytaleCipher(rows=rows)
            
            if option == "1":
                enc = cipher.encrypt(text)
                print("Ciphertext:", enc)
            elif option == "2":
                dec = cipher.decrypt(text)
                print("Plaintext:", dec)
            else:
                print(f"{Color.RED}Opsion i pavlefshem!{Color.RESET}")
            
            shfaq_menu()
                
        elif choice == "3":
            print("\n MASONIC CIPHER ")
            print("1. Enkripto")
            print("2. Dekripto")
            
            option = input("Zgjidh opsionin: ").strip()
            
            if option == "1":
                text = input("Shkruaj plain text: ").strip()
                
                if not text:
                    print(f"{Color.RED}Mesazh i zbrazet!{Color.RESET}")
                    shfaq_menu()
                    continue
                
                if not valido_shkronja(text):
                    print(f"{Color.RED}Gabim: Lejohen vetem shkronja!{Color.RESET}\n")
                    shfaq_menu()
                    continue
                
                cipher = MasonicCipher()
                enc = cipher.encrypt(text)
                print("Ciphertext:", enc)
                
            elif option == "2":
                text = input("Shkruaj tekstin e enkriptuar: ").strip()
                
                if not text:
                    print(f"{Color.RED}Mesazh i zbrazet!{Color.RESET}")
                    shfaq_menu()
                    continue
                
                cipher = MasonicCipher()
                dec = cipher.decrypt(text)
                print("Plaintext:", dec)
                
            else:
                print(f"{Color.RED}Opsion i pavlefshem!{Color.RESET}")
            
            shfaq_menu()
                
        elif choice == "4":
            print("\n KRAHASO TE 3 ALGORITMET ")
            
            text = input("Shkruaj tekstin: ").strip()
            
            if not text:
                print(f"{Color.RED}Mesazh i zbrazet!{Color.RESET}")
                shfaq_menu()
                continue
            
            if not valido_shkronja(text):
                print(f"{Color.RED}Gabim: Lejohen vetem shkronja!{Color.RESET}\n")
                shfaq_menu()
                continue
            
            try:
                rows = int(input("Numri i rreshtave per Scytale: ").strip())
                if rows <= 0:
                    print(f"{Color.RED}Numri i rreshtave duhet te jete me i madh se 0!{Color.RESET}")
                    shfaq_menu()
                    continue
            except ValueError:
                print(f"{Color.RED}Gabim: Duhet te jepni nje numer te plote!{Color.RESET}")
                shfaq_menu()
                continue
            
            print("\nREZULTATET:")
            print("-" * 30)
            
            pigpen_result = pigpen_encrypt(text)
            print(f"PIGPEN:  {pigpen_result}")
            
            scytale_cipher = ScytaleCipher(rows=rows)
            scytale_result = scytale_cipher.encrypt(text)
            print(f"SCYTALE: {scytale_result}")
            
            masonic_cipher = MasonicCipher()
            masonic_result = masonic_cipher.encrypt(text)
            print(f"MASONIC: {masonic_result}")
            
            shfaq_menu()


if __name__ == "__main__":
    main()