import re
import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    """
    Clean and preprocess text using spaCy.

    Steps:
    1. Lowercase
    2. Remove numbers
    3. Remove punctuation
    4. Remove stopwords
    5. Lemmatization

    Returns:
        str: Cleaned text
    """

    # Convert to lowercase
    text = text.lower()

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove punctuation
    text = re.sub(r"[^\w\s]", " ", text)

    # Process with spaCy
    doc = nlp(text)

    cleaned_tokens = []

    for token in doc:
        if (
            not token.is_stop
            and not token.is_punct
            and token.is_alpha
        ):
            cleaned_tokens.append(token.lemma_)

    return " ".join(cleaned_tokens)