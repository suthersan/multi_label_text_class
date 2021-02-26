import pandas as pd
import spacy

def read_data(file_name, nlp):
    read_data = pd.read_csv(file_name,skip_blank_lines = True)
    read_data = read_data.dropna()
    
    val = ''
    result = []

    for text in nlp.pipe(iter(read_data['text'])):
        for token in text:
            val = val + ' ' + token._.tfidf
        result.append(val)
        val=''
    read_data.drop(['text'], axis=1)
    read_data['text'] = result

    return read_data