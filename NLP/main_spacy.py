def display_format(length):
    for i in range(length):
        print('-', end="")
    print()

import spacy
nlp = spacy.load('en_core_web_sm') # Load the english model

# text, label_, pos_, lemma_, dep_

while True:
    # text_input = input("You: ") # Ask a prompt from the user
    text_input = "Elon Musk founded SpaceX in 2002 and was born in South Africa."
    prompt = nlp(text_input) # Processed NLP object

    print("[ TOKENIZATION ]")
    display_format(16)

    # 1. Tokenization [ Splitting Text ]
    for token in prompt:
        print(f'{token.text}')

    print()
    print("[ NAMED ENTITY RECOGNITION ]")
    display_format(28)

    # 2. NER [ Named Entity Recognition ]
    for token in prompt.ents:
        print(f'{token.text} >> {token.label_}')

    print()
    print("[ PART-OF-SPEECH ]")
    display_format(18)

    # 3. POS [ Part-of-speech ]
    for token in prompt:
        print(f'{token.text} >> {token.pos_}')

    print()
    print("[ LEMMATIZATION ]")
    display_format(17)

    # 4. Lemmatization [ Extracting base form of words ]
    for token in prompt:
        print(f'{token.text} >> {token.lemma_}')

    print()
    print("[ DEPENDENCY PARSING ]")
    display_format(22)

    # 5. Dependency Parsing [ Finding relationships ]
    for token in prompt:
        print(f'{token.text} >> {token.dep_} >> {token.head.text}')
    break