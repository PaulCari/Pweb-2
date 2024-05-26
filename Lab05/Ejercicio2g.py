from interpreter import draw
from chessPictures import *

par = square.join(square.negative())
linea = par.horizontalRepeat(4)
negativa = linea.negative()
cuadro = linea.up(negativa)

parte1 = square.negative().under(rock).join(square.under(knight))
parte2 = square.negative().under(bishop).join(square.under(queen))
parte3 = square.negative().under(king).join(square.under(bishop))
parte4 = square.negative().under(knight).join(square.under(rock))

fila1 = parte1.join(parte2).join(parte3).join(parte4)
invfila1 = fila1.negative()
peones = square.under(pawn).join(square.negative().under(pawn))
filapeones = peones.horizontalRepeat(4)
peonesnegros = filapeones.negative()

tablero1 = invfila1.up(peonesnegros)
tablero2 = cuadro.verticalRepeat(2)
tablero3 = filapeones.up(fila1)

completo = tablero1.up(tablero2).up(tablero3)

draw(completo)