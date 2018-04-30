from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User


engine = create_engine('sqlite:///transportitemswithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Shiva", email="dgpshiva@gmail.com",
             picture='./shiva.jpg')
session.add(User1)
session.commit()

# Items for Bikes
Category1 = Category(user_id=1, name="Bikes")

session.add(Category1)
session.commit()

item1 = Item(user_id=1, name="Apache RTR", description="One of the best two wheelers in its class!",
                     capacity="2", fuelType="Petrol", mileage="45 kmpl", maxSpeed="148", price="1240$", category=Category1)

session.add(item1)
session.commit()


print "added items!"
