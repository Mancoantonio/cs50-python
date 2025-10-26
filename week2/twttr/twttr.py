def main():
    word = input("Ingrese palabra: ")
    neword = ("")
    # DEFINIMOS LAS VOCALES
    vowels = "aeiouAEIOU"
    ## recorremos la palabra
    for i in word:
        if i in vowels:
            continue
# añadimos i si es que NO es vocal
        neword += i

#imprimimos la nueva palabra
    print(neword)
main()




