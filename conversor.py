#!/usr/bin/env python3


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Valor inválido. Digite um número.")


def conversao_metricas():
    print("(1) m -> km")
    print("(2) km -> m")

    while True:
        try:
            opcao = int(input("> "))
        except ValueError:
            print("Opção incorreta")
            continue

        if opcao == 1:
            metros = read_float("m = ")
            print(f"km = {metros / 1000}")
            return

        if opcao == 2:
            quilometros = read_float("km = ")
            print(f"m = {quilometros * 1000}")
            return

        print("Opção incorreta")


def conversao_volumetricas():
    print("(1) L -> mL")
    print("(2) mL -> L")

    while True:
        try:
            opcao = int(input("> "))
        except ValueError:
            print("Opção incorreta")
            continue

        if opcao == 1:
            litros = read_float("L = ")
            print(f"mL = {litros * 1000}")
            return

        if opcao == 2:
            mililitros = read_float("mL = ")
            print(f"L = {mililitros / 1000}")
            return

        print("Opção incorreta")


def main():
    print("Converter\n")
    print("(1) Unidades metricas")
    print("(2) Unidades volumetricas")

    while True:
        try:
            opcao = int(input("> "))
        except ValueError:
            print("Opção incorreta")
            continue

        if opcao == 1:
            conversao_metricas()
            return

        if opcao == 2:
            conversao_volumetricas()
            return

        print("Opção incorreta")


if __name__ == "__main__":
    main()
