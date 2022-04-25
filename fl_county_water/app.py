from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField

app = Flask(__name__)
application = app

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'ihopethisworks'

db_name = 'florida_county.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

class Water(db.Model):
    __tablename__ = 'fl_county'
    id =  db.Column(db.Integer, primary_key=True)
    county =  db.Column(db.String)
    tot_wells = db.Column(db.Integer)
    tot_over = db.Column(db.String)
    pct_bad = db.Column(db.String)
    n_ppm = db.Column(db.Integer)
    trend = db.Column(db.String)
    facts = db.Column(db.String)
    url = db.Column(db.String)
    photo = db.Column(db.String)

class CountyForm(FlaskForm):
    dropdown = SelectField('Choose a county:',
    choices=[ (1, 'Alachua County'), (2, 'Baker County'),(3, 'Bay County'),(4, 'Bradford County'),(5, 'Brevard County'),(6, 'Broward County'),(7, 'Calhoun County'),(8, 'Charlotte County'),(9, 'Citrus County'),(10, 'Clay County'),(11, 'Collier County'),(12, 'Columbia County'),(13, 'Miami-Dade County'),(14, 'DeSoto County'),(15, 'Dixie County'),(16, 'Duval County'),(17, 'Escambia County'),(18, 'Flagler County'),(19, 'Franklin County'),(20, 'Gadsden County'),(21, 'Gilchrist County'),(22, 'Glades County'),(23, 'Gulf County'),(24, 'Hamilton County'),(25, 'Hardee County'),(26, 'Hendry County'),(27, 'Hernando County'),(28, 'Highlands County'),(29, 'Hillsborough County'),(30, 'Holmes County'),(31, 'Indian River County'),(32, 'Jackson County'),(33, 'Jefferson County'),(34, 'Lafayette County'),(35, 'Lake County'),(36, 'Lee County'),(37, 'Leon County'),(38, 'Levy County'),(39, 'Liberty County'),(40, 'Madison County'),(41, 'Manatee County'),(42, 'Marion County'),(43, 'Martin County '),(44, 'Monroe County'),(45, 'Nassau County'),(46, 'Okaloosa County'),(47, 'Okeechobee County'),(48, 'Orange County'),(49, 'Osceola County '),(50, 'Palm Beach County'),(51, 'Pasco County'),(52, 'Pinellas County'),(53, 'Polk County'),(54, 'Putnam County'),(55, 'St. Johns County'),(56, 'St. Lucie County'),(57, 'Santa Rosa County'),(58, 'Sarasota County'),(59, 'Seminole County'),(60, 'Sumter County'),(61, 'Suwannee County'), (62, 'Taylor County'),(63, 'Union County'),(64, 'Volusia County'),(65, 'Wakulla County'),(66, 'Walton County'),(67, 'Washington County') ])



# first route

@app.route('/')
def index():
    a = Water.query.order_by(Water.id)

    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = CountyForm()
    if form.validate_on_submit():
        # redirect the browser to another route and template
        return redirect( url_for('county', id=id) )

    return render_template('index.html', a=a, the_title="Water Index")

# second route

@app.route('/county/<id>')
def county(id):
    a = Water.query.get_or_404(id)

    return render_template('county.html', a=a, id=id, the_title=a.id)

# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
