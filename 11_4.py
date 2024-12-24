import re


def create_oglav(input_file, output_file):
    file = open(input_file, 'r')
    text = file.read()
    file.close()

    chapters = re.findall(r'(Глава \d+|Chapter \d+)\n(.+)', text)

    file = open(output_file, 'w')
    file.write("Оглавление\n")
    for chapter in chapters:
        file.write(f"{chapter[0]}. {chapter[1]}\n")
    file.close()


input_f = 'Chapters.txt'
output_f = 'Contents.txt'

create_oglav(input_f, output_f)
