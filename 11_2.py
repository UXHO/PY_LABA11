import re


def check_sentence(sent, word_lim):
    words = sent.split()
    return len(words) > word_lim


try:
    file = open('Sentences.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("Ошибка: файл не найден.")
    exit()
else:
    text = file.read()
    file.close()
    print("Текст успешно прочитан из файла.")

try:
    word_limit = int(input("Введите минимальное количество слов в предложении: "))
except ValueError:
    print("Ошибка: введите корректное целое число.")
    exit()

# Разделение текста на предложения по шаблону
sentences = re.split(r'(?<=[.!?]) +', text)
print(f"Найдено предложений: {len(sentences)}")

file = open('new_sentences.txt', 'w', encoding='utf-8')
for sentence in sentences:
    sentence = sentence.strip()
    if sentence and check_sentence(sentence, word_limit):
        file.write(sentence + '\n')
        print(f"Записано предложение: {sentence}")
file.close()
