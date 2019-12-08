from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def index():

    """Tato funce se zavolá, když uživatel přijde
    na domovskou stránku naší aplikace.
    Vrátí řetězec, který se zobrazí v prohlížeči.
    """
    return 'Ahoj Pyladies!'

@app.route('/url/')
def show_url():
    return url_for('profile', username = 'pylady')

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name = None):    
    return render_template('hello.html', name = name)

@app.route('/user/<username>/')
def profile(username):
    
    return 'User {}'.format(username)    

if __name__ == "__main__":
    # spustí aplikaci
    app.run()