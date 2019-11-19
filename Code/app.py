from flask import Flask
from sample import stochastic_sampling
from dictionary_words import open_file
import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from markov_chain import markov_chain, get_pairs, generate_sentences

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/urlshortener')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
tweets = db.tweets


app = Flask(__name__)

words = open_file('story.txt')

@app.route('/')
def index():
    return generate_sentences(markov_chain(get_pairs(words)), 20)



# @aoo.route('/save')
# def saved_tweets():
#     pass

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
