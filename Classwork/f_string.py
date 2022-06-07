from datetime import datetime

name = 'Dorcas'
lang = "Java"
age = 16

fff = f"{name} is a {lang} lord and {age}years old"
print(fff)
print(f'{name=}, {age=}, , {datetime.datetime.now():%A}')

print(datetime.date())
