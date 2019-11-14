from flask import Flask
from histogram import Histogram
from sample import stochastic_sampling
import dictionary_words
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/urlshortener')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
tweets = db.tweets


app = Flask(__name__)

histogram = Histogram('story.txt').histogram_dictionary()

@app.route('/')
def index():
    sentences = []
    for _ in range(10):
        sentences.append(stochastic_sampling(histogram))
    return " ".join(sentences)

@aoo.route('/save')
def saved_tweets():
    pass

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
