import os
from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query
import googlemaps

try:
    from my_config import API_KEY
except ImportError:
    API_KEY = os.environ.get('API_KEY')

gmaps = googlemaps.Client(key=API_KEY)
db = TinyDB('db/db.json')
parks_db = TinyDB("db/parks.json")
# {"_default": {"1": {"type": "name"}}}
# for item in db:
#     print(item)

app = Flask(__name__)
def create_id():
    return len(db.all())+1

@app.route("/")
def index():
    return render_template("Home Page.html")

@app.route("/lost_found") ## telling the URL of the project, connect button to that link
def lost_found():
    pets = db.all()
    return render_template("lstnfnd.html", pets=pets, API_KEY=API_KEY)

@app.route("/lost_pet/", methods=["GET", "POST"])
def lost_pet():
    if request.method == 'POST':
        # collect information from request.form (using the names
        # attributes from your inputs) and create a database entry;
        # then google "URL redirect"

        db.insert({
            "id":create_id(),
            "name":request.form["name"],
            "address":request.form["address"],
            "info":request.form["info"],
            "contact":request.form["contact"],
            "date":request.form["date"],
            "coord":gmaps.geocode(request.form["address"])[0]["geometry"]["location"]
        })
        return redirect(url_for("lost_found"))
    return render_template("lostpet.html")

@app.route("/lost_pet/<int:pet_id>")
def pet_info(pet_id):
    Pet = Query()
    pet = db.search(Pet.id == pet_id)[0]
    return render_template("pet_info.html", pet=pet)

# @app.route("/petlost/<string:petname>/")
# def pet_info():
#    return render_template("Lost pet information")

# @app.route("/petfound/<string:petname>/")
# def found_pet():
#    return render_template("Yay you found the pet")

@app.route("/parks_beaches")
def parks_beaches():
    parks=parks_db.all()
    return render_template("parks_beaches.html", parks=parks, API_KEY=API_KEY)

@app.route("/about_us")
def about_us():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run()
