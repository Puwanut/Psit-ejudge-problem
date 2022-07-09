"""Additive"""
import math as m
def main():
    """find answer with math module"""
    print((m.sin(m.radians(90))+m.sin(m.radians(60))**2) / \
    (m.cos(m.radians(245**2))+m.cos(m.radians(180))))
    print((m.factorial(16)*m.factorial(4))/m.factorial(8))
    print(40/m.sqrt(13**2+(-3)**2))
    print(m.log10(1234**4))
    print((m.log(4234, 5)+m.log(8191, 2)+71*m.log10(156154))/\
    (m.log(777, 7)-m.log(888, 8)-m.log(999, 9)))
main()
