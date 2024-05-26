from interpreter import draw
from chessPictures import *

caballo = knight
negro = knight.negative()
caballo1 = caballo.join(negro)
invcaballo = knight.horizontalMirror()
invcaballonegro = negro.horizontalMirror()
caballo2 =  invcaballonegro.join(invcaballo)
ambos = caballo1.up(caballo2) 
draw(ambos)