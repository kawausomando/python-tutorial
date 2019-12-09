from datetime import date

now = date.today()

print(now)
# 2019-12-09

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# 12-09-19. 09 Dec 2019 is a Monday on the 09 day of December.

birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)
# 20219