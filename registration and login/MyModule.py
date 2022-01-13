from random import *

users=[]
passwords=[]


def work():
    while True:
        print("Здравствуйте много уважаемый пользователь!, если хотите зарегистрироваться нажмите 1,если авторизваться то 2")
        print("1 - Регистрация")
        print()
        print("2 - Авторизация")
        print()
        print("3-Выход из программы")
        vast=int(input())
        print()
        if vast==1:
            print("Пожалуйста придумайте и введите свой логин и пароль")
            print()
            while 1:
                login=input("Введите ваш Логин: ")
                if login not in users:
                    print("Поздравляем с вашим новым логином:", login)
                    print()
                    break
                else:
                    print("К сожалению данный Логин уже используется, попробуйте ввести другой.")
                    print()
            print("Вы можете создать пароль самостоятельно нажав 1 или предоставить это нам нажав цифру 2:")
            print("1 - Самостоятельно")
            print("2 - Автоматически")
            passvast=int(input())
            if passvast==2:
                psa=random_pass()
                passwords.append(psa)
                break
            while 1:
                if passvast==1: #Регистрация
                    print("ВНИМАНИЕ! убедитесь что Ваш пароль  содержит: знаки, большие и маленькие символы, а так же цифры. ")
                    psa=input("Пожалейста Введите свой придуманный пароль: ")
                    check=password_check(psa)
                    if check==True:
                        users.append(login)
                        passwords.append(psa)
                        print("Поздравляем с созданием акаунта")
                        break
                       
                    else:
                        print("Извините, но Ваш пароль не подходит.")
                        print()
        if vast==2:   #Авторизация
            print("Пожалйста Введите Ваши данные для входа!")
            login=str(input("Ваш логин - "))
            password=str(input("Ваш пароль - "))
            check=autorisation_check(login,password)
            if check==True and checkz==True:
                print("Успешный вход, добро пожаловать!")
            else:
                print("Неверный логин или пароль! Попробуйте ещё раз.")
                print()
        if vast==3:
            break


def random_pass():
    import random
    """
    see funktsioon genereerib kasutaja registreerimiseks juhuslikult genereeritud parooli
    :rtype:list
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    print(ls)
    # Извлекаем из списка 12 произвольных значений
    psword = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    return psword
check=False    
def password_check(passwords:str)-> bool:
    """
    Kontrollib, kas parool sisaldab numbreid, suur- ja väiketähti ning kas need sisaldavad märke.
    :rtype:bool
    """
    global check
    spisok=list(passwords)
    a=b=c=d=e=False
    for q in spisok:
        if q.isdigit(): 
            a=True
        if q.isalpha():
            b=True
        if q.isupper():
            c=True
        if q.islower():
            d=True
        if q in list(".,:;!_*-+()/#¤%&"):
            e=True
        if a==True and b==True and c==True and d==True and e==True:
            check=True
        else:
            check=False
    return check

global psa
def autorisation_check(login:str,password:str)->bool:
    """
    see funktsioon kontrollib kasutaja volitusi identsete sisselogimiste ja paroolide olemasolu loendites ning kui kõik on õige, tagastab see tõene
    :param str login:
    :param str password:
    """
    check=checkz=False
    if login in users:
        check=True
    if password in passwords:
        checkz=True
    if check==True and checkz==True and users.index(login)==passwords.index(psa):
        check=True
    return check