import inflect
p = inflect.engine()
nombres = []

def main():

    while True:
        try:
            n = input()
            nombres.append(n)

        except EOFError:
            break
    print(f"Adieu, adieu, to {p.join(nombres)}")
main()