from flask import Flask, render_template, redirect, request, flash
from models import db, connect_db, Pet
from forms import AddPet, EditPet

app = Flask(__name__)
app.config['SECRET_KEY'] = "petsarecooliguessbutwhatabouthumans"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


#routes for the pet shop:

@app.route('/')
def homepage():
    """displays all pets with availability"""
    petList = Pet.query.all()
    return render_template('main.html',pets = petList)


@app.route('/add', methods = ['GET','POST'])
def addPet():
    """either validates and adds a new pet through post, or displays the form to add new pet"""
    form = AddPet(available = True)

    if form.validate_on_submit():
        newName = form.name.data
        newSpecies = form.species.data
        newAge = form.age.data
        note = form.notes.data
        newPic = form.photo_url.data
        availablequery = form.available.data

        newPet = Pet(name=newName,species=newSpecies,age=newAge,notes=note,photo_url=newPic,available=availablequery)
        db.session.add(newPet)
        db.session.commit()
        return redirect('/')

    return render_template('add_pet.html', form = form)


@app.route('/<petID>', methods = ['GET','POST'])
def petRoute(petID):
    """shows an individual pet's info. Post allows to edit the values allowed from EditPet"""
    thisPet = Pet.query.get_or_404(petID)
    form = EditPet(obj = thisPet)
    
    if form.validate_on_submit():
        thisPet.photo_url = form.photo_url.data
        thisPet.notes = form.notes.data
        thisPet.available = form.available.data
        db.session.commit()
        return redirect(f"/{petID}")

    return render_template('pet_view.html', pet = thisPet, form = form)
