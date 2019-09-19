import cv2 as cv
import os


def qdraw(circuit):
    try:
        os.mkdir('./res')
    except FileExistsError:
        pass
    circuit.draw(filename='./res/qdraw.png')
    img = cv.imread('./res/qdraw.png')
    cv.imshow("CIRCUIT", img)
    cv.waitkey(-1)
