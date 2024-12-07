import re
import csv

with open("task1-en.txt", "r", encoding="utf-8") as file:
    data = file.read()
numbers = re.findall(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?", data)
words = re.findall(r'\b\w{6}\b|\b\w{8}\b', data)
print(numbers, words)

print()

with open('task2.html', 'r', encoding='utf-8') as file:
    data = file.read()
content = re.findall(r'content="(https?://[a-zA-Z0-9.-/]+)"', data)
print(content)

print()

with open('task3.txt', 'r', encoding='utf-8') as file:
    data = ' ' + file.read() + ''

dates = re.findall(r'\d{4}[-]\d{2}[-]\d{2}', data)
for date in dates:
    data = data.replace(date, ' ')

sites = re.findall(r'https?://[a-zA-Z0-9.-]+/', data)
for site in sites:
    data = data.replace(site, ' ')

emails = re.findall(r'[a-z]{1}[a-z0-9.-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}', data)
for email in emails:
    data = data.replace(email, ' ')

names = re.findall(r'[A-Z]{1}[a-z]+', data)
for name in names:
    data = data.replace(name, ' ')

ids = re.findall(r'\d+', data)
for id in ids:
    data = data.replace(id, ' ')

records = list(zip(ids, names, emails, dates, sites))
records.sort(key=lambda r: int(r[0]))

with open('task3.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Surname', 'Email', 'Registration Date', 'Website'])
    for record in records:
        writer.writerow(record)

print(f"Данные сохранены в файл {'task3.csv'}.")
print(len(ids), len(names), len(emails), len(dates), len(sites))

print()

with open('task_add.txt', 'r', encoding='utf-8') as file:
    data = file.read()
dates = re.findall(r'\s(\d{2,4}[./-]\d{2,4}[./-]\d{2,4})',data)
emails = re.findall(r'\s([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})', data)
sites = re.findall(r'\s(https?://[a-zA-Z0-9.-/]+)', data)
print(*dates, sep='\t')
print(*emails, sep='\t')
print(*sites, sep='\t')