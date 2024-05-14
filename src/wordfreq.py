"""The purpose of this script is to print the top 10th to 20th words
in a provided document by frequency, without the usage of third-party libraries.
"""
import urllib.request
import string
import json

# Step 1: Read configuration parameters from the file
config = {}
with open("freq_config.json", 'r') as file:
    config = json.load(file)[0]

# Extracting parameters
url = str(config.get('url'))
start_rank = int(config.get('start_rank', 10))  # Default to 10 if not specified
end_rank = int(config.get('end_rank', 20))  # Default to 20 if not specified

# Step 2: Fetch the text from the URL
response = urllib.request.urlopen(url)
text = response.read().decode('utf-8')

# Step 3: Preprocess the text
# Replace line breaks with spaces
text = text.replace('\n', ' ').replace('\r', ' ')

# Remove punctuation and convert to lowercase
translator = str.maketrans('', '', string.punctuation)
text = text.translate(translator).lower()

# Step 4: Split the text into words
words = text.split()

# Step 5: Count the frequency of each word
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Step 6: Sort the words by frequency
sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

# Step 7: Print the words ranked from 10th to 20th by frequency
print(f"Top {start_rank} to {end_rank} words by frequency:")
for rank, (word, count) in enumerate(sorted_word_count[(start_rank-1):end_rank], start=start_rank):
    print(f"{rank}: {word} (Frequency: {count})")
