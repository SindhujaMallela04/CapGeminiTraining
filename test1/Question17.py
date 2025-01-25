#funciton to count the occurences of each word in a sentence
def word_count(str):    
    words = str.split()
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
#function to get user input
def get_input():
    str = input("Enter a sentence: ")
    return str
#function to display the occurences of each word
def display(str):
    print("Word    Occurences of the word")
    for word, count in word_count(str).items():
        if word not in word_count(str):
            print(f"{word}         0")
        else:
            print(f"{word}      {count}")
#main function
def main():    
    str = get_input()
    display(str)
main()