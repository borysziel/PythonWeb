from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# bardzo istotny obiekt
Base = declarative_base()

class Kampanie(Base):

    __tablename__ = 'kampanie'

    #Klucz głowny
    id = Column(Integer,primary_key=True)

    data = Column(String)

    id_portalu = Column(Integer, ForeignKey('portale.id'))

    rodzaj_api = Column(String)

    # tworzymy relację - obie klasy odpowiadające tabelom muszą wiedzieć o tej relacji

    ofert = relationship('Oferty', back_populates='kampan')

class Portale(Base):

    __tablename__ = 'portale'

    id = Column(Integer,primary_key=True)

    nazwa_portalu = Column(String)



class Oferty(Base):
    __tablename__ = 'oferty'

    id = Column(Integer, primary_key=True)

    id_kampanii = Column(Integer, ForeignKey('kampanie.id'))
    id_oferty = Column(String)
    id_sprzedajacego = Column(String)

    lokalizacja = Column(String)
    tytul = Column(String)
    cena = Column(String)
    marka = Column(String)
    model = Column(String, nullable=True)
    rok_produkcji = Column(String)
    przebieg = Column(String)
    pojemnosc = Column(String)
    moc = Column(String)
    rodzaj_paliwa = Column(String)
    kolor = Column(String)
    uszkodzony = Column(String)
    kraj = Column(String, nullable=True)
    naped = Column(String)
    liczba_miejsc = Column(String)

    kampan = relationship('Kampanie', back_populates='ofert')
