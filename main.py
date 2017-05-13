
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def main():
    return """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
        <script async defer src="https://buttons.github.io/buttons.js"></script>        

        <body style="padding:3cm">
        <center>
            <h1 class="display-3">The Spam Repository</h1>
            <br/>
            <p class="lead">The official repository of the Spam package manager</p>
            <pre><kbd>$ spam get https://spam-pkg.herokuapp.com/&ltpackage_name&gt</kbd></pre>
            <a class="github-button" href="https://github.com/jwinnie/spam-pkg" data-size="large" data-show-count="true" aria-label="jwinnie/spam-pkg on GitHub">View packages on Github</a>
        </center>
        </body>
    """

@app.route("/<package>")
def get_package(package):
    return send_from_directory("spam", package)
