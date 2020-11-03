# -*- coding: utf-8 -*-


def foreing_exchange_calculator(ammount):
    mex_to_col_rate=145.97
    return mex_to_col_rate*ammount


def run():
    print("Calculadora de divisas")
    print("Convierte pesos mexicanos a pesos colombianos ")
    print("")

    ammount =float(input("Ingrese la cantidad de pesos mexicanos que quieres convertir "))
    
    resutl= foreing_exchange_calculator(ammount)

    tmp ="${} pesos mexicanos son ${} pesos colombianos ".format(ammount, resutl)
    print (tmp)
    print("${} pesos mexicanos son ${} pesos colombianos ".format(ammount, resutl))
    print("")


if __name__ == "__main__":
    run()