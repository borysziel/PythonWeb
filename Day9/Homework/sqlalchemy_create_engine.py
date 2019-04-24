
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from offer_models import Base

# wskazanie gdzie tworzymy bazę
engine = create_engine('sqlite:///offers_mass.db')

# utworzenie struktury
Base.metadata.create_all(engine)

# utworzenie obiektu sesji
Session = sessionmaker(bind=engine)
2