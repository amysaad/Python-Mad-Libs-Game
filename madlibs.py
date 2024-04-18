#Author: Amy Saad
#Due Date: 11/24/2023
#Program description: Python program that will implements a short Mad Libs game. 
#The program asks the user to give random words like adjectives, nouns, adverbs, etc. without any context.

import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import spacy
import re
nltk.download('averaged_perceptron_tagger')
nlp = spacy.load("en_core_web_sm")

with open("text_file.txt", "r") as file:
    text = file.read()

def removeType(word):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    for tagged_word in tagged_words:
        if tagged_word[1].startswith("NN"):  # Noun
            return "(__Noun__)"
        elif tagged_word[1].startswith("VB"):  # Verb
            return "(__Verb__)"
        elif tagged_word[1] == "VBZ":  # Verb (3rd person)
            return "(__Verb (3rd person)__)"
        elif tagged_word[1].startswith("JJ"):  # Adjective
            return "(__Adjective__)"
        elif tagged_word[1].startswith("RB"):  # Adverb
            return "(__Adverb__)"
        elif tagged_word[1] == "IN":  # Preposition
            return "(__Preposition__)"
        else:
            return None
        
def createSentences(text):
    newSentence = ""
    for _ in range(2):
        sentences = nltk.sent_tokenize(text)
        current_sentence = random.choice(sentences)
        generated_text = [current_sentence]
        words = nltk.word_tokenize(current_sentence)
        next_word = random.choice(words)
        generated_text.append(next_word)
        current_sentence = ' '.join(words[1:]) + ' ' + next_word
        newSentence += " " + ' '.join(generated_text)
    return newSentence

def removeItems(words):
    newSentence = ""
    for word in words.split():
        if random.randint(0, 10) == 0:  # Randomly select a word for replacement
            if removeType(word) is not None:
                newSentence += (" " + removeType(word) + " ")  # Replacement happens here
            else:
                newSentence += " " + word
        else:
            newSentence += " " + word
    return newSentence.strip()

def recommendWord(sentence):
    doc = nlp(sentence)
    # Get the last word
    last_word = doc[-1].text
    # Get the most likely next word based on statistical likelihood
    next_word_candidates = []
    for token in doc[-1].head.rights:
        if token.is_alpha:
            next_word_candidates.append(token.text)
    return next_word_candidates

workbook = ""
def print_and_stop(sentence):
    global workbook
    placeholders = ["(__Noun__)","(__Verb__)","(__Verb (3rd person)__)","(__Adjective__)","(__Adverb__)","(__Preposition__)"]
    # Split the sentence into parts based on the placeholders
    parts = [sentence]
    for placeholder in placeholders:
        parts = [part for subpart in parts for part in subpart.split(placeholder)]
    # print
    for part in parts:
        part = part.strip()
        print(part)
        # Recommend a word based on the part
        if len(workbook) > 0:
            recommend = recommendWord(workbook)
        else:
            recommend = recommendWord(part)
        # Prompt user to try the recommended word
        user_input = input(f"Try: {recommend} > ")
        print(f"{part} ({user_input.strip()})")
        workbook += f" {part} {user_input.strip()} "
    print()

generated_sentence = createSentences(text)
sentence_blinks = removeItems(generated_sentence)
print_and_stop(sentence_blinks)
print(workbook)
