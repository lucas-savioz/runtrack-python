def arrondir_multiple_de_5(note):
    multiple_de_5 = round(note / 5) * 5
    if note - multiple_de_5 < 3:
        return multiple_de_5
    else:
        return note

notes_eleves = [45, 76, 37.6, 35, 39.5, 55, 26, 90, 62]

for note in notes_eleves:
    note_arrondie = arrondir_multiple_de_5(note)
    print(f"Note : {note}, Note arrondie : {note_arrondie}")

    if note_arrondie < 40:
        print("Tu as échoué le test")
    else:
        print("Tu as réussi le test")
