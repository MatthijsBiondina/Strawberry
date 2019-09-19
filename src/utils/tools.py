import cv2 as cv
import os
from qiskit.visualization import plot_histogram


def qdraw(circuit):
    circuit.draw(filename='./res/qdraw.png', output='mpl')
    img = cv.imread('./res/qdraw.png')
    cv.imshow("CIRCUIT", img)
    cv.waitKey(-1)


def qhist(counts):
    img = plot_histogram(counts)
    print(img)
