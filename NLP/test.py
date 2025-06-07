# NLP Fundamentals with Python
# Install required packages: pip install nltk spacy scikit-learn

import nltk
import spacy
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import re

# Download NLTK data (run once)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Sample text data
texts = [
    "I love this movie! It's absolutely fantastic.",
    "This film is terrible. I hate it.",
    "Great acting and amazing storyline.",
    "Boring movie with poor dialogue.",
    "Best movie ever! Highly recommended."
]

labels = ['positive', 'negative', 'positive', 'negative', 'positive']

print("=== 1. TEXT PREPROCESSING ===")

def preprocess_text(text):
    """Basic text preprocessing"""
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text

# Preprocess our texts
preprocessed_texts = [preprocess_text(text) for text in texts]
for i, (original, processed) in enumerate(zip(texts, preprocessed_texts)):
    print(f"Original: {original}")
    print(f"Processed: {processed}")
    print()

print("\n=== 2. TOKENIZATION WITH NLTK ===")

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Tokenization
sample_text = "Hello world! This is a sample sentence. How are you doing today?"
tokens = word_tokenize(sample_text)
sentences = sent_tokenize(sample_text)

print(f"Word tokens: {tokens}")
print(f"Sentence tokens: {sentences}")

# Stop words removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print(f"After removing stop words: {filtered_tokens}")

# Stemming vs Lemmatization
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ['running', 'runs', 'ran', 'better', 'good']
print(f"\nOriginal words: {words}")
print(f"Stemmed: {[stemmer.stem(word) for word in words]}")
print(f"Lemmatized: {[lemmatizer.lemmatize(word) for word in words]}")

print("\n=== 3. BAG OF WORDS ===")

def create_bow(texts):
    """Create bag of words representation"""
    # Get all unique words
    all_words = []
    for text in texts:
        all_words.extend(text.split())
    
    vocab = list(set(all_words))
    print(f"Vocabulary: {vocab}")
    
    # Create BOW vectors
    bow_vectors = []
    for text in texts:
        vector = [text.split().count(word) for word in vocab]
        bow_vectors.append(vector)
    
    return bow_vectors, vocab

bow_vectors, vocab = create_bow(preprocessed_texts)
for i, vector in enumerate(bow_vectors):
    print(f"Text {i+1}: {vector}")

print("\n=== 4. TF-IDF ===")

# Using scikit-learn for TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(texts)

print(f"TF-IDF matrix shape: {tfidf_matrix.shape}")
print(f"Feature names: {tfidf_vectorizer.get_feature_names_out()}")
print(f"TF-IDF matrix (first document): {tfidf_matrix[0].toarray()}")

print("\n=== 5. TEXT CLASSIFICATION ===")

# Simple sentiment analysis using Naive Bayes
classifier = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', MultinomialNB())
])

# Train the classifier
classifier.fit(texts, labels)

# Test on new data
test_texts = [
    "This movie is amazing!",
    "I didn't like this film at all."
]

predictions = classifier.predict(test_texts)
probabilities = classifier.predict_proba(test_texts)

for text, pred, prob in zip(test_texts, predictions, probabilities):
    print(f"Text: '{text}'")
    print(f"Prediction: {pred}")
    print(f"Probabilities: {prob}")
    print()

print("=== 6. SPACY ADVANCED PROCESSING ===")

# Load spaCy model (install with: python -m spacy download en_core_web_sm)
try:
    nlp = spacy.load("en_core_web_sm")
    
    doc = nlp("Apple Inc. is looking at buying U.K. startup for $1 billion")
    
    print("Tokens and their properties:")
    for token in doc:
        print(f"{token.text:12} {token.pos_:10} {token.lemma_:15} {token.is_stop}")
    
    print("\nNamed Entities:")
    for ent in doc.ents:
        print(f"{ent.text:15} {ent.label_:10} {spacy.explain(ent.label_)}")
    
    print("\nDependency Parsing:")
    for token in doc:
        print(f"{token.text:12} -> {token.head.text:12} ({token.dep_})")

except OSError:
    print("SpaCy English model not installed. Run: python -m spacy download en_core_web_sm")

print("\n=== 7. WORD FREQUENCY ANALYSIS ===")

def analyze_word_frequency(texts):
    """Analyze word frequency across texts"""
    all_words = []
    for text in texts:
        # Simple tokenization
        words = re.findall(r'\b\w+\b', text.lower())
        all_words.extend(words)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in all_words if word not in stop_words]
    
    # Count frequencies
    word_freq = Counter(filtered_words)
    
    return word_freq

word_freq = analyze_word_frequency(texts)
print("Most common words:")
for word, count in word_freq.most_common(10):
    print(f"{word}: {count}")

print("\n=== 8. SIMPLE TEXT SIMILARITY ===")

from sklearn.metrics.pairwise import cosine_similarity

# Calculate similarity between texts using TF-IDF
tfidf_matrix = tfidf_vectorizer.fit_transform(texts)
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

print("Text similarity matrix:")
for i in range(len(texts)):
    for j in range(len(texts)):
        print(f"{similarity_matrix[i][j]:.3f}", end="  ")
    print()

print("\nMost similar pairs:")
for i in range(len(texts)):
    for j in range(i+1, len(texts)):
        similarity = similarity_matrix[i][j]
        print(f"Text {i+1} & Text {j+1}: {similarity:.3f}")
        if similarity > 0.1:
            print(f"  Text {i+1}: {texts[i]}")
            print(f"  Text {j+1}: {texts[j]}")
        print()
