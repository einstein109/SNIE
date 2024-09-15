# Dictionary of swear words and alternatives
swear_words = {
    "damn": "darn",
    "hell": "heck",
    "shit": "shoot",
    "fuck": "amazement",
    "bitch": "lover",
    "asshole": "jerk",
    "motherfucker": "dude",
    "Annoying": "ambitious",
    "hate": "love",
    "ass": "heart",
    "Doris": "Kamama",
}

# Function to check for swear words and suggest alternatives
def check_swear_words(sentence):
    words = sentence.split()
    clean_sentence = []
    for word in words:
        lower_word = word.lower()
        if lower_word in swear_words:
            print(f"Warning: '{word}' is a swear word!")
            print(f"Try saying '{swear_words[lower_word]}' instead.")
            clean_sentence.append(swear_words[lower_word])
        else:
            clean_sentence.append(word)
    return " ".join(clean_sentence)

def main():
    print("Type your sentences below. Type 'exit' to quit.")
    while True:
        sentence = input("You: ")
        if sentence.lower() == "exit":
            break
        clean_sentence = check_swear_words(sentence)
        print(f"Rephrased sentence: {clean_sentence}\n")

if __name__ == "__main__":
    main()
