#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(file="./Input/Names/invited_names.txt") as names:
    all_names = []
    for name in names.readlines():
        all_names.append(name.strip())



with open(file="./Input/Letters/starting_letter.txt") as letter:
    first_line = letter.readline()
    remaining_lines = []
    for line in  letter.readlines()[1:]:
        if line == "\n":
            remaining_lines.append(line)
        else:
            remaining_lines.append(line.strip())
    for name in all_names:
        full_text = first_line.join(remaining_lines).replace("[name]", name)
        #
        # with open(file=f"./Output/ReadyToSend/letter_for_{name}.txt", mode="x") as output:
        #     output.write(first_line)
        #     output.write(remaining_lines)



print(full_text)