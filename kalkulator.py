import colorama
from colorama import init
from colorama import Fore, Back, Style

init()

print( Back.BLUE )
print( Fore.BLACK )


action = input("Привет! Это дебильный калькулятор, что будем делать (+ -): ")

print( Back.MAGENTA )

num1 = float( input("Ок, с действием разобрались теперь укажи число: ") )

print( Back.RED )

num2 = float( input("Ок, а теперь укажи второе число: ") )

if action == "+":
    result = num1 + num2
    
    print( Back.GREEN )

    print("Чтож, калькулятор посчитал что " + str(num1) + action + str(num2) + " будет " + str(result) )

elif action == "-":
    
    print( Back.GREEN )
    
    result = num1 - num2
    print("Чтож, калькулятор посчитал что " + str(num1) + action + str(num2) + " будет " + str(result) )

else:
   print("К сожелению, но Дебильному калькулятору неудалось посчитать т.к действие не указано в коде... (действие: " + action + " )")
