# PÄÄOHJELMA

# KIRJASTOJEN JA MODULIEN LATAUS

# Otetaan käyttöön Windows-äänikirjasto (pythonin sisäänrakennettu kirjasto)
import winsound

# Otetaan käyttöön oma funktiomoduli
import funktiot_moduli

# varsinainen pääohjelma alkaa tästä

# Ikuinen silmukka


while True:
    # Tätä toistetaan kunnes käyttäjä sulkee ohjelman
    mittaustulokset= []
    seina1 = float(input("Anna ensimmäisen seinän pituus: "))
    seina2 = float(input("Anna toisen seinän pituus: "))
    lavistaja = float(input("Anna ristimitta: "))

    mittaustulokset.append(seina1)
    mittaustulokset.append(seina2)
    mittaustulokset.append(lavistaja)


    # Kerrotaan onko tila suorakulmainen
    print("nurkka suorakulmainen", funktiot_moduli.suorakulma(
        seina1, seina2, lavistaja))

    # Kysytään käyttäjältä haluaako jatkaa
    lopetetaan = input("Paina L, jos haluat lopettaa")

    if lopetetaan != "L":
        break

# Ohjelman suoritus päättyy
mittauksia = len(mittaustulokset)
print("Kiitos tästä päivästä", mittauksia, "mittausta")

# Tulostetaan ruudulle kaikki mittaustulokset
print("Päivän mittaukset alla:")
for mittaus in mittaustulokset:
    print(mittaus)
