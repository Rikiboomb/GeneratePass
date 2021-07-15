import os
import random
import colorama
import sys
import time
import string
from time import sleep
from colorama import Fore, Back, Style
from termcolor import colored
colorama.init()
sleep(0.5) 
#time.sleep(1)
lownum = 7
highnum = 19

def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))

out_red("..................")
out_red("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡜⢣ ")
out_red("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠎⡴⢦⠱                     ╔════════════════════════════════════════════╗")
out_red("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⢎⣜⣉⣉⣧⡱⡄                                      About me ")
out_red("⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⢃⡞⠒⣒⣒⠒⢳⡘⣄                     》 Link:https://lolz.guru/members/310926/")
out_red("⠄⠄⠄⠄⠄⠄⠄⠄⣰⢡⣎⡩⠭⠤⠤⠭⢍⣱⡜⣆                     》 Nick:3Vill")
out_red("⠄⠄⠄⠄⠄⠄⠄⡴⢡⡯⠴⢒⣈⣩⣉⣑⡒⠠⣹⡌⢦                        .")
out_red("⠄⠄⠄⠄⠄⠄⡔⣡⣣⠔⡺⡋⡁⢀⡀⢈⠙⢟⠢⣝⣄⢢                    ( `•.¸    ")
out_red("⠄⠄⠄⠄⢀⡜⣰⡟⠁⢰⡓⢎⣀⣸⣿⣷⡱⢚⡆⠈⢻⣆⢣⡀                 ..`•.¸)    ")
out_red("⠄⠄⠄⢀⠎⡼⣇⠣⡀⠸⡄⢊⢿⣿⣿⡿⡑⢠⠇⢀⠜⣸⢧⠱⡀                 ..¸.•)       ")
out_red("⠄⠄⢠⢋⢼⡙⢌⠳⣍⠲⢽⣄⣁⠂⠐⣈⣠⡯⠔⣡⠞⡡⢊⣧⡙⡄                .(.•´        ")
out_red("⠄⣠⢃⣞⠣⡙⠦⡑⠦⣍⡒⠤⠬⠭⠭⠥⠤⢒⣩⠴⢊⠴⢋⠜⣳⡘⣄               c(¯¯) * ♪♫ ♥ Evening Tea Splash ♥")
out_red("⣰⣃⣛⣚⣓⣚⣓⣚⣓⣒⣛⣛⣓⣒⣒⣚⣛⣛⣒⣚⣓⣚⣓⣚⣒⣛⣘⣆           ''''''''''''")
print(Style.RESET_ALL)

PLAIN_TEXT = string.ascii_letters
CIPHER_TEXT = 'kWFUsDYeAxolSLTwChgNJtaMvQIzRZVrPEyfiKXGcdBunbqHjpOm'

CIPHER_TABLE = str.maketrans(PLAIN_TEXT, CIPHER_TEXT)
PLAIN_TABLE = str.maketrans(CIPHER_TEXT, PLAIN_TEXT)

chars = 'qwertyuiopasdfghjklzxcvbnm'
chars += chars.upper()
nums = str(1234567890)
chars += nums
special_chars = '!@#$%^&*()+-_'
chars += special_chars
sleep(0.5) 
#length = int(input("Введите число символов в password: "))
sleep(0.5) 

def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))
    
def convert():
    z=int(input('Введите номер задания: '))
    if z == 1:
        length = 0
        while 7 > length or 19 < length:
           try:
                password = 0
                length = int(input("Введите число символов в password (7 - 19) : "))
                print("")
           except ValueError:
                print("")
                print(colored("Ошибка: введены не правильные символы", 'red'))
                print("")     
        password = "".join(random.sample(chars, length))
        print(colored("Ваш сгенерированный password:", 'red'), password)
        my_file = open("passwords.txt", "a+")
        my_file.write(password)
        my_file.write(" ")
        my_file.close()
    elif z==2:
        try:
            file = open("passwords.txt", "r")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print('Not found')
    elif z==3:
        try:
            file = open("passwords.txt", "w")
            print("Passwords удалены")
            file.close()
        except FileNotFoundError:
            print('Файл отсутствует')
    elif z==4:
            print("В разработке")

    elif z==5:
        os.system('clear')
        os.abort()
        
print('-----Команды software...')
print('  1.-Генерация random passwords')
print('  2.-Просмотр сгенерированных passwords')
print('  3.-Очистка всех сгенерированных passwords')
print('  4.-Шифратор\Дешифратор текста')
print('  5.-Закрыть software')
print("")

convert()
while True:
    flag = input('Продолжить или выйти? [Y/N]: ')

    if flag == 'Y' or 'y':
        os.system('clear')
        out_red("..................")
        out_red("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡜⢣ ")
        out_red("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠎⡴⢦⠱                     ╔════════════════════════════════════════════╗")
        out_red("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⢎⣜⣉⣉⣧⡱⡄                                      About me ")
        out_red("⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⢃⡞⠒⣒⣒⠒⢳⡘⣄                     》 Link:https://lolz.guru/members/310926/")
        out_red("⠄⠄⠄⠄⠄⠄⠄⠄⣰⢡⣎⡩⠭⠤⠤⠭⢍⣱⡜⣆                     》 Nick:3Vill")
        out_red("⠄⠄⠄⠄⠄⠄⠄⡴⢡⡯⠴⢒⣈⣩⣉⣑⡒⠠⣹⡌⢦                        .")
        out_red("⠄⠄⠄⠄⠄⠄⡔⣡⣣⠔⡺⡋⡁⢀⡀⢈⠙⢟⠢⣝⣄⢢                    ( `•.¸    ")
        out_red("⠄⠄⠄⠄⢀⡜⣰⡟⠁⢰⡓⢎⣀⣸⣿⣷⡱⢚⡆⠈⢻⣆⢣⡀                 ..`•.¸)    ")
        out_red("⠄⠄⠄⢀⠎⡼⣇⠣⡀⠸⡄⢊⢿⣿⣿⡿⡑⢠⠇⢀⠜⣸⢧⠱⡀                 ..¸.•)       ")
        out_red("⠄⠄⢠⢋⢼⡙⢌⠳⣍⠲⢽⣄⣁⠂⠐⣈⣠⡯⠔⣡⠞⡡⢊⣧⡙⡄                .(.•´        ")
        out_red("⠄⣠⢃⣞⠣⡙⠦⡑⠦⣍⡒⠤⠬⠭⠭⠥⠤⢒⣩⠴⢊⠴⢋⠜⣳⡘⣄               c(¯¯) * ♪♫ ♥ Evening Tea Splash ♥")
        out_red("⣰⣃⣛⣚⣓⣚⣓⣚⣓⣒⣛⣛⣓⣒⣒⣚⣛⣛⣒⣚⣓⣚⣓⣚⣒⣛⣘⣆           ''''''''''''")
        print(Style.RESET_ALL)
        print('-----Команды software...')
        print('  1.-Генерация random passwords')
        print('  2.-Просмотр сгенерированных passwords')
        print('  3.-Очистка всех сгенерированных passwords')
        print('  4.-Шифратор\Дешифратор текста')
        print('  5.-Закрыть software')
        print("")
        convert()
    else:
        break
