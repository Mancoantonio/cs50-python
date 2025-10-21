## defining user's response
greet = input("Hello, sir\n")
greet = greet.strip().lower()
## defining main funcion
def main():
    if greet.startswith("hello"):
        print("$0")
    elif greet[0] == "h":
        print("$20")
    else:
        print("$100")

main()


