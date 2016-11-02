from models import Song_BOW



# need to import dict of words 
# also need to include trained NB model and tfidf model here 

# ******* really just need to build a class that takes a paragraph and breaks it down to word 
# counts in the format we need 



def parse_data_predict(data):
    parsed_data = data
    year = 1983

    Song_BOW.objects.create(
                            bow=parsed_data,
                            year=year)