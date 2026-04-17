from ciphers.scytale import ScytaleCipher
from ciphers.pigpen import encrypt as pigpen_encrypt, decrypt as pigpen_decrypt
from ciphers.masonic import MasonicCipher


def valido_shkronja(text):
    # validimi qe teksti ne dy algoritmet me qene vetem shkronja
    for char in text:
        if not (char.isalpha() or char.isspace()):
            return False
    return True


def main():
    print("=" * 40)
    print("CLASSICAL ENCRYPTION ALGORITHMS")
    print("=" * 40)
    print("1. Pigpen")
    print("2. Scytale")
    print("3. Masonic")
    print("4. Krahaso")
    print("5. Dil")
    
    while True:
        choice = input("\nZgjidh (1-5): ").strip()
        
        if choice == "5":
            print("Mirupafshim!")
            break
        
        if choice not in ["1", "2", "3", "4"]:
            print("Zgjedhje e pavlefshme!")
            continue
            
        if choice == "1":
            print("\nSHIFRA PIGPEN")
            print("1. Enkripto")
            print("2. Dekripto")
            
            option = input("Zgjidh opsionin: ").strip()
            text = input("Shkruaj tekstin: ").strip()
            
            if not text:
                print("Mesazh i zbrazet!")
                continue
            
            if not valido_shkronja(text):
                print("Gabim: Lejohen vetem shkronja!")
                continue
            
            if option == "1":
                enc = pigpen_encrypt(text)
                print("Enkriptuar:", enc)
                
            elif option == "2":
                dec = pigpen_decrypt(text)
                print("Dekriptuar:", dec)
                
            else:
                print("Opsion i pavlefshem!")
                
        elif choice == "2":
            print("\n SCYTALE TRANSPOSITION")
            print("1. Enkripto")
            print("2. Dekripto")
            
            option = input("Zgjidh opsionin: ").strip()
            text = input("Shkruaj tekstin: ").strip()
            
            if not text:
                print("Mesazh i zbrazet!")
                continue
            
            try:
                rows = int(input("Numri i rreshtave: ").strip())
                if rows <= 0:
                    print("Numri i rreshtave duhet te jete me i madh se 0!")
                    continue
            except ValueError:
                print("Gabim: Duhet te jepni nje numer te plote!")
                continue
            
            cipher = ScytaleCipher(rows=rows)
            
            if option == "1":
                enc = cipher.encrypt(text)
                print("Enkriptuar:", enc)
                
            elif option == "2":
                dec = cipher.decrypt(text)
                print("Dekriptuar:", dec)
                
            else:
                print("Opsion i pavlefshem!")
                
        elif choice == "3":
            print("\n MASONIC CIPHER")
            print("1. Enkripto")
            print("2. Dekripto")
            
            option = input("Zgjidh opsionin: ").strip()
            text = input("Shkruaj tekstin: ").strip()
            
            if not text:
                print("Mesazh i zbrazet!")
                continue
            
            if not valido_shkronja(text):
                print("Gabim: Lejohen vetem shkronja!")
                continue
            
            cipher = MasonicCipher()
            
            if option == "1":
                enc = cipher.encrypt(text)
                print("Enkriptuar:", enc)
                
            elif option == "2":
                dec = cipher.decrypt(text)
                print("Dekriptuar:", dec)
                
            else:
                print("Opsion i pavlefshem!")
                
        elif choice == "4":
            print("\n" + "=" * 40)
            print("KRAHASO - Te 3 ALGORITMET")
            print("=" * 40)
            
            text = input("Shkruaj tekstin: ").strip()
            
            if not text:
                print("Mesazh i zbrazet!")
                continue
            
            if not valido_shkronja(text):
                print("Gabim: Lejohen vetem shkronja!")
                continue
            
            try:
                rows = int(input("Numri i rreshtave per Scytale: ").strip())
                if rows <= 0:
                    print("Numri i rreshtave duhet te jete me i madh se 0!")
                    continue
            except ValueError:
                print("Gabim: Duhet te jepni nje numer te plote!")
                continue
            
            print("\n" + "-" * 40)
            print("REZULTATET:")
            print("-" * 40)
            
            pigpen_result = pigpen_encrypt(text)
            print(f"1. PIGPEN:    {pigpen_result}")
            
            scytale_cipher = ScytaleCipher(rows=rows)
            scytale_result = scytale_cipher.encrypt(text)
            print(f"2. SCYTALE:   {scytale_result}")
            
            masonic_cipher = MasonicCipher()
            masonic_result = masonic_cipher.encrypt(text)
            print(f"3. MASONIC:   {masonic_result}")
            
            print("-" * 40)


if __name__ == "__main__":
    main()