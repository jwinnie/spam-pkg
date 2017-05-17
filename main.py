
import flask

app = flask.Flask(__name__)

@app.route("/")
def main():
    return flask.render_template("index.html")

@app.route("/files/<package>/<file>")
def get_file(package, file):
    return flask.send_from_directory("packages", "{}/{}".format(package, file))

@app.route("/<package>")
def get_package(package):
    return flask.send_from_directory("packages", "{}/spam.toml".format(package))
