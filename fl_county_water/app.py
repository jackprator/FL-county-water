from flask import Flask, g, render_template
import sqlite3

app = Flask(__name__)
application = app

def connect_db():
    sql = sqlite3.connect('database/florida_county.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    #Check if DB is there
    if not hasattr(g, 'sqlite3'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

# first route

@app.route('/')
def index():
    db = get_db()
    cursor = db.execute('SELECT id, county, tot_wells, tot_over, pct_bad, n_ppm, trend, facts, url FROM fl_county')
    results = cursor.fetchall()
    pairs_list = []
    for p in results:
        pairs_list.append( (p['id'], p['county']) )
    return render_template('index.html', pairs=pairs_list, the_title="County Index")

# second route

@app.route('/county/<num>')
def detail(num):
    try:
        county_dict = result[int(num) - 1]
    except:
        return f"<h1>Invalid value for county: {num}</h1>"


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
