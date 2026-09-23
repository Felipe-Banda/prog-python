# Importações e Instância Base
from fastapi import FastAPI, HTTPException

## Instanciando o aplicativo FastAPI
app = FastAPI()

## Rota Raiz (Boas-vindas)
@app.get('/')
def mensagem_boas_vindas():
    return{'mensagem': 'Bem-vindo à API Calculadora!'}

## Rota de Soma
@app.get('/somar/{a}/{b}')
def somar(a:float, b: float):
    resultado = a + b
    return {'operação': 'soma', 'resultado': resultado}

## Rota Subtração
@app.get('/subtrair/{a}/{b}')
def subtrair(a: float, b: float):
    resultado = a - b
    return {'operação': 'subtração', 'resultado': resultado}

## Rota Multiplicação
@app.get('/multiplicar/{a}/{b}')
def multiplicar(a: float, b: float):
    resultado = a * b
    return {'operação': 'multiplicação', 'resultado': resultado}

## Rota Divisão
@app.get('/dividir')
def dividir(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail='Não é possível dividir por zero.')
    resultado = a / b
    return {'operação': 'divisão', 'resultado': resultado}

