# 03_python_control_structures/nested_if_elif_else.py

# Control Flow with if / elif / else in Python
# Demonstrates branching logic using language detection, time of day, season, and weekday.

import datetime

# Get current date and time
now = datetime.datetime.now()
hour = now.hour
month = now.month
day_of_week = now.weekday()  # Monday is 0, Sunday is 6

# User-defined language
# Options: "english", "russian", "german", "french", "italian"
language = input("Input your language: ")  

# Determine time of day 
if hour < 12:
    time_of_day = "morning"
elif 12 <= hour < 18:
    time_of_day = "afternoon"
else:
    time_of_day = "evening"

# Determine season 
if month in [12, 1, 2]:
    season = "winter"
elif month in [3, 4, 5]:
    season = "spring"
elif month in [6, 7, 8]:
    season = "summer"
else:
    season = "autumn"

# Determine if it's a weekend 
if day_of_week in [5, 6]:
    weekend = True
else:
    weekend = False

# Main branching logic based on language 
if language == "english":
    print("Language: English")

    # Time of day greeting
    if time_of_day == "morning":
        print("Good morning!")
    elif time_of_day == "afternoon":
        print("Good afternoon!")
    else:
        print("Good evening!")

    # Seasonal message
    if season == "winter":
        print("It's cold outside. Stay warm!")
    elif season == "spring":
        print("Flowers are blooming. Enjoy the weather!")
    elif season == "summer":
        print("It's hot! Time for the beach.")
    else:
        print("Leaves are falling. Autumn vibes!")

    # Weekend/weekday
    if weekend:
        print("It's the weekend. Time to relax!")
    else:
        print("It's a workday. Stay productive!")

elif language == "russian":
    print("Язык: Русский")

    if time_of_day == "morning":
        print("Доброе утро!")
    elif time_of_day == "afternoon":
        print("Добрый день!")
    else:
        print("Добрый вечер!")

    if season == "winter":
        print("На улице холодно. Одевайтесь теплее!")
    elif season == "spring":
        print("Весна пришла. Всё цветет!")
    elif season == "summer":
        print("Лето! Пора отдыхать.")
    else:
        print("Осень. Листья опадают.")

    if weekend:
        print("Выходной. Можно отдохнуть!")
    else:
        print("Рабочий день. Удачи в делах!")

elif language == "german":
    print("Sprache: Deutsch")

    if time_of_day == "morning":
        print("Guten Morgen!")
    elif time_of_day == "afternoon":
        print("Guten Tag!")
    else:
        print("Guten Abend!")

    if season == "winter":
        print("Es ist kalt. Bleib warm!")
    elif season == "spring":
        print("Der Frühling ist da. Alles blüht!")
    elif season == "summer":
        print("Sommerzeit! Zeit für den Strand.")
    else:
        print("Herbststimmung überall.")

    if weekend:
        print("Wochenende! Zeit zum Entspannen.")
    else:
        print("Arbeitstag. Viel Erfolg!")

elif language == "french":
    print("Langue : Français")

    if time_of_day == "morning":
        print("Bonjour!")
    elif time_of_day == "afternoon":
        print("Bon après-midi!")
    else:
        print("Bonsoir!")

    if season == "winter":
        print("Il fait froid. Restez au chaud!")
    elif season == "spring":
        print("Le printemps est là. Les fleurs poussent!")
    elif season == "summer":
        print("Il fait chaud. À la plage!")
    else:
        print("Les feuilles tombent. C'est l'automne.")

    if weekend:
        print("C'est le week-end. Repos bien mérité!")
    else:
        print("C'est un jour de travail. Bon courage!")

elif language == "italian":
    print("Lingua: Italiano")

    if time_of_day == "morning":
        print("Buongiorno!")
    elif time_of_day == "afternoon":
        print("Buon pomeriggio!")
    else:
        print("Buonasera!")

    if season == "winter":
        print("Fa freddo. Copriti bene!")
    elif season == "spring":
        print("È primavera. Che bello!")
    elif season == "summer":
        print("Estate! Andiamo al mare.")
    else:
        print("Autunno. Le foglie cadono.")

    if weekend:
        print("È il fine settimana. Rilassati!")
    else:
        print("Giorno lavorativo. Buon lavoro!")

else:
    print("Unsupported language.")

# Nested ifs can be used for more precise logic
# Use them when outer condition must be true to check inner
