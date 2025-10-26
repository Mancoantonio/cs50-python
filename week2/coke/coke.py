def main():
    cokita = 50
    monea = 0

    while monea < cokita:
        monto = int(input("Ingrese moneda "))
        if monto == 5:
            monea = monea + 5
            print(f"Faltan: {cokita - monea}", end="\n")
        elif monto == 10:
            monea = monea + 10
            print(f"Faltan: {cokita - monea}", end="\n")
        elif monto == 25:
            monea = monea + 25
            print(f"Faltan: {cokita - monea}", end="\n")
        elif monea == cokita:
            break
        else:
            print(f"MONEDA FALSA !! LLAMAR A CARABINEROS !!", end="\n")
            break

    if (cokita - monea) <= 0:
        print(f"Change Owed: {monea - cokita}", end="\n")

main()
