from analyzer import Analyzer
import time

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