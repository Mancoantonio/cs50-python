import random

def main ():
    level = input(("Select level :"))  #número tope del juego (inclusive)
    level = int(level)
    generado = random.randint(1, level)
    while True:
        try:
            if level > 0:
                guess = input("Guess: ")
                guess = int(guess)
            else:
                continue
            if guess <= 0:
                continue
            elif guess < generado:
                print("Too small!")
                pass
            elif guess > generado:
                print("Too large!")
                pass
            else:
                print("Just right!")
                break
        except ValueError:
            pass
main()
