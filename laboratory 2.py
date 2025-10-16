#prog 1
password=input("Введите пароль:")
a=len(password) #длина пароля
if a<8:
    print("Cлишком короткий пароль")
print("Пароль принят")


#prog 2
status=input("online/offline") 
if status=="online":
    print("Связь установлена")
else:
    print("Cвязь потерена")

#prog 3
a=int(input("Введите уровень угрозы 1-100"))
if 1<=a<=30:
    print("Низкий уровень угрозы")
elif 31<=a<=70:
    print("Cредний уровень угрозы")   
elif 71<=a<=100:
    print("Высокий уровень угрозы")    
else:
    print("Oшибка ввода")    


#prog 4
cheksum_original=input() #оригинальное значение
cheksum_current=input()  #текущее значение
status="Файл не изменен" if cheksum_original==cheksum_current else"Файл поврежден" 
print(status)

#prog 5
event_code=input("Введите код события(ERR,WRN,INF)")
match event_code:
    case "ERR":
        print("Oшибка системы")
    case "WRN":
        print("Предупреждение")
    case "INF":
        print("Информационное сообщение")
    case _: 
        print("Неизвестный код события")