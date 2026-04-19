import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ciphers.scytale import ScytaleCipher
from ciphers.pigpen import encrypt as pigpen_encrypt, decrypt as pigpen_decrypt
from ciphers.masonic import MasonicCipher
from fn import (valido_shkronja, shfaq_menu, titull_program, titull_cipher, error_print, print_rezultat, kontrollo_text, opsion_i_vlefshem,numri_rreshtave, numri_rreshtave_krahaso)

class Color:
    RED = '\033[91m'
    RESET = '\033[0m'


def main():
    titull_program()
    shfaq_menu()
    
    while True:
        choice = input("Zgjidh (1-5): ").strip()
        
        if choice == "5":
            print("Mirupafshim!")
            break
        
        if choice not in ["1", "2", "3", "4"]:
            error_print("Zgjedhje e pavlefshme!")
            continue
            
        if choice == "1":
            titull_cipher("PIGPEN CIPHER")
            
            option = input("Zgjidh opsionin: ").strip()
            
            if not opsion_i_vlefshem(option):
                error_print("Opsion i pavlefshem!")
                shfaq_menu()
                continue
            
            if option == "1":
                text = input("Shkruaj plain text: ").strip()
                
                vlefsh, msg = kontrollo_text(text)
                if not vlefsh:
                    error_print(msg)
                    shfaq_menu()
                    continue
                
                if not valido_shkronja(text):
                    error_print("Gabim: Lejohen vetem shkronja!")
                    shfaq_menu()
                    continue
                
                enc = pigpen_encrypt(text)
                print_rezultat("Ciphertext", enc)
                
            elif option == "2":
                text = input("Shkruaj tekstin e enkriptuar: ").strip()
                
                vlefsh, msg = kontrollo_text(text)
                if not vlefsh:
                    error_print(msg)
                    shfaq_menu()
                    continue
                
                dec = pigpen_decrypt(text)
                print_rezultat("Plaintext", dec)
            
            shfaq_menu()
                
        elif choice == "2":
            titull_cipher("SCYTALE TRANSPOSITION")
            
            option = input("Zgjidh opsionin: ").strip()
            
            if not opsion_i_vlefshem(option):
                error_print("Opsion i pavlefshem!")
                shfaq_menu()
                continue
            
            text = input("Shkruaj tekstin: ").strip()
            
            vlefsh, msg = kontrollo_text(text)
            if not vlefsh:
                error_print(msg)
                shfaq_menu()
                continue
            
            rows, error = numri_rreshtave()
            if error:
                error_print(error)
                shfaq_menu()
                continue
            
            cipher = ScytaleCipher(rows=rows)
            
            if option == "1":
                enc = cipher.encrypt(text)
                print_rezultat("Ciphertext", enc)
            elif option == "2":
                dec = cipher.decrypt(text)
                print_rezultat("Plaintext", dec)
            
            shfaq_menu()
                
        elif choice == "3":
            titull_cipher("MASONIC CIPHER")
            
            option = input("Zgjidh opsionin: ").strip()
            
            if not opsion_i_vlefshem(option):
                error_print("Opsion i pavlefshem!")
                shfaq_menu()
                continue
            
            if option == "1":
                text = input("Shkruaj plain text: ").strip()
                
                vlefsh, msg = kontrollo_text(text)
                if not vlefsh:
                    error_print(msg)
                    shfaq_menu()
                    continue
                
                if not valido_shkronja(text):
                    error_print("Gabim: Lejohen vetem shkronja!")
                    shfaq_menu()
                    continue
                
                cipher = MasonicCipher()
                enc = cipher.encrypt(text)
                print_rezultat("Ciphertext", enc)
                
            elif option == "2":
                text = input("Shkruaj tekstin e enkriptuar: ").strip()
                
                vlefsh, msg = kontrollo_text(text)
                if not vlefsh:
                    error_print(msg)
                    shfaq_menu()
                    continue
                
                cipher = MasonicCipher()
                dec = cipher.decrypt(text)
                print_rezultat("Plaintext", dec)
            
            shfaq_menu()
                
        elif choice == "4":
            print("\n KRAHASO TE 3 ALGORITMET ")
            
            text = input("Shkruaj tekstin: ").strip()
            
            vlefsh, msg = kontrollo_text(text)
            if not vlefsh:
                error_print(msg)
                shfaq_menu()
                continue
            
            if not valido_shkronja(text):
                error_print("Gabim: Lejohen vetem shkronja!")
                shfaq_menu()
                continue
            
            rows, error = numri_rreshtave_krahaso()
            if error:
                error_print(error)
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