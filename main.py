from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def find_most_common_word():
    if request.method == 'POST':
        file = request.files['file']
        text = file.read().decode('utf-8')
        words = text.split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        most_common_word = max(word_count, key=word_count.get)
        count = word_count[most_common_word]
        return render_template('result.html', most_common_word=most_common_word, count=count)

if __name__ == '__main__':
    app.run(debug=True)