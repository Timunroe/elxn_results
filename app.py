from flask import Flask, render_template, request, url_for, redirect
import model
import fetch
import data

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data.build_template()
        # fetch.put_S3()
    return render_template('index.html', data=model.db)


# [MAIN]-----------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
