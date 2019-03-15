import nltk
import sys
import re
from os import listdir                        #needed imports


def main():
    text = sys.argv[1]
    text = text.replace("\n", " ")        #removes all newline characters
    text = text.lower()                   #makes all words lowercase
    text = text.replace(".", " .")        #this seperates out the periods
    tweet = nltk.tokenize.TweetTokenizer()
    tokens = tweet.tokenize(text)
    if tokens.__contains__(":-)"):
        print("happy")
        text = text.replace(":-)", "")
    word_tokens = nltk.word_tokenize(text)
    misspell_tokens = tweet.tokenize(text)
    tagged = nltk.pos_tag(word_tokens)
    print(tagged)


if len(sys.argv) < 2:              #prints error message if no string is passed
    print("Error : No input")
else:
    main()