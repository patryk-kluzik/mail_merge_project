# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = '[name]'

with open(file="./Input/Names/invited_names.txt") as names:
    all_names = []
    for name in names.readlines():
        all_names.append(name.strip())

with open(file="./Input/Letters/starting_letter.txt") as letter:
    all_lines = letter.read()

    for name in all_names:
        full_text = ''.join(all_lines).replace(PLACEHOLDER, name)

        with open(file=f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output:
            output.write(full_text)

print(all_lines)
