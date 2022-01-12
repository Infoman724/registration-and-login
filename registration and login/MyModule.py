from random import *

users=["vlad"]
passwords=["vlad1234"]


def work():
    while True:
        print("Здравствуйте много уважаемый пользователь!, если хотите зарегистрироваться нажмите 1,если авторизваться то 2")
        print("1 - Регистрация")
        print("2 - Авторизация")
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
                if passvast==1:
                    print("ВНИМАНИЕ! убедитесь что Ваш пароль  содержит: знаки, большие и маленькие символы, а так же цифры. ")
                    psa=input("Пожалейста Введите свой придуманный пароль: ")
                    check=str
                    if check==str:
                        users.append(login)
                        passwords.append(psa)
                        print("Поздравляем с созданием акаунта")
                        break
                       
                    else:
                        print("Извините, но Ваш пароль не подходит.")
                        print()
        if vast==2:
            print("Пожалйста Введите Ваши данные для входа!")
            login=str(input("Ваш логин - "))
            password=str(input("Ваш пароль - "))
            check=autorisation_check(login,password)
            if check==True and check1==True:
                print("Успешный вход, добро пожаловать!")
            else:
                print("Неверный логин или пароль! Попробуйте ещё раз.")
                print()



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
    print("Ваш пароль,",psword)
    



def autorisation_check(login:str,password:str)->bool:
    """
    see funktsioon kontrollib kasutaja volitusi identsete sisselogimiste ja paroolide olemasolu loendites ning kui kõik on õige, tagastab see tõene
    :param str login:
    :param str password:
    """
    if login in users:
        check=True
    else:
        check=False
    if password in passwords:
        check1=True
    else:
        check1=False
        return check