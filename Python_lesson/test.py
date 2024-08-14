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

def data_user(user, data);
    for i in data if i = user
