from flask import render_template, request, jsonify, make_response, Flask
# import nipyapi
import dotenv

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

@app.route("/token", methods=["POST"])
def token():
    pass
    # nipyapi.security.set_service_ssl_context
    # nipyapi.security.service_login()


if __name__ == "__main__":
    ca_path = "/Users/janisax/git/nifi-environment/certs"
    app.run(debug=True, port=5005)