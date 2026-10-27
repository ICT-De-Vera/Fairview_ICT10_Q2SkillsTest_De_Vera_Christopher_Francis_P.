from pyscript import display, document

Non_metals = {
    "H": ("hydrogen", 1, 1.008),
    "C": ("carbon", 6, 12.011),
    "N": ("nitrogen", 7, 14.007),
    "O": ("oxygen", 8, 15.999),
    "P": ("phosphorus", 15, 30.974),
    "S": ("sulfur", 16, 32.065),
    "Se": ("selenium", 34, 78.971),
    "F": ("fluorine", 9, 18.998),
    "Cl": ("chlorine", 17, 35.453),
    "Br": ("bromine", 35, 79.904),
    "I": ("iodine", 53, 126.904),
    "At": ("astatine", 85, 210),
    "Ts": ("tennessine", 117, 294),
    "He": ("helium", 2, 4.0026),
    "Ne": ("neon", 10, 20.1797),
    "Ar": ("argon", 18, 39.948),
    "Kr": ("krypton", 36, 83.798),
    "Xe": ("xenon", 54, 131.293),
    "Rn": ("radon", 86, 222),
    "Og": ("oganesson", 118, 294)
}

def lookupelement():
    symbol = document.getElementById("elementInput").value.strip()
    name, atomic_number, atomic_mass = Non_metals.get(
        symbol, ("Unknown element", "N/A", "N/A")
    )

    display(f"Element: {name}", target="elementName")
    display(f"Atomic Number: {atomic_number}", target="atomicNumber")
    display(f"Atomic Mass: {atomic_mass}", target="atomicMass")
    display(f"Symbol: {symbol}", target="elementSymbol")

    
