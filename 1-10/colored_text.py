import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+'hi my name is sumin'+Fore.GREEN+Back.RED+' I am learning python')
print(Back.CYAN+'hi my name is minsu')
print()
print(Fore.BLUE+Style.DIM+'hi my name i sumin')
print(Fore.BLUE+Style.NORMAL+'hi my name i sumin')
print(Fore.BLUE+Style.BRIGHT+'hi my name i sumin')
print(Fore.BLUE+Style.RESET_ALL+'hi my name i sumin')
print()
print(Fore.RED+Back.GREEN+'hi my name is sumin')