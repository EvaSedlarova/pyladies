# Naprogramuj jednoduchou webovou aplikaci pomocí frameworku Flask.
# Aplikace bude mít dva endpointy. První bude home page s uvítáním a návodem,
# co může uživatel na stránkách najít. Druhý bude poskytovat informace podle zadaného klíče.

# Endpoint, který bude poskytovat data musí mít dynamickou URL.
# Místo <username> bude tvůj endpoint přijímat argument např. jméno, autor básně, obdarovaný.
# Uvnitř něj si otevřeš a načteš soubor s JSONem. Soubor nezapomeň otevírat pomocí
# with open(.... Obsah souboru si nahraješ do pythonního slovníku pomocí json.loads.
# Podle zadaného klíče vybereš potřebné hodnoty ze slovníku a vrátíš je.

# Po nahrání JSONu se tvoje data budou chovat jako klasický pythonní slovník
# a jak vybírat ze slovníku podle klíče už známe.

# Nezapomeň ošetřit situaci, kdy uživatel zadá klíč, který nebude ve slovníku.
# To můžeš vyřešit nějakou hezkou hláškou. Pokud si troufneš, můžeš uživateli pomocí Flaskové funkce abort vrátit stavový kód 404 - nenalezeno.
# Dokumentaci k abort můžeš najít tady: https://flask.palletsprojects.com/en/1.1.x/api/#flask.abort


from flask import Flask, abort
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return 'Hello everybody!\nHere you can find some stuff'

@app.route('/<key>/')
def dictionary(key):    
    with open('homework.txt') as file_:
        data = json.loads(file_.read())
        if key in data:
            return key + ': ' + data[key]
        else:
            return abort(404)

if __name__ == "__main__":
    app.run()