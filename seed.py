from app import db
from models import Pet

db.drop_all()
db.create_all()

p = Pet(name = 'Pocky', species="dog", available = True, photo_url='https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*')
p2 = Pet(name='Whisky', species='cat', available=False, photo_url='https://hips.hearstapps.com/hmg-prod/images/beautiful-smooth-haired-red-cat-lies-on-the-sofa-royalty-free-image-1678488026.jpg?crop=0.88847xw:1xh;center,top&resize=1200:*')
db.session.add(p)
db.session.add(p2)
db.session.commit()