import random

def main():
    nivel = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(nivel)
        y = generate_integer(nivel)
        correct_answer = x + y
        tries = 0

        while tries < 3:
            try:
                user_input = int(input(f"{x} + {y} = "))
                if user_input == correct_answer:
                    score = score + 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            tries = tries + 1

        if tries == 3:
            print(correct_answer)

    print(f"Score: {score}/10")

def get_level():
        while True:
            try:
                nivel = int(input("Level(1, 2 or 3): "))
                if nivel == 1 or nivel == 2 or nivel == 3:
                    return nivel

            except ValueError:
                pass

def generate_integer(nivel):
    if nivel != 1 and nivel !=2 and nivel != 3:
            raise ValueError
        
    if nivel == 1:
            return random.randint(0,9)
    elif nivel == 2:
            return random.randint(10,99)
    elif nivel == 3:
            return random.randint(100,999)
        
if __name__ == "__main__":
    main()