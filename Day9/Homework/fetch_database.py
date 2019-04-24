from sqlalchemy.sql import func
from sqlalchemy_create_engine import Session



def database_statistics():
    from offer_models import Kampanie, Portale,Oferty

    session = Session()
    offerNumber = session.query(func.count(Oferty.id)).one()
    print(offerNumber)
    return offerNumber

def database_cost():
    from offer_models import Kampanie, Portale,Oferty

    session = Session()
    minPrice = session.query(func.min(Oferty.cena)).one()
    maxPrice = session.query(func.max(Oferty.cena)).one()
    minMilage = session.query(func.min(Oferty.przebieg)).one()
    maxMilage = session.query(func.max(Oferty.przebieg)).one()

    print("Min value: " , minPrice[0])
    print("Max value: " , maxPrice[0])
    print("Min milage: " , minMilage[0])
    print("Max milage: " , maxMilage[0])

    return ''

if __name__ == '__main__':
    database_cost()
    database_statistics()