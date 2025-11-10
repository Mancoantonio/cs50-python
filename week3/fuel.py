def main():

    while True:
        frac_input=input("Fraction: ").split("/") #separador para el "/" de la fracción, nos queda una lista

        try:
            dividendo=int(frac_input[0])
            divisor=int(frac_input[1])
            frac_res=(dividendo/divisor)*100
            if dividendo > divisor or dividendo < 0 or divisor < 0:
                continue
            frac_fin=round(frac_res)

        except ZeroDivisionError:
            continue
        except ValueError:
            continue

        if frac_res <= 1:
            print("E")
        elif frac_res >= 99:
            print("F")
        else:
            print(f"{frac_fin}%")
        break
main()

