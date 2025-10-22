## definimos la funcion principal
def main():
    ## we ask the user for the time of the day
    time = input("Enter the time:\n")
    if convert(time) >= 7.0 and convert(time) < 8.0:
        print("Breakfast time")
    elif convert(time) >= 12.0 and covert(time) < 13.0
        print("Lunch time")
    elif convert(time) >= 18.0 and convert(time) < 19.0

    ## then we convert the input to ints
    ## AND split into hours and minutes
def convert(time):

    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    minutes = minutes/60
    return hours + minutes

main()
