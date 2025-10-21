
def main():

## First we ask the user for the filename
    flnm = input(str("Enter filename and extension:\n"))
    flnm = flnm.lower().strip()
##then we check the extension by splicing from the last character
    if flnm[-4:] == ".jpg":
        print("image/jpeg")
    elif flnm[-4:] == ".gif":
        print("image/gif")
    elif flnm[-5:] == ".jpeg":
        print("image/jpeg")
    elif flnm[-4:] == ".png":
        print("image/png")
    elif flnm[-4:] == ".pdf":
        print("application/pdf")
    elif flnm[-4:] == ".txt":
        print("text/plain")
    elif flnm[-4:] == ".zip":
        print("application/zip")
    else:
        print("application/octet-stream")

main()
