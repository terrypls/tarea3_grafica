import matplotlib.pyplot as plt


class Grafico(object):
    def __init__(self, poblacion):
        self.poblacion = poblacion

    def graficar(self, datos):
        largo_x = [x for x in range(len(datos))]
        vivos = []
        muertos = []
        enfermos = []
        for data in datos:
            enfermos.append(data[0])
            vivos.append(data[1])
            muertos.append(data[2])

        print((vivos))
        print(muertos)
        print(enfermos)

        fig, ax = plt.subplots()
        ax.plot(largo_x, enfermos, label="enfermos")
        ax.plot(largo_x, vivos, label="sanos")
        ax.plot(largo_x, muertos, label="muertos")
        ax.set_xlabel('x label')  # Add an x-label to the axes.
        ax.set_ylabel('y label')  # Add a y-label to the axes.
        ax.set_title("Simple Plot")  # Add a title to the axes.
        ax.legend()  # Add a legend.
        plt.show()