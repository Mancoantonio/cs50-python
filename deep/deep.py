def main():
    resp = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    resp = resp.strip().lower()
    if resp == "42" or resp == "forty-two" or resp == "forty two":
        print("Yes")
    else:
        print("No")

main()
