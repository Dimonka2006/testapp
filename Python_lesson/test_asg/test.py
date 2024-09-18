import os

data = [
"2024-05-01 vasya Create file /etc/cron.d/old-cron",
"2024-05-19 robot Clear filesystem",
"2024-06-01 vasya Delete file /etc/cron.d/old-cron",
"2024-06-09 petr Create Directory /var/dir/name",
"2024-06-09 robot Deploy new version",
"2024-06-09 scaner Scan all directories",
"2024-06-19 robot Deploy new version",
"2024-06-19 robot Change permissions"
]

# Создаем пустой файл для записи данных
output_file = 'output.txt'
with open(output_file, 'w') as f:
    for line in data:
        if 'robot' in line:
            f.write(line + '\n')

print('Записи скопированы в файл:', output_file)

#сначала проверяет каждую строку в списке data, 
# ищет подстроку robot, и записывает такие строки в файл output.txt. 
# В конце выполнения он выведет сообщение о том, 
# что данные были успешно скопированы в файл.