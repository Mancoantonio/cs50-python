def main():
    cokita = 50
    monea = 0
    monto = int(input("Inserte una moneda: "))
    if monto == 5:
        monea = monea + 5
    if monto == 10:
        monea = monea + 10
    if monto == 25:
        monea = monea + 25
    while monea < 50:
        print("falta plata po ctm")
        break
main()
