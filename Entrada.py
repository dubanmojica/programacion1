{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOllbyxjlqO8W7tYtGtNENc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dubanmojica/programacion1/blob/main/Entrada.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "LwQJJWkXvDj2"
      },
      "outputs": [],
      "source": [
        "def validar_numero(mensaje):\n",
        "    while True:\n",
        "        try:\n",
        "            valor = float(input(mensaje))\n",
        "            return valor\n",
        "        except ValueError:\n",
        "            print(\"Error: Debe ingresar un número válido.\")\n",
        "\n",
        "def ingresar_matriz():\n",
        "    print(\"\\n--- Configuración de Matriz ---\")\n",
        "    filas = int(validar_numero(\"Ingrese el número de filas: \"))\n",
        "    columnas = int(validar_numero(\"Ingrese el número de columnas: \"))\n",
        "\n",
        "    matriz = []\n",
        "    for i in range(filas):\n",
        "        fila = []\n",
        "        for j in range(columnas):\n",
        "            elemento = validar_numero(f\"Elemento [{i+1}][{j+1}]: \")\n",
        "            fila.append(elemento)\n",
        "        matriz.append(fila)\n",
        "    return matriz\n",
        "\n",
        "def mostrar_matriz(matriz):\n",
        "    if matriz is None:\n",
        "        return\n",
        "    for fila in matriz:\n",
        "        print(\"[\", end=\" \")\n",
        "        for elemento in fila:\n",
        "            print(f\"{elemento:8.2f}\", end=\" \")\n",
        "        print(\"]\")"
      ]
    }
  ]
}