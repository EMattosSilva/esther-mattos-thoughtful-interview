
from sort_packages import sort

"""
main.py
Author: Esther de Mattos

This script provides an interactive way to test the package sorting function.
It prompts the user for package dimensions and mass, then classifies the package
as STANDARD, SPECIAL, or REJECTED according to the rules defined in sort_packages.py.
"""

def main():
	"""
	Prompts the user for package dimensions and mass, calls the sort function,
	and prints the classification result.
	"""
	print("Package sort function test")
	width = float(input("Enter width (cm): "))
	height = float(input("Enter height (cm): "))
	length = float(input("Enter length (cm): "))
	mass = float(input("Enter mass (kg): "))
	result = sort(width, height, length, mass)
	print(f"Result: {result}")

if __name__ == "__main__":
	main()

