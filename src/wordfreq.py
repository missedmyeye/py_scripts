"""The purpose of this script is to print the top (start rank)th to (end rank)th words
in a provided document by frequency, without the usage of third-party libraries.
"""
import urllib.request
import string
import json
import sys

def fetch_word_frequencies(url, start_rank=10, end_rank=20):
    """Fetch the top words in a document from a URL by frequency.
    
    Parameters:
    - url (str): The URL of the document.
    - start_rank (int): The starting rank of words to display.
    - end_rank (int): The ending rank of words to display.
    
    Returns:
    - List of tuples containing words and their frequencies.
    """
    # Fetch the text from the URL
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')

    # Preprocess the text
    # Replace line breaks with spaces
    text = text.replace('\n', ' ').replace('\r', ' ')

    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Sort the words by frequency
    sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

    # Get the words ranked by frequency
    ranked_words = sorted_word_count[(start_rank-1):end_rank]
    return ranked_words

if __name__ == "__main__":
    # Read configuration parameters from the file
    config = {}
    with open("freq_config.json", 'r') as file:
        config = json.load(file)[0]

        # Check command-line arguments
        if len(sys.argv) > 1 and sys.argv[1].strip():
            url = sys.argv[1]
        else:
            url = str(config.get('url'))

        if len(sys.argv) > 2 and sys.argv[2].strip():
            start_rank = int(sys.argv[2])
        else:
            # Read the config file if no START_RANK is provided, default to 10
            start_rank = int(config.get('start_rank', 10))

        if len(sys.argv) > 3 and sys.argv[3].strip():
            end_rank = int(sys.argv[3])
        else:
            # Read the config file if no END_RANK is provided, default to 20
            end_rank = int(config.get('end_rank', 20))

        # If inputted start rank more or same as end rank (erroneous), show only start rank
        if end_rank <= start_rank:
            end_rank = start_rank

    ranked_words  = fetch_word_frequencies(url,start_rank,end_rank)

    # Print the words ranked by frequency
    print(f"Words ranked from {start_rank}th to {end_rank}th by frequency:")
    for word, count in ranked_words:
        print(f"{word}: {count}")
