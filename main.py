_file = r"C:\Users\ASUS2022\Desktop\data.txt"
_file1 = r"C:\Users\ASUS2022\Desktop\usa1.txt"
# 1 count words and sentences
num_lines = []
t_words = []
palingrams_words = []
words = []
def read_text(_file, t_words, num_lines):
    with open(_file) as f:
        for line in f:
            t_words += line.split()
            num_lines += line.split(".")

read_text(_file,t_words, num_lines)
for word in t_words:
    words += word.split(".")
for word in words:
     if(word==''):
         words.remove(word)
print('Number of words in text file:', len(words))
print('Number of sentences in text file:', len(num_lines)-1)

#2 find palindormes
palindromes = []
def check_palindromes(str)->bool:
    if(len(str) > 1):
        if(str==str[::-1]):
            return True
        else:
            return False

def get_all_palindromes(words):
    for word in words:
        if(check_palindromes(word)):
            palindromes.append(word)

get_all_palindromes(words)

print("All palindromes in text file: ", palindromes)

# find palingrams
palingrams = []

read_text(_file1, palingrams_words, num_lines)

def find_palingrams(palingrams_words):
    for word_ in palingrams_words:
        for word in palingrams_words:
            if word_ in word:
                palingrams.append(word_)

find_palingrams(palingrams_words)

print("All palingrams in text file: ", palingrams)