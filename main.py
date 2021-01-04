from grafico import Grafico
from poblacion import Poblacion


def main():
    poblacion = Poblacion()
    poblacion.crearIndividuos()
    for i in range(10):
        poblacion.cadenaDeContagios()
        poblacion.recuperados()
        poblacion.crearEstadistica()
    print(poblacion.getEstadisticas())
    grafico = Grafico(poblacion.getPoblacion)
    grafico.graficar(poblacion.getEstadisticas())


if __name__ == "__main__":
    main()
