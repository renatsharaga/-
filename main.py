from fastapi import FastAPI


app = FastAPI()

@app.post("/calculator/{pervoe}/{vtoroe}/{znack}")
def calculator(pervoe: str, vtoroe: str, znack: str):
    return prim(pervoe,  vtoroe, znack)







def prim(pervoe, vtoroe, znack):
    if znack == "+":
        return plus(pervoe, vtoroe)
    if znack == "-":
        return minus(pervoe, vtoroe)
    if znack == ":":
        return delenie(pervoe, vtoroe)
    if znack == "*":
        return mnosh(pervoe, vtoroe)
    return "Ошибка"







def delenie(a, b):
    if b == "0":
        return "Делить на ноль нельзя"
    return int(a) / int(b)
def mnosh(a, b):
    return int(a) * int(b)
def minus(a, b):
    return int(a) - int(b)
def plus(a, b):
    return int(a) + int(b)