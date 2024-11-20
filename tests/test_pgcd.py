# test_math_utils.py

from src.my_arithmetic_tvalenti.pgcd import pgcd

def test_pgcd():
    assert pgcd(8, 12) == 4
    assert pgcd(25, 10) == 5 
    assert pgcd(17, 13) == 1 

    assert pgcd(-8, 12) == 4
    assert pgcd(8, -12) == 4
    assert pgcd(-8, -12) == 4
    
    assert pgcd(0, 10) == 10
    assert pgcd(10, 0) == 10
    assert pgcd(0, 0) == 0 
