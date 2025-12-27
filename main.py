import time
from analyzer import Analyzer


def main():
    analyzer = Analyzer()

    text = analyzer.read_file()
    analyzer.extract_words(text)

    common_words = analyzer.common_words()
    avg_word_length = analyzer.average_word_length()

    print("Text statistics")
    print("----------------")
    print(f"Total words       : {len(analyzer.words)}")
    print(f"Unique words      : {len(common_words)}")
    print(f"Avg word length   : {avg_word_length:.2f}")

    analyzer.plot_top_10_words()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()

    print(f"\nExecution time: {end - start:.6f} seconds")
