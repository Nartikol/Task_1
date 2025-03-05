print ("Задание 1")

name = "Nikolay"
print (name)

hobby = 'Work'
print (hobby)

film = """У меня есть любимый фильм
и он идет по телевизору"""
print (film)


print ("Задание 2")


text = "Programming"
print (text[0])
print (text[10])
print (text[:5])
print (text[4:])


print ("Задание 3")


name = "Nikolay"
surname = "Savchenko"
result = name + " " + surname
print (result)

text = "Hello" * 3
print (text)


print ("Задание 4")


age = "37"
city = "Tihoreck"
text = "Hello Nikolay, your are {} yes old. {} is your hometowh !".format(age, city)
print (text)


age = "37"
city = "Tihoreck"
text = (f'Hello Nikolay, your are {age} yes old. {city} is your hometowh !')
print (text)


print ("Задание 5")


text = "  пробелы  "
print (text.strip())

text = "Я люблю котов."
new_text = text.replace ("котов", "собак")
print (new_text)

text = "Python is great"
words = text.split()
print (words)

text = ["P", "y", "t", "h", "o", "n"]
text_str = "".join(text)
print ("И что-же за слово Мы получим при слиянии :", text_str)


