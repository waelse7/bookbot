from re import T


class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.file_content = self.__read_file()
    
    def __read_file(self):
        with open(f"./books/{self.filename}", 'r') as f:
            return f.read()
    
    def count_words(self):
        return len(self.file_content.split())
    
    def count_letters(self):
        letters = {}
        for char in self.file_content:
            if char.isalpha():
                char = char.lower()
                letters[char] = letters.get(char, 0) + 1
        return letters

def main():
    filereader = FileReader("frankenstein.txt")
    words = filereader.count_words()
    letters = filereader.count_letters()
    letters_list = list(letters.items())
    letters_list.sort(key=lambda item: item[1], reverse=True)
    print("------Report------")
    print(f"There are {words} in the text.")
    print("Letter count")
    for char, count in letters_list:
        print(f"{char}: {count}")
    print("-------------------")

if __name__ == "__main__":
    main()