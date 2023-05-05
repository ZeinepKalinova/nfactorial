import random
import string

def generate_name(bigrams, length):
    """
    Генерирует имя заданной длины, используя вероятности биграмм
    """
    name = ""
    # выбираем первую букву случайным образом
    current = random.choice(string.ascii_lowercase)
    name += current
    # генерируем оставшиеся буквы
    for i in range(length - 1):
        # получаем вероятности для следующих биграмм
        freqs = bigrams.get(current, {})
        # выбираем следующую букву случайным образом
        if freqs:
            current = random.choices(list(freqs.keys()), weights=list(freqs.values()))[0][-1]
        else:
            current = random.choice(string.ascii_lowercase)
        name += current
    return name.capitalize()

def calculate_bigram_probabilities(words):
    """
    Вычисляет вероятности всех биграмм в словах
    """
    bigrams = {}
    for word in words:
        # добавляем начальный и конечный символы
        word = "^" + word + "$"
        for i in range(len(word)-1):
            # получаем текущую и следующую буквы
            current = word[i]
            next = word[i+1]
            # создаем словарь с частотами для текущей буквы
            freqs = bigrams.get(current, {})
            # увеличиваем частоту для текущей буквы и следующей буквы
            freqs[next] = freqs.get(next, 0) + 1
            # сохраняем словарь с частотами для текущей буквы
            bigrams[current] = freqs
    # вычисляем вероятности для всех биграмм
    for current in bigrams:
        total = sum(bigrams[current].values())
        for next in bigrams[current]:
            bigrams[current][next] /= total
    return bigrams

# загружаем данные из файла
with open("names.txt") as f:
    names = [line.strip() for line in f]

# вычисляем вероятности биграмм
bigrams = calculate_bigram_probabilities(names)

# генерируем имена
for i in range(10):
    print(generate_name(bigrams, 5))
