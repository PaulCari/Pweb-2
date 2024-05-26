from interpreter import draw
from chessPictures import *
caballo = Picture(KNIGHT)
negro = caballo.negative()
caballo1 = caballo.join(negro)
caballo2 = negro.join(caballo)
ambos = caballo1.up(caballo2)
draw(ambos)
