from app import AnalisaSite

s = AnalisaSite


def menu():
    print("========================")
    print("     Analisa Site    ")
    print("========================")
    print("[1] - Imprime tag")
    print("[2] - Contador de tag")
    print("[0] - Sair")
    print(" ")


loop = True
texto = ""
while loop:
    menu()
    res = int(input("Opcao: "))

    if res == 1:
        s.listartags()
    elif res == 2:
        s.contartags()
    if res == 0:
        loop = False
