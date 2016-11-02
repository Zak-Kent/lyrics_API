from models import Song_BOW

import gensim
import time

# need to import a hard coded dict object because django can't use a pickled obj during testing
from data_loader import dict_test

# imports stemming script used on all lyrics in model 
from lyrics_data.word_stemmer import lyrics_to_bow

# need to import dict of words 
# also need to include trained NB model and tfidf model here 

# ******* really just need to build a class that takes a paragraph and breaks it down to word 
# counts in the format we need 


def parse_data_predict(data):
    parsed_data = lyrics_to_bow(data)
    print(type(parsed_data))
    print(parsed_data)

    dicty = dict_test()

    # breaks words into a dict where keys map to the word's # in lookup dict 
    # ex. 23: 2 --> the 23rd word in the lookup dict was seen in the song 2 times 
    new_dict = {}
    for word in parsed_data.keys():
        try:
            new_dict[dicty[word]] = parsed_data[word]
        except:
            print('fail!!!!!!!!!!!!!!!!!!!!')
            

    new_new = new_dict
    print(type(new_new))
    print(new_new)

    year = 1983

    # load_models()

    Song_BOW.objects.create(
                            bow=new_new,
                            year=year)


# parse_data_predict("Don't turn turn your eyes away And please say that you will stay A while")









