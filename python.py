import random
from collections import defaultdict


class BigramLanguageModel:
    def __init__(self, data_file):
        self.bigram_counts = defaultdict(int)
        self.char_counts = defaultdict(int)
        self.char_list = []
        self.read_data(data_file)

    def read_data(self, data_file):
        with open(data_file, "r") as f:
            for line in f:
                line = line.strip().lower()
                for i in range(len(line) - 1):
                    bigram = line[i:i+2]
                    self.bigram_counts[bigram] += 1
                    self.char_counts[bigram[0]] += 1
                    if i == 0:
                        self.char_list.append(bigram[0])

    def get_probability_table(self):
        probability_table = defaultdict(dict)
        for bigram, count in self.bigram_counts.items():
            char = bigram[0]
            probability = count / self.char_counts[char]
            probability_table[char][bigram[1]] = probability
        return probability_table

    def generate_name(self):
        name = random.choice(self.char_list)
        while True:
            char = name[-1]
            if char not in self.get_probability_table():
                break
            next_char = random.choices(
                list(self.get_probability_table()[char].keys()),
                list(self.get_probability_table()[char].values())
            )[0]
            name += next_char
        return name
