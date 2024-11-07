# discord : ayamessh
# github  : https://github.com/ayamessh/connection-checker
import requests 
import os 
from colorama import Fore 

r = Fore.RED 
g = Fore.GREEN 
b = Fore.BLUE 

os.system('cls') 

req = requests.get(url="https://google.com") 


if req.status_code == 200:
    print(f"{g}You are connected to internet\n\n") 
else:
    print(f'{r}No connection\n\n')

input(f'{b}Press enter to exit') 