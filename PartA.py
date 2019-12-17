import sys
import re
from collections import defaultdict


#Time Complexity is O(N)
#This function creates a file handler using "with" and only reads a single line at a time so
#all data from the file does not have to be stored at once.
def tokenize(file_name: str) -> list:
    tokens = [] # O(1)
    with open(file_name, 'r') as text_file:
        for line in text_file:
            tokens.extend(re.findall(r"[a-zA-Z0-9]+", line.lower()))
    return tokens

#Time Complexity is O(N)
#This function uses a defaultdict to count the frequency of tokens.
def compute_word_frequencies(token_list: list) -> dict:
    word_freq = defaultdict(int)  # O(1)
    for word in token_list:  # O(N)
        word_freq[word] += 1  # O(1)
    return word_freq


#Time Complexity is O(N Log N)
#This function prints the sorted key values primarily by the value, and then alphabetically
#between ties.
def print_frequencies(token_freq: dict) -> None:
    print("Token / Frequency", sep='\t')
    for k, v in sorted(token_freq.items(), key=lambda x: (-x[1], x[0])):  # O(N Log N)
        print(k, v)


def main():
    token_list = tokenize(sys.argv[-1])
    token_freq = compute_word_frequencies(token_list)
    print_frequencies(token_freq)


if __name__ == "__main__":
    main()
