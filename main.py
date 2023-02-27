PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_names = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_names)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_names}.txt", mode="w") as completed_letters:
            ready_letter = new_letter.replace("Angela", stripped_names)
            completed_letters.write(ready_letter)




