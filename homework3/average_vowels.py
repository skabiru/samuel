# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.
def counting_vowels_and_consonants(text):
    vowels = 0 # initialize both the vowels and consonants so we can track the numbers
    consonants = 0
    vowels_possible = "aeiouAEIOU" # check if the letter is in here and if so it can count as a vowel

    for i in text:
        if i.isalpha():
            if i in vowels_possible:
                vowels = vowels + 1
            else:
                consonants += 1
    return (vowels, consonants)

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()
def average_vowels_and_consonants(paragraph):
    sentences = paragraph.split(". ") # splits the paragraph into sentences
    num_sentences = len(sentences)
    
    total_vowels = 0
    total_consonants = 0 # initialize the count
    
    for i in sentences: # for each sentence count the vowels and consonants
        v,c = counting_vowels_and_consonants(i)
        total_vowels += v
        total_consonants += c

        return (num_sentences, total_vowels/ num_sentences, total_consonants/ num_sentences)


# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
number, avg_vowel, avg_consonant = average_vowels_and_consonants(paragraph)

print(f"Average Vowels per Sentence: {avg_vowel}")
print(f"Average Consonants per Sentence: {avg_consonant}")