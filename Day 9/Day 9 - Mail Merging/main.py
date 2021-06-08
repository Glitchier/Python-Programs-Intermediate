with open("./input/names/names.txt") as name_file:
    names = name_file.readlines()

with open("./input/letters/starting_letter.docx") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_content.replace("[name]",striped_name)
        with open(f"./output/ReadyToSend/Letter_to_{striped_name}.docx",mode="w") as completed_letter:
            completed_letter.write(new_letter)