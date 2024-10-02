  def make_bricks(small, big, goal):
  #start counts at 0
  inches = int(0)
  bigsUsed = int(0)
  
  while goal > inches and big > bigsUsed and big != 0:
    inches += 5
    bigsUsed += 1
    
    print("afterloop")
    print("goal: " + str(goal))
    print("inches: " + str(inches))
    print("bigsUsed: " + str(bigsUsed) + "\n")

  
  if inches > goal:
    inches -= 5
    bigsUsed -= 1
    print("bigsUsedFINAL " + str(bigsUsed) + "\n")
  else:
    placeHeld = 1
    print("bigsUsedFINAL " + str(bigsUsed) + "\n")
  
  if goal - bigsUsed*5 <= small:
    print("inches: " + str(inches))
    print("bigsUsed: " + str(bigsUsed))
    print("goal - bigsUsed*5= " + str(goal - bigsUsed*5))
    print("True")
  else:
    print("inches: " + str(inches))
    print("bigsUsed: " + str(bigsUsed))
    print("False")

make_bricks(4, 20, 39)

'''
def make_bricks(small, big, goal):
  #start counts at 0
  inches = int(0)
  bigsUsed = int(0)
  
  while goal > inches and big > bigsUsed and big != 0:
    inches += 5
    bigsUsed += 1

  if inches > goal:
    inches -= 5
    bigsUsed -= 1
  else:
    placeHeld = 1
  
  if goal - bigsUsed*5 <= small:
    return True
  else:
    return False
    
'''


'''make_bricks(3, 1, 8) → True	
make_bricks(3, 1, 9) → False		
make_bricks(3, 2, 10) → True	
make_bricks(3, 2, 8) → True		
make_bricks(3, 2, 9) → False		
make_bricks(6, 1, 11) → True		
make_bricks(6, 0, 11) → False		
make_bricks(1, 4, 11) → True	
make_bricks(0, 3, 10) → True	
make_bricks(1, 4, 12) → False		
make_bricks(3, 1, 7) → True	
make_bricks(1, 1, 7) → False	
make_bricks(2, 1, 7) → True		
make_bricks(7, 1, 11) → True	
make_bricks(7, 1, 8) → True		
make_bricks(7, 1, 13) → False		
make_bricks(43, 1, 46) → True		
make_bricks(40, 1, 46) → False	
make_bricks(40, 2, 47) → True	
make_bricks(40, 2, 50) → True	
make_bricks(40, 2, 52) → False		
make_bricks(22, 2, 33) → False		
make_bricks(0, 2, 10) → True	
make_bricks(1000000, 1000, 1000100) → True	
make_bricks(2, 1000000, 100003) → False	
make_bricks(20, 0, 19) → True		
make_bricks(20, 0, 21) → False	
make_bricks(20, 4, 51) → False	
make_bricks(20, 4, 39) → True	
other tests
'''