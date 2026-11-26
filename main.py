Web VPython 3.2
box(texture =  "https://i.postimg.cc/zvCnYX5j/sr27b890af2ad78.png")



b = sphere (size = vec(0.1,0.1,0.1), color = color.yellow, radius =0.05)
while True :
   rate(100)
   k = keysdown()
   if 'left'in k :
      b.pos.x = b.pos.x - 0.003
   if'right'in k :
      b.pos.x = b.pos.x + 0.003
   if'up'in k :  
      b.pos.y = b.pos.y + 0.003
   if'down'in k :      
      b.pos.y = b.pos.y - 0.003 
   if 'w' in k:
        b.pos.z += 0.01
   if 's' in k:
        b.pos.z -= 0.01
