def main():
#creamos una variable vacía
    CamelCase = input("Escribe un texto en CamelCase: ")
    snk_case = ("")
# recorremos el str
    for var in CamelCase:
        if var.isupper():
            snk_case += "_" + var.lower()
        else:
            snk_case += var
    print(snk_case)

main()
