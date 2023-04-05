import random
response="y"
loop = 0
while(response=="y"):
  no=random.randint(1,6)
  print(no)
  if no==1:
      print("[-----]")
      print("[     ]")
      print("[  0  ]")
      print("[     ]")
      print("[-----]")
  elif no==2:
      print("[-----]")
      print("[    0]")
      print("[  0  ]")
      print("[     ]")
      print("[-----]") 
  elif no==3:
      print("[-----]")
      print("[    0]")
      print("[  0  ]")
      print("[0    ]")
      print("[-----]") 
  elif no==4:
      print("[-----]")
      print("[0   0]")
      print("[     ]")
      print("[0   0]")
      print("[-----]") 
  else:
      print("[-----]")
      print("[0 0 0]")
      print("[     ]")
      print("[0 0 0]")
      print("[-----]")

  
  response=str(input("Do you want to roll a dice (y/n)"))


