from models import Song_BOW
import pickle 

# imports stemming script used on all lyrics in model 
from lyrics_data.word_stemmer import lyrics_to_bow

# need to import dict of words 
# also need to include trained NB model and tfidf model here 

# ******* really just need to build a class that takes a paragraph and breaks it down to word 
# counts in the format we need 

def parse_data_predict(data):
    parsed_data = lyrics_to_bow(data)
    year = 1983



    Song_BOW.objects.create(
                            bow=parsed_data,
                            year=year)