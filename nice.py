#from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Home Page</title>
      </head>
      <body>
        <p>Hi! This is the home page.</p>
        <a href="http://127.0.0.1:5000/hello">Hello Page</a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <div>
            <label>What's your name? <input type="text" name="person"></label>
          </div>
          <div>
            <label>Select a compliment: 
              <input type="radio" name="AWESOMENESS" value="awesome">Awesome
              <input type="radio" name="AWESOMENESS" value="ducky">Ducky
              <input type="radio" name="AWESOMENESS" value="oh-not-so-meh">Oh not so meh...
            </label>
            </div>
            <input type="submit">
        </form>
        <form action="/diss">
          <div>
            <label>Select a diss: 
              <input type="radio" name="INSULT" value="terrible">Terrible
              <input type="radio" name="INSULT" value="stinky">Stinky
              <input type="radio" name="INSULT" value="oh-so-meh">Oh so meh...
            </label>
          </div>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("AWESOMENESS")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
