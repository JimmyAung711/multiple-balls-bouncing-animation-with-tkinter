class Ball:
          def __init__(self,canvas,x,y,diameter,xV,yV,color):
                    self.canvas = canvas
                    self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
                    self.xV = xV
                    self.yV = yV
                    
          def move(self):
                    cords = self.canvas.coords(self.image)
                    print(cords)
                    if (cords[2] >= self.canvas.winfo_width()) or cords[0] < 0:
                              self.xV = -self.xV
                    if (cords[3] >= self.canvas.winfo_height()) or cords[1] < 0:
                              self.yV = -self.yV
                    self.canvas.move(self.image,self.xV,self.yV)