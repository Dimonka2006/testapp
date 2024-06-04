#проверка на ошибки try - except
print ("введите число а=")
try:
    a = float(input())
    procent = 100/a
    print("100/a = %s" % procent)
except ValueError:
    print ("Вы ввели не число")
except ZeroDivisionError:
    print ("Вы ввели 0!!!")
except:
    print ("Возникла ошибка!!! текст")
else:
    print ("Все выполнил")
finally:
    print("Блок выполняется в любом случае!!!")


    



