def display_format(length):
    for i in range(length):
        print('-', end="")
    print();

import spacy
nlp = spacy.load('en_core_web_sm') # Load the english model

while True:
    # text_input = input("You: ") # Ask a prompt from the user
    text_input = "Elon Musk founded SpaceX in 2002 and was born in South Africa."
    prompt = nlp(text_input) # Processed NLP object

    counter = 1
    print(" [ TOKENIZATION ]")
    display_format(18)

    # 1. Tokenization [ Splitting Text ]
    for token in prompt:
        print(f'{counter}. {token.text}')
        counter += 1

    print("      [ NER ]")
    display_format(19)

    # 2. NER [ Named Entity Recognition ]
    for token in prompt.ents:
        print(f'{token.text} >> {token.label_}')

    print("      [ POS ]")
    display_format(19)

    # 3. POS [ Part-of-speech ]
    for token in prompt:
        print(f'{token.text} >> {token.pos_}')

    print(" [ LEMMATIZATION ]")
    display_format(19)

    # 4. Lemmatization [ Extracting base form of words ]
    for token in prompt:
        print(f'{token.text} >> {token.lemma_}')

    print("[ DEPENDENCY PARSING ]")
    display_format(22)

    # 5. Dependency Parsing [ Finding relationships ]
    for token in prompt:
        print(f'{token.text} >> {token.dep_} >> {token.head.text}')
    break