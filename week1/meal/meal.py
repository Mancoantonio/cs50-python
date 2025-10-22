## definimos la funcion principal
def main():
    ## we ask the user for the time of the day
    time = input("Enter the time:\n")
    if convert(time) >= 7.0 and convert(time) < 8.0:
        print("breakfast time")
    elif convert(time) >= 12.0 and convert(time) < 13.0:
        print("lunch time")
    elif convert(time) >= 18.0 and convert(time) < 19.0:
        print("dinner time")
    else:
        return

    ## then we convert the input to ints
    ## AND split into hours and minutes
def convert(time):

    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    minutes = minutes/60
    return hours + minutes

if __name__ == "__main__":
main()
