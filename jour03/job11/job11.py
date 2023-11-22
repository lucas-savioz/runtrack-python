def time_to_text(minutes):
    print(
        f"{minutes // 60} heure{'s' if minutes // 60 != 1 else ''}"
        + (f" et {minutes % 60} minute{'s' if minutes % 60 != 1 else ''}" if minutes % 60 != 0 else "")
        if isinstance(minutes, int) and minutes >= 0
        else
            print("Veuillez entrer un nombre entier positif")
    )

time_to_text(120)
time_to_text(155)
time_to_text(35)
time_to_text(5555)
time_to_text("BLABLA")
