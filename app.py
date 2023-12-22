from flask import Flask, render_template, flash, redirect
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pets"

app.app_context().push()
connect_db(app)


@app.route('/')
def index():
    all_pets = Pet.query.all()
    return render_template('home.html', pets=all_pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        print('valid')
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species,photo_url=photo_url, age=age, notes = notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form = form)
    
@app.route('/<int:pet_id>', methods = ['GET','POST'])
def pet_page(pet_id):
    curr_pet = Pet.query.get(pet_id)
    form = EditPetForm(obj = curr_pet)
    if form.validate_on_submit():
        curr_pet.name = form.name.data
        curr_pet.species = form.species.data
        curr_pet.photo_url = form.photo_url.data
        curr_pet.age = form.age.data
        curr_pet.notes = form.notes.data
        curr_pet.available = form.available.data
        db.session.commit()
        flash(f"Pet {pet_id} updated!")
        return redirect(f"/{pet_id}")

    return render_template('pet_page.html', pet = curr_pet, form = form )


    