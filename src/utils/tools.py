import cv2 as cv
import os
from qiskit.visualization import plot_histogram


def fname(path):
    return path.split('/')[-1]


def qdraw(circuit):
    circuit.draw(filename='./res/qdraw.png', output='mpl')
    render('./res/qdraw.png')


def qhist(counts):
    img = plot_histogram(counts)
    img.savefig('./res/qhist.png')
    render('./res/qhist.png')


def render(path):
    img = cv.imread(path)
    cv.imshow(fname(path), img)
    cv.waitKey(-1)
