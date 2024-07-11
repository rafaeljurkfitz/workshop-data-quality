import pandas as pd

from app.etl import load_settings, transformar


def test_config_env():
    settings = load_settings()
    
    assert settings["db_host"] is not None and settings["db_host"] != "", "db_host is missing or empty"
    assert settings["db_user"] is not None and settings["db_user"] != "", "db_user is missing or empty"
    assert settings["db_pass"] is not None and settings["db_pass"] != "", "db_pass is missing or empty"
    assert settings["db_name"] is not None and settings["db_name"] != "", "db_name is missing or empty"
    assert settings["db_port"] is not None and settings["db_port"] != "", "db_port is missing or empty"

def test_calculo_valor_total_estoque():
    # Preparação
    df = pd.DataFrame({
        'quantidade': [10, 5],
        'preco': [20.0, 100.0],
        'categoria': ['brinquedos', 'eletrônicos']
    })
    expected = pd.Series([200.0, 500.0], name='valor_total_estoque')

    # Ação
    result = transformar(df)

    # Verificação
    pd.testing.assert_series_equal(result['valor_total_estoque'], expected)

def test_normalizacao_categoria():
    # Preparação
    df = pd.DataFrame({
        'quantidade': [1, 2],
        'preco': [10.0, 20.0],
        'categoria': ['brinquedos', 'eletrônicos']
    })
    expected = pd.Series(['BRINQUEDOS', 'ELETRÔNICOS'], name='categoria_normalizada')

    # Ação
    result = transformar(df)

    # Verificação
    pd.testing.assert_series_equal(result['categoria_normalizada'], expected)

def test_determinacao_disponibilidade():
    # Preparação
    df = pd.DataFrame({
        'quantidade': [0, 2],
        'preco': [10.0, 20.0],
        'categoria': ['brinquedos', 'eletrônicos']
    })
    expected = pd.Series([False, True], name='disponibilidade')

    # Ação
    result = transformar(df)

    # Verificação
    pd.testing.assert_series_equal(result['disponibilidade'], expected)

# Para rodar os testes, execute `pytest nome_do_arquivo.py` no terminal.