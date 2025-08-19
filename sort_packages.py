"""
sort_packages.py
Author: Esther de Mattos

This module provides the sort function to classify packages as STANDARD, SPECIAL, or REJECTED
based on their dimensions and mass.

Rules:
- A package is bulky if its volume (width x height x length) is greater than or equal to 1,000,000 cm³
  or if any dimension is greater than or equal to 150 cm.
- A package is heavy if its mass is greater than or equal to 20 kg.
- Classification:
    - SPECIAL: Bulky or heavy
    - REJECTED: Bulky and heavy
    - STANDARD: Otherwise
"""

def sort(width, height, length, mass):
    """
    Classifies a package as STANDARD, SPECIAL, or REJECTED based on its dimensions and mass.

    Args:
        width (float): Width of the package in centimeters.
        height (float): Height of the package in centimeters.
        length (float): Length of the package in centimeters.
        mass (float): Mass of the package in kilograms.

    Returns:
        str: The classification of the package ('STANDARD', 'SPECIAL', or 'REJECTED').
    """
    isBulky = False
    if ( width >= 150 or height >= 150 or length >= 150 ) or (width * height * length) >= 1000000:
        isBulky = True
    if isBulky or mass >= 20:
        return "SPECIAL"
    elif isBulky and mass >= 20:
        return "REJECTED"
    else:
        return "STANDARD"
    