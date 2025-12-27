import re

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

        for value in self.words:
            if value not in common:
                common[value] = 1
            else:
                common[value] += 1    
        
        return common


def main():
    analyze = Analyzer()
    text = analyze.read_file()
    words = analyze.extract_words(text)
    common = analyze.common_words()
    print(common)

if __name__ == "__main__":
    main()