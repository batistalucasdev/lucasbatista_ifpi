from app import soma

def test_soma():
    # Teste 1: soma de números positivos
    assert soma(2, 3) == 5
    
    # Teste 2: soma envolvendo zero
    assert soma(0, 5) == 5
    
    # Teste 3: soma de números negativos
    assert soma(-1, -2) == -3
