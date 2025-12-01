import sys
import random
from pyfiglet import Figlet


figlet = Figlet()
fuente = figlet.getFonts()

if len(sys.argv) == 2:
    sys.exit(1)


if len(sys.argv) == 3 and sys.argv[1] not in ["-f", "--font"]:
    sys.exit(1)


if len(sys.argv) == 3 and sys.argv[2] not in fuente:
    sys.exit(1)

if len(sys.argv) == 1:
        font_elegida = random.choice(fuente)
        figlet.setFont(font=font_elegida)
        texto = input("Input: ")
        print(figlet.renderText(texto))


elif len(sys.argv) == 3:
        fuente_elegida = sys.argv[2]
        figlet.setFont(font=fuente_elegida)
        texto = input("Input: ")
        print(figlet.renderText(texto))



