"""The purpose of this script is to print the top 10th to 20th words
in a provided document by frequency, without the usage of third-party libraries.
"""
import urllib.request
import string

# Step 1: Fetch the text from the URL
url = "https://www.gutenberg.org/cache/epub/16317/pg16317.txt"
response = urllib.request.urlopen(url)
text = response.read().decode('utf-8')

# Step 2: Preprocess the text
# Remove punctuation and convert to lowercase
translator = str.maketrans('', '', string.punctuation)
text = text.translate(translator).lower()

# Step 3: Split the text into words
words = text.split()

# Step 4: Count the frequency of each word
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Step 5: Sort the words by frequency
sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

# Step 6: Print the words ranked from 10th to 20th by frequency
print("Top 10th to 20th words by frequency:")
for rank, (word, count) in enumerate(sorted_word_count[9:20], start=10):
    print(f"{rank}: {word} (Frequency: {count})")
