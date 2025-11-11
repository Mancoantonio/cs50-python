def main():
    compras={}
 
    while True:
        try:
            item = input("")
            item = item.upper()

            if item not in compras:
                compras[item] = 1 
            else:
                item in compras
                compras[item] += 1


        except EOFError:
            break

    for clave, valor in compras.items():
        print(f"{valor} {item.upper()}")

main()
