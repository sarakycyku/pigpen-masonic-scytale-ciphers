from ciphers.scytale import ScytaleCipher
def main():
    print("=" * 40)
    print("ALGORITME KLASIKE TE ENKRIPTIMIT")
    print("=" * 40)
    print("1. Pigpen")
    print("2. Scytale")
    print("3. Masonic")
    print("4. Dalje")
    
    while True:
        choice = input("\nZgjidh (1-4): ").strip()
        
        if choice == "4":
            print("Mirupafshim!")
            break
        
        if choice not in ["1", "2", "3"]:
            print("Zgjedhje e pavlefshme!")
            continue
        
        text = input("Mesazhi: ").strip()
        if not text:
            print("Zbrazet!")
            continue
        
       


if __name__ == "__main__":
    main()