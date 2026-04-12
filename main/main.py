from ciphers.scytale import ScytaleCipher

def main():
    print("=" * 40)
    print("CLASSIC ENCRYPTION ALGORITHMS")
    print("=" * 40)
    print("1. Pigpen")
    print("2. Scytale")
    print("3. Masonic")
    print("4. Exit")
    
    while True:
        choice = input("\nChoose (1-4): ").strip()
        
        if choice == "4":
            print("Goodbye!")
            break
        
        if choice not in ["1", "2", "3"]:
            print("Invalid choice!")
            continue
        
        if choice == "2":
            print("SCYTALE TRANSPOSITION CIPHER")
            print("1. Encrypt")
            print("2. Decrypt")
            
            option = input("Select option: ").strip()
            text = input("Enter the text:").strip()
            
            if not text:
                print("Empty message!")
                continue
            
            rows = int(input("Number of rows: ").strip())
            cipher = ScytaleCipher(rows=rows)
            
            if option == "1":
                enc = cipher.encrypt(text)
                print("Encrypted:", enc)
                
            elif option == "2":
                dec = cipher.decrypt(text)
                print("Decrypted:", dec)
                
            else:
                print("Invalid option!")

if __name__ == "__main__":
    main()