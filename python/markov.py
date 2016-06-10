#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

from random import randint
import string

printable = set(string.printable)

fname = "text_samples/wasteland.txt"
fname = "text_samples/cat_in_hat.txt"
fname = "text_samples/green_eggs_ham.txt"

#fname = raw_input()

output_len = 60
#output_len = input()

chain_n = 3

text = open(fname, 'r').read()
text = text.lower()
#text = ''.join([let if let in printable else ' ' for let in text])
text = text.replace("'", "")
text = text.replace("`", "")
text = text.replace("-", "")


# Get all words
words = text.split()

### PART 1: Start the text ###
randno = randint(0,len(words)-chain_n)
output = words[randno:randno+chain_n]

### PART 2: generate the rest ###


while len(output) < output_len:
    state = output[-chain_n:]
    history = dict()

    # Collect stats on past states like this
    validCount = 0
    for i in range(len(words)-chain_n-1):
        isValid = True
        for j in range(chain_n):
            isValid &= state[j]==words[i+j]
        if isValid:
            nextWord = words[i+chain_n]
            if nextWord in history:
                history[words[i+chain_n]] += 1
            else:
                history[words[i+chain_n]] = 1
            validCount += 1

    # Choose random number
    randno = randint(1, validCount)

    pastWords = history.keys()
    pos = 0
    for w in pastWords:
        pos += history[w]
        if pos >= randno:
            nextWord = w
            break

    output.append(nextWord)

# Print output
print ' '.join(output)




