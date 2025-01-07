from flask import Flask, make_response, request, render_template
app = Flask(__name__)
@app.route('/')
def showWelcome():
    return render_template('screen_1.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)