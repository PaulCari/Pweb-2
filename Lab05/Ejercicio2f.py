from interpreter import draw
from chessPictures import *

par = square.join(square.negative())
linea = par.horizontalRepeat(4)
negativa = linea.negative()
cuadro = linea.up(negativa)
draw(cuadro.verticalRepeat(2))