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


def titull_program():
    print("=" * 30)
    print("ALGORITMET KLASIKE")
    print("=" * 30)


def titull_cipher(emri):
    print(f"\n {emri} ")
    print("1. Enkripto")
    print("2. Dekripto")


def error_print(msg):
    print(f"\033[91m{msg}\033[0m")


def print_rezultat(tipi, rezultati):
    print(f"{tipi}: {rezultati}")


def kontrollo_text(text):
    if not text:
        return False, "Mesazh i zbrazet!"
    return True, None


def opsion_i_vlefshem(option, opsionet=["1", "2"]):
    return option in opsionet


def numri_rreshtave():
    try:
        rows = int(input("Numri i rreshtave: ").strip())
        if rows <= 0:
            return None, "Numri i rreshtave duhet te jete me i madh se 0!"
        return rows, None
    except ValueError:
        return None, "Gabim: Duhet te jepni nje numer te plote!"


def numri_rreshtave_krahaso():
    try:
        rows = int(input("Numri i rreshtave per Scytale: ").strip())
        if rows <= 0:
            return None, "Numri i rreshtave duhet te jete me i madh se 0!"
        return rows, None
    except ValueError:
        return None, "Gabim: Duhet te jepni nje numer te plote!"