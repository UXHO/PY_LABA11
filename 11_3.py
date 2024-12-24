import random


def generate_sentence(phrases):
    return ' '.join(random.choice(element) for element in phrases)


def write_sentences_to_file(sentences):
    file = open('Result.txt', 'a')
    file.write('\n\n'.join(sentences) + '\n\n')
    file.close()


file1 = open('Phrases.txt', 'r')
lines = [line.strip().split('; ') for line in file1]
file1.close()

while True:
    try:
        num_sentences = int(input("Сколько предложений вы хотите сгенерировать? "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
    else:
        break

sents = [generate_sentence(lines) for _ in range(num_sentences)]
write_sentences_to_file(sents)

while True:
    answer = input("Хотите продолжить?: ").strip().lower()
    if answer == 'нет':
        break
    elif answer == 'да':
        while True:
            try:
                num_sentences = int(input("Сколько предложений вы хотите сгенерировать? "))
            except ValueError:
                print("Пожалуйста, введите целое число.")
            else:
                break

        sents = [generate_sentence(lines) for _ in range(num_sentences)]
        write_sentences_to_file(sents)
    else:
        print("Пожалуйста, ответьте 'Да' или 'Нет'.")
