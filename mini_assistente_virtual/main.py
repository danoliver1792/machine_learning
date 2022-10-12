import pyttsx3
import os

engine = pyttsx3.init()
pyttsx3.speak('Cite um número para entrar em uma aplicação: ')

while True:
    print('Cite um número para entrar em uma aplicação: ')
    print('''\n1.MICROSOFT WORD \t 2.MICROSOFT POWERPOINT \t 3.MICROSOFT EXCEL \t
    4.GOOGLE CHROME \t 0.FOR EXIT
    ''')

    p = input()
    p = p.upper()
    print(p)

    if 'NAO' in p:
        pyttsx3.speak('Tente novamente')
        print('-')
        continue

    elif '1' in p:
        pyttsx3.speak('Iniciando o Word')
        os.system('start winword')
    elif '2' in p:
        pyttsx3.speak('Iniciando o Powerpoint')
        os.system('start powerpnt')
    elif '3' in p:
        pyttsx3.speak('Iniciando o Excel')
        os.system('start excel')
    elif '4' in p:
        pyttsx3.speak('Iniciando o Google Chrome')
        os.system('start chrome')
    elif '0' in p:
        pyttsx3.speak('Saindo da aplicação, obrigada!')
        break
    else:
        pyttsx3.speak(p)
        print('Comando invalido')
        pyttsx3.speak('Comando invalido! Tente novamente')
