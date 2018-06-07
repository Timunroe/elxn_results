from flask import Flask, render_template, request, url_for, redirect
import model
import fetch
import data
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['action'] == 'fetch_cp':
            db = model.get_api()
            return render_template('index.html', data=db)
        if request.form['action'] == 'deploy_cp':
            # read file cp.db
            with open('cp.db') as json_data:
                db = json.load(json_data)
            data.build_template(db)
            fetch.put_S3()
            return render_template('index.html', data=db)
        if request.form['action'] == 'fetch_manual':
            return render_template('index.html', data=model.db)
        if request.form['action'] == 'deploy_manual':
            data.build_template(model.db)
            fetch.put_S3()
            return render_template('index.html', data=model.db)
    return render_template('index.html', data=model.db)


# [MAIN]-----------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
