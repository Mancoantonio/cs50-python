## defining the main function
def main():
    ops = input(str("Ingrese operación:\n"))
    opera = ops.split()
    primer_num = int(opera[0])
    operador = (opera[1])
    segundo_num = int(opera[2])
    if operador == "+":
        result = primer_num + segundo_num
    elif operador == "-":
        result = primer_num - segundo_num
    elif operador == "*":
        result = primer_num * segundo_num
    elif operador == "/":
        result = primer_num / segundo_num
    else :
        print("Operador no válido")
        return

    print(f"Result is: {result:.1f}")

main()
