from models import Song_BOW

import gensim
import pickle

from sklearn.externals import joblib
from scipy.sparse import lil_matrix

# need to import a hard coded dict object because django can't use a pickled obj during testing
from data_loader import dict_test
from dict_pickle import convert_dict

# imports stemming script used on all lyrics in model 
from lyrics_data.word_stemmer import lyrics_to_bow

# need to import dict of words 
# also need to include trained NB model and tfidf model here 

# ******* really just need to build a class that takes a paragraph and breaks it down to word 
# counts in the format we need 

def matrix_func(a_list):
    """take a list of dicts and return a sparse lil_matrix"""
    # make a matrix that matches the size of list of dicts 
    sparse_matrix = lil_matrix((len(a_list), 5000))

    # loop through each dict in list, and add that dicts values to idx of key in sparse matrix 
    for idx, a_dict in enumerate(a_list):

        for key in a_dict.keys(): 
            # subtracting 1 from the key because values in dict start at 1 
            sparse_matrix[idx, key - 1] = a_dict[key]
    
    return sparse_matrix


def parse_data_predict(data):
    parsed_data = lyrics_to_bow(data)
    print(type(parsed_data))
    print(parsed_data)

    # try: 
    #     dicty = pickle.load('save_dict.p', 'rb')
    # except:
    #     print('exception on loading pickle')
    #     # during testing django can't load pickle files so you have to load hard coded dict
    #     dicty = dict_test()

    # # breaks words into a dict where keys map to the word's # in lookup dict 
    # # ex. 23: 2 --> the 23rd word in the lookup dict was seen in the song 2 times 
    # new_dict = {}
    # for word in parsed_data.keys():
    #     try:
    #         new_dict[dicty[word]] = parsed_data[word]
    #     except:
    #         print('word not in dictionary, skipped')
            

    # new_new = new_dict
    # print(type(new_new))
    # print(new_new)
    print('3' * 50)
    
    new_test = convert_dict(parsed_data)
    print(new_test)

    # ----------------------------------------------------------------
    # get tfidf for word counts 

    tfidf = gensim.models.TfidfModel.load("full_tfidf_model.tfidf")

    
    song_tfidf = tfidf[new_test.items()]
    print(song_tfidf)

    tfidf_dict = {}
    for key, value in song_tfidf:
        tfidf_dict[key] = value

    print(tfidf_dict)

    dense = matrix_func([tfidf_dict])
    # ----------------------------------------------------------------
    # load model and get year prediciton and confidence score 

    clf = joblib.load('NB_pickle.pkl')

    year = clf.predict(dense[0].toarray())
    # gets probability of class 
    confidence_score = clf.predict_proba(dense[0].toarray())
    
    print("5" * 50)
    print(year)

    print(confidence_score[0])

    print(confidence_score[0].max())
    print(confidence_score[0][year])
    # load_models()

    Song_BOW.objects.create(
                            bow=tfidf_dict,
                            year=year,
                            confidence=confidence_score[0].max())


# parse_data_predict("Don't turn turn your eyes away And please say that you will stay A while")









