import re
from collections import Counter
import timeit
import time
import matplotlib.pyplot as plt


class Analyzer:
    ''' Analyze text files and extract words '''
    def __init__(self):
        self.words = [] # List for each word in the txt

    def read_file(self):
        "Read the txt file or raise exception"
        try:
            with open("data.txt", "r", encoding="utf-8") as file:
                return file.read()

        except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
            print(f"File read error: {e}")
            raise
    
    def extract_words(self, text):
        "Extract all the words, remove spaces and punctuations"
        self.words = re.findall(r"\b\w+\b", text.lower())
        return self.words
    
    def common_words(self):
        "A function for the most common words in the data file"
        common = {}
        # for word in self.words:
        #     common[word] = common.get(word, 0) + 1    
        return Counter(self.words)
    
    def average_word_length(self):
        if not self.words:
            return 0
        total_length = sum(len(word) for word in self.words)
        return total_length / len(self.words)
    
    def plot_top_10_words(self):
        counts = Counter(self.words).most_common(10)

        labels = [word for word, _ in counts]
        values = [count for _, count in counts]

        plt.figure()
        plt.bar(labels, values)
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.title("Top 10 Most Common Words")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


def main():
    analyze = Analyzer()
    text = analyze.read_file()
    words = analyze.extract_words(text)
    common = analyze.common_words()
    avg = analyze.average_word_length()
    print(avg)
    analyze.plot_top_10_words()

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print("Time -> ", stop - start)