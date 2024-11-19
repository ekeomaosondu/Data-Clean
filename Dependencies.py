import re
import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag


def is_valid_token(token):
    #Invalidate punctuation and capitalized text
    return (not bool(re.match(r'.*[0-9,$\-%\':;\`/\.\*+•\"\“\”\’\—\_\¨].*', token))) and not token.isupper()
    

def natural(line):
    #Returns the sentence if it is natural language
    #Returns None otherwise
    cleaned_tokens = [token for token in word_tokenize(line) if is_valid_token(token)]

    pos_tags = pos_tag(cleaned_tokens)
    has_verb = any(tag.startswith('VB') for _, tag in pos_tags)
    has_noun = any(tag.startswith('NN') for _, tag in pos_tags)  
    is_short = len(cleaned_tokens) < 3

    if has_verb and has_noun and not is_short:
        return " ".join(cleaned_tokens)

def clean_corpus(corpus):
    #Clean an entire disclosure corpus

    
    corpus = re.sub(r"\(.*?\)", "", corpus)
    corpus = re.sub("Mr.", "Mr", corpus)
    corpus = re.sub("Inc.", "Inc", corpus)

    lines = corpus.splitlines()
    sentences = []

    for line in lines:
        sentences.extend(line.split(". "))
    

    natural_language_lines = []
    for sent in sentences:
        nat = natural(sent)
        if nat is not None:
            natural_language_lines.append(nat)
            
    return ". ".join(natural_language_lines)