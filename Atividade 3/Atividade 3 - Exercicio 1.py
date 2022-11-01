
turno = (input("Digite M para manha V para boa tarde N para noite:")).upper()


match(turno):
    case("M"):
        print("Bom Dia!")

    case("V"):
        print("Boa Tarde!")

    case("N"):
        print("Boa Noite!")
    case _:
        print("Valor inválido!")

