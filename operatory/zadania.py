"""
Odpal pythona w knsoli i sprzwdz co robia dane operatory ze slajdu 11.
do operatorów bitowych warto użyc reprezentacji bitowej
"""

x = 0b00001
print(bin(x))
print(bin(x<<2))
x = 0b101000
print(bin(x>>2))
print(bin(x^0b00001))
print(bin(x|x))
