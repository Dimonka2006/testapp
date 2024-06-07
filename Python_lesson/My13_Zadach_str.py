# replace in string substring name to your name
s = "Hello world name"
# строки не изменяемы, но можно создать по шаблону с заменой нужных слов
name_to_replace = "name" 
name_new = "dus"

s_new = s.replace(name_to_replace, name_new)
print(s_new)

# output all values < 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [i for i in a
      if i < 5]

print(b) 