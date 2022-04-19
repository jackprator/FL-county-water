from flask import Flask, g, render_template
import sqlite3



def connect_db():
    sql = sqlite3.connect('database/florida_county.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    #Check if DB is there
    if not hasattr(g, 'sqlite3'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

def idk():
    db = get_db()
    cursor = db.execute('SELECT id, county, tot_wells, tot_over, pct_bad, n_ppm, trend, facts, url FROM fl_county')
    #results.clear() in case results is not var only in func
    results = cursor.fetchall()
    pairs_list = []
    for p in results:
        pairs_list.append( (p['id'], p['county']) )
    return pairs_list

# first route


@app.route('/')
def index():

    for p in pairs:
        print(p)
    return render_template('index.html', pairs, the_title="County Index")

# second route

@app.route('/county/<num>')
def detail(num):
    try:
        county_dict = results[int(num) - 1]
    except:
        return f"<h1>Invalid value for county: {num}</h1>"

def create_app():
    app = Flask(__name__)

    with app.app_context():
        connect_db()
        get_db()
        idk()
        index()
        detail(num)
    return app
# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
