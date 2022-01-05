def work():
    login=[]
    pswrd=[]
    vast=str(input("Здравствуйте уважаемый пользователь! если вы хотите зарегистрироваться нажмите reg,если авторизоваться loggin,если хотите прератить работу нажмите stop   "))
    if vast=="reg":
        log=str(input("введите свой логин =>"))
        login.append(log)
        print(login)
        pasvast=str(input("мы можем создать пароль автоматичекси для этого нажмите 4,если хотите создать пароль сами нажмите 5 =>"))
        if pasvast==4:
            import random
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
            print(psword)
    elif pasvast==5:
        paswrd=str(input("введите свой пароль=>"))
        pswrd.append(paswrd)
        print(pswrd)
            