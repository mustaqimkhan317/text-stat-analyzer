import re

class Analyzer:
    ''' Analyze text files and extract words '''
    def __init__(self):
        self.words = []

    def read_file(self):
        try:
            with open("data.txt", "r", encoding="utf-8") as file:
                return file.read()

        except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
            print(f"File read error: {e}")
            raise
    
    def extract_words(self, text):
        self.words = re.findall(r"\b\w+\b", text.lower())
        return self.words


def main():
    analyze = Analyzer()
    text = analyze.read_file()
    words = analyze.extract_words(text)
    print(words)

if __name__ == "__main__":
    main()