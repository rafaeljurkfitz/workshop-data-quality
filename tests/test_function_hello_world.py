from app.funcao import funcao_hello_world

def test_funcao_hello_world():
    exit = funcao_hello_world()
    template = "Hello World!"
    assert exit == template