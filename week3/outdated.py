def main():
#definir variables
    day = None
    month = None
    year = None
    userslist = ""
    meses = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}


    while True:
        usersdate = input("Enter date: ")

        try:
            if "/" in usersdate:                    #primer formato soportado MM/DD/AAAA
                userslist = usersdate.split("/")     #separación de la fecha por "/"
                month = int(userslist[0])
                day = int(userslist[1])
                year = int(userslist[2])

                if month >= 1 and month <= 12 and day >= 1 and day <= 31 and year > 0:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

        except ValueError:
            continue

        try:

            if "," in usersdate:               #segundo formato soportado: Mes Día, AAAA
                userslist = usersdate.replace(","," ").split() # reemplazar coma por espacio y separar los valores para la lista
                if len(userslist) < 3:
                    continue
                if userslist[0][0].isdigit():
                    continue
                month = meses[userslist[0]]
                day = int(userslist[1])
                year = int(userslist[2])
                if month >= 1 and month <= 12 and day >= 1 and day <= 31 and year > 0:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

        except ValueError:
            continue

        else:
            continue

main()




