Web VPython 3.2
box(texture =  "https://i.postimg.cc/zvCnYX5j/sr27b890af2ad78.png")
sphere(pos = vec(0.3,0.5,-1), color = color.yellow, radius = 0.05)

b = box(size = vec(0.1,-0.1,1), color = color.yellow, radius =0.05)
while True :
   rate(100)
   k = keysdown()
   if 'left'in k :
      b.pos.x = b.pos.x - 000.1
   if'right'in k :
      b.pos.x = b.pos.x + 000.1
   if'up'in k :  
      b.pos.y = b.pos.y + 000.1
   if'down'in k :      
      b.pos.y = b.pos.y - 000.1 
