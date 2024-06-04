#
f = open("my_file.txt", "w")
f.write("Hi my file")
f.close()

f = open("123.txt")
r = f.read()
print(r)


#for i in range(0, 5):
#  print(i)

s = [54464, 454, 4422, 4545]
print("Max: ", max(s))
print("Min: ", min(s))
print(list(range(0, 5)))
print("Sum: ", sum(list(range(0, 5,))))


#Шаг 2
print(list(range(0, 10, 2)))

s = "Ochen mnogo znaniy"
print(len(s))





eval ('''print("Hi again!!! 777")''')
#print("Введите выражение:")
#v = input()
#print("результат:", eval(v))

#exect ('''s=10
#b=20
#print(s+b)
#''')


s = "Hello!"
print (s)
print(s.upper())


print (abs(-10))

skorost = -120
if abs (skorost) > 0:
    print("Игорк движется")

if skorost > 0 or skorost <0:
    print("2: Игорк движется")

s = "hi"
dir (s)
help(s.upper)



print("Введите ваш возраст")
age = input()
if int(age)>10:
    print("вам больше 10")
    
if int(age)<50:
    print("Пойдет, вам пока еще нормально")    