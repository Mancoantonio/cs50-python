def main():
    felis={}

    felis={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    total=0

    while True:
        try:
            tab=input("Item: ").title()
            if tab not in felis:
                continue
            if tab in felis:
                total += felis[tab]
            print(f"Total: ${total:2f}")

        except EOFError:
            break

main()
