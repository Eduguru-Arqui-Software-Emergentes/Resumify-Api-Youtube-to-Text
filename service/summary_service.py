from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from models.response_summary import ResponseSummary

def summarize_text(text: str):
    stop_words = set(stopwords.words("spanish"))
    words = word_tokenize(text, language="spanish")
    freq_table = dict()
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    sentences = sent_tokenize(text, language="spanish")
    sentence_value = dict()
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq

    sum_values = 0
    for sentence in sentence_value:
        sum_values += sentence_value[sentence]

    average = int(sum_values / len(sentence_value))

    summary = ""
    for sentence in sentences:
        if sentence in sentence_value and sentence_value[sentence] > (1.2 * average):
            summary += " " + sentence

    return ResponseSummary(summary).to_dict()