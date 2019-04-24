PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE kampanie(id integer primary key autoincrement not null, data text, foreign key (id_portalu) references portale(id), rodzaj_api text);
CREATE TABLE portale(id integer primary key autoincrement not null, nazwa_portalu text);
CREATE TABLE oferty(id integer primary key autoincrement not null, foreign key (id_kampanii) references kampanie(id), \
id_oferty integer not null, id_sprzedajacego integer not null, lokalizacja text, tytul text, cena text, marka text, model text,\
rok_produkcji text, przebieg text, pojemnosc text, moc text, rodzaj_paliwa text, kolor text, uszkodzony text, kraj text, naped, text, liczba_miejsc integer not null);
COMMIT;