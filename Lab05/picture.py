from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
       vertical = [fila for fila in reversed(self.img)]
       return Picture (vertical)

  def horizontalMirror(self):
      horizontal = [fila[::-1] for fila in self.img]
      return Picture(horizontal)

  def negative(self):
    neg_img = [''.join([self._invColor(char) for char in line]) for line in self.img]
    return Picture(neg_img)

  def join(self, p):
    new_img = []
    for i in range(len(self.img)):
        combined_line = self.img[i] + p.img[i]
        new_img.append(combined_line)
    return Picture(new_img)

  def up(self, p):
    joined_img = self.img + p.img
    return Picture(joined_img)

  def under(self, p):
    combined_img = []
    for line_self, line_p in zip(self.img, p.img):
        combined_line = ''.join(char_p if char_p != ' ' else char_self for char_self, char_p in zip(line_self, line_p))
        combined_img.append(combined_line)
    return Picture(combined_img)
 
  
  def horizontalRepeat(self, n):
       imagen = []
       for line in self.img:  
            repeated_line = line * n
            imagen.append(repeated_line)
       return Picture(imagen)
  
  def verticalRepeat(self, n):
        imagen = []
        for i in range(n):
            imagen.extend(self.img)
        return Picture(imagen)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

