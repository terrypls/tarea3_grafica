import matplotlib.pyplot as plt


class Grafico(object):
    def __init__(self):
        self.yo = None

    def graficar(self, datos):
        largo_x = [x for x in range(len(datos))]
        vivos = []
        muertos = []
        enfermos = []
        for data in datos:
            enfermos.append(data[0])
            vivos.append(data[1])
            muertos.append(data[2])

        fig, ax = plt.subplots()
        ax.plot(largo_x, enfermos, label="enfermos")
        ax.plot(largo_x, vivos, label="sanos")
        ax.plot(largo_x, muertos, label="muertos")
        ax.set_xlabel('Dias pasados')  # Add an x-label to the axes.
        ax.set_ylabel('Cantidad de individuos')  # Add a y-label to the axes.
        ax.set_title("Gráfico simulación")  # Add a title to the axes.
        ax.legend()  # Add a legend.
        plt.show()
