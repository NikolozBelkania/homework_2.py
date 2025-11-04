



# Workshop 2-ის ძირითადი იდეები:

# მინიჭების ოპერატორი (=) გამოიყენება იმისთვის, რომ ცვლადს მნიშვნელობა მივანიჭოთ. მაგალითად: x = 5 ნიშნავს, რომ x ცვლადში ინახება 5.

# input() ფუნქცია საშუალებას აძლევს მომხმარებელს შეიყვანოს ინფორმაცია, რომელსაც პროგრამა შემდგომ იყენებს.

# პირობითი ოპერატორები (if, elif, else) პროგრამას აძლევს საშუალებას მიიღოს გადაწყვეტილება პირობების მიხედვით.

# ამ ელემენტების კომბინაციით შეიძლება შეიქმნას ინტერაქტიული პროგრამები, რომლებიც რეაგირებენ მომხმარებლის შეყვანაზე.


# Temperature check with safe input loop
while True:
    try:
        temperature = int(input("შეიყვანე ტემპერატურა: "))
        if temperature >= 30:
            print("ცხელა.")
        else:
            print("არ ცხელა.")
        break
    except ValueError:
        print("შეყვანილი მნიშვნელობა არ არის რიცხვი. სცადე თავიდან.")


# User info collection
name = input("შეიყვანე შენი სახელი: ")
age = input("შეიყვანე შენი ასაკი: ")
experience = input("გქონია თუ არა კოდის წერის გამოცდილება? (დიახ/არა): ")
favorite_lang = input("რომელია შენი საყვარელი პროგრამირების ენა? ")

print("\nმადლობა ინფორმაციისთვის, " + name + "!\n")

# Number comparison with safe input loop
while True:
    try:
        num1 = input("შეიყვანე პირველი რიცხვი: ")
        num2 = input("შეიყვანე მეორე რიცხვი: ")

        print("\nსტრიქონების პირდაპირი შედარება:")
        print(f"{num1} > {num2} არის {num1 > num2}")
        print(f"{num1} < {num2} არის {num1 < num2}")
        print(f"{num1} == {num2} არის {num1 == num2}")

        # Convert to int safely
        num1 = int(num1)
        num2 = int(num2)

        print("\nახლა, როცა გარდავქმნით int ტიპად:")
        print(f"{num1} > {num2} არის {num1 > num2}")
        print(f"{num1} < {num2} არის {num1 < num2}")
        print(f"{num1} == {num2} არის {num1 == num2}")
        break
    except ValueError:
        print("შეიყვანე მხოლოდ რიცხვები, სცადე თავიდან.")

# Study minutes conversion with safe input loop
while True:
    try:
        study_minutes = int(input("\nრამდენი წუთი ისწავლე დღეს?: "))
        hours = study_minutes // 60
        minutes = study_minutes % 60
        print(f"შენ ისწავლე {hours} საათი და {minutes} წუთი დღეს. მშვენიერი პროგრესია!")
        break
    except ValueError:
        print("შეიყვანე რიცხვი წუთებში, სცადე თავიდან.")

# Energy level
while True:
    energy = input("\nშეაფასე შენი ენერგიის დონე 1-დან 5-მდე: ")
    if energy in ["4", "5"]:
        print("შესანიშნავია, მაგარ ხოდზე ხარ! 💪")
        break
    elif energy == "3":
        print("სცადე მცირე შესვენება, რომ განიტვირთო. ☕")
        break
    elif energy in ["1", "2"]:
        print("წადი დაისვენე, მერე გააგრძელე. 😴")
        break
    else:
        print("შეყვანა არასწორია (შეიყვანე რიცხვი 1-დან 5-მდე). სცადე თავიდან.")


print("Packed study schedule!") if study_minutes > 180 and int(energy) >= 4 else None
