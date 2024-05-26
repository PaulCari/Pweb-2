from interpreter import draw
from chessPictures import *

par = square.join(square.negative())
linea = par.horizontalRepeat(4)
draw(linea.negative())