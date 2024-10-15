from flask import Flask, render_template, request
import htmlhelper as html
import report

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<user>')
def user(user):
    return html.returnhtml(user)


@app.route('/<user>/report')
def reportuser(user):
    return report.report(user)


if __name__ == '__main__':
    app.run(debug=True)