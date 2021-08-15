from flask import *


# from flask import Flask
app = Flask(__name__)


# from flask import Flask
@app.route('/')
def index():
    return '/'


# from flask import Flask
@app.route('/path')
def path():
    return '/path'


# from flask import Flask
@app.route('/url/<int:id>')
# float / int / path / string / uuid
def url(id=None):
    return '/url/{}'.format(id)


# from flask import Flask, request
@app.route('/query')
def query():
    name = request.args.get('name')
    return '/query?name={}'.format(name)


# from flask import Flask, request
@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        name = request.form['name']
    return '/post {{ "name": "{}" }}'.format(name)


# from flask import Flask, render_template
@app.route('/post', methods=['GET'])
def post_form():
    return render_template('post.html')

# from flask import Flask, render_template
# ./templates/***.html を作成
@app.route('/template')
def template():
    return render_template(
        'index.html',
        title='12345',
        html_contents='<h1>HTML Contents</h1>',
        text_contents='<h1>TEXT Contents</h1>',
        dict_items={'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
    )


# from flask import Flask, jsonify
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False
@app.route("/json")
def json():
    return jsonify({"name": "foo"}), 200


# from flask import Flask, redirect
@app.route('/redirect/302')
def redirect302():
    return redirect('https://www.google.com')

@app.route('/redirect/200')
def redirect200():
    return redirect('https://www.google.com', code=200)


# from flask import redirect, url_for
@app.route('/redirect/for')
def redirect_func():
    return redirect(url_for('url', id='789'))


if __name__ == "__main__":
    app.run(debug=True)