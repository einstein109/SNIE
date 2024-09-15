# Extended dictionary of negative phrases and positive rephrases about Doris
negative_phrases = {
    "Doris is lazy": "Doris is taking well-deserved rest and recharging her energy.",
    "Doris is annoying": "Doris has a unique personality that keeps life interesting.",
    "Doris never listens to me": "Doris is thoughtful and takes time to consider things deeply.",
    "Doris is selfish": "Doris knows how to prioritize her needs and maintain balance.",
    "Doris is always late": "Doris takes her time to ensure everything is perfect before she arrives.",
    "Doris doesn't care about me": "Doris shows her care in different ways, sometimes subtle but meaningful.",
    "Doris is bad at communicating": "Doris communicates in her own way, and it's something we're working on together.",
    "Doris is too demanding": "Doris has high standards, which motivates me to be my best.",
    "Doris makes everything about herself": "Doris is passionate and driven, which is one of the things I admire about her.",
    "Doris argues too much": "Doris has strong opinions and is confident enough to express them openly.",
    "Doris is an annoying bitch": "Kamama is an ambitious lover",
    "I hate her when she starts talking about her friend with a big ass": "I love her when she talks about her big hearted friends",
    "Like the fuck is that": "like the good amusement it is"
}

# Function to check for negative phrases and suggest positive alternatives
def rephrase_sentence(sentence):
    for neg_phrase, pos_phrase in negative_phrases.items():
        if neg_phrase.lower() in sentence.lower():
            print(f"Warning: Negative comment detected!")
            print(f"Rephrasing to: '{pos_phrase}'")
            return sentence.replace(neg_phrase, pos_phrase)
    return sentence

def main():
    print("Express your thoughts, and I'll help rephrase them into something positive! Type 'exit' to quit.")
    while True:
        sentence = input("You: ")
        if sentence.lower() == "exit":
            break
        positive_sentence = rephrase_sentence(sentence)
        print(f"Rephrased sentence: {positive_sentence}\n")

if __name__ == "__main__":
    main()
