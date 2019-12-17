import sys
import re

file1 = sys.argv[-1]
file2 = sys.argv[-2]

#Time Complexity is O(N)
#This function creates a file handler using "with" and only reads a single line at a time so
#all data from the file does not have to be stored at once.
def tokenize(file_name: str) -> list:
    tokens = []
    with open(file_name, 'r') as text_file:
        for line in text_file:
            tokens.extend(re.findall(r"[a-zA-Z0-9]+", line.lower()))
    return tokens

#Time Complexity is O(len(s) + len(t))
#Returns the intersection of the two sets, which are the overlapping tokens.
def find_intersection(set1: set, set2: set) -> set:
    return set1 & set2


#Time Complexity is O(N)
#Prints the number of tokens that overlap between both files.
def print_output(intersection_set: set) -> None:
    print(len(intersection_set))
    for word in intersection_set:
        print(word, sep = '\n')


def main():
    file1_token_set = set(tokenize(file1))
    file2_token_set = set(tokenize(file2))
    intersection = find_intersection(file1_token_set, file2_token_set)
    print_output(intersection)


if __name__ == "__main__":
    main()
