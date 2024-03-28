from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def handle_requests():
    return render_template('html/index.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)