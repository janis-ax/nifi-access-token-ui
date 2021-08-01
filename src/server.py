from flask import render_template, request, jsonify, make_response, Flask

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('index.html')


@app.route("/ping", methods=["POST"])
def ping():
    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "OK"}), 200)

    return res

app.run(debug=True, port=5005)