from flask import Flask, render_template
from modules.markov import SecondOrderMarkovChain
from modules.dictionary_words import open_file
app = Flask(__name__)


corpus = SecondOrderMarkovChain('modules/dan-brown.txt', 20)

@app.route('/')
def index():
    # sentence = SecondOrderMarkovChain(corpus, 20)
    sentence = corpus.generate_sentences()
    return render_template('index.html', sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True)
