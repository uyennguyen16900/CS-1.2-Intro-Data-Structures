from flask import Flask
from histogram import histogram_dictionary
from sample import stochastic_sampling
import dictionary_words

app = Flask(__name__)

histogram = histogram_dictionary('story.txt')

@app.route('/')
def hello_world():
    sentences = []
    for _ in range(10):
        sentences.append(stochastic_sampling(histogram))
    return " ".join(sentences)

if __name__ == "__main__":
    app.run(debug=True)
