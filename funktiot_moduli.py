# X-funktio tarkistaa onko kulma suora

def suorakulma(sivuA, sivuB, lavistaja):
    """Tarkistaa suorakulmaisuuden käyttäen Pythagoraan lausetta
    Args:
        sivuA (float): Ensimmäisen pituus
        sivuB (float): Toisen pituus
        lavistaja (float): Lävistäjän pituus
    Returns:
        boolean: TRUE -> suorakulma
    """
    A_nelio = sivuA * sivuA
    B_nelio = sivuB * sivuB
    l_nelio = lavistaja * lavistaja

    if A_nelio + B_nelio == l_nelio:
        suora = True
    else:
        suora = False
    return suora

# Testataan, että toimii, poista tämä myöhemmin
if __name__ == "__main__":
   vastaus = suorakulma(3, 4, 5)
print(vastaus)

vastaus = suorakulma(3, 4, 6)
print(vastaus)

