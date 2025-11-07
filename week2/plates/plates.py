def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) <2 or len(s)>6: #si el largo es menor que 2 o mayor que 6 caracteres
        return False

    if not ((s[0]).isalpha() and s[1].isalpha()): #si NO son letras los dos primeros caracteres de la patente
        return False
    flag_num = False    #crear la variable como bandera booleana
    for i in s: #creamos loop para recorrer (s)
        if i.isdigit():    #preguntamos si i es un digito
            if flag_num==False:  #primer numero encontrado
                if i == "0":   # no puede ser cero
                    return False
            flag_num = True
        else:
            if flag_num:
                return True




main()
