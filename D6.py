#!/usr/bin/env python

#This is my attempt to create a Dice Rolling program to use in absence of having the real thing
# Print statement fixed from print(" )" to print(" ")

import random                                   #Moved to the top of the program for aesthetics
endprogram=0
number=random.randint(1,6)

while endprogram != "q":

print("Welcome to eDice")                       #Changed indentation of print statements
print("Press the Enter Key to Roll the D6")
input()

  if number == 1:                               #Fixed indentation (syntax) error
      print("[----------]")
      print("[          ]")
      print("[    0     ]")
      print("[          ]")
      print("[----------]")
      print()
      Print("Type 'q' to Quit")
      endprogram=input()
  if number==2:
       print("[----------]")
       print("[          ]")
       print("[  0   0   ]")
       print("[          ]")
       print("[----------]")
       print()
       print("Type 'q' to Quit")
       endprogram=input()
  if number==3:
       print("[----------]")
       print("[  0       ]")
       print("[     0    ]")
       print("[        0 ]")
       print("[----------]")
       print()
       print("Type 'q' to Quit")
       endprogram=input()
  if number==4:
       print("[----------]")
       print("[  0    0  ]")
       print("[          ]")
       print("[  0    0  ]")
       print("[----------]")
       print()
       print("Type 'q' to Quit")
       endprogram=input()
  if number==5:
       print("[----------]")
       print("[  0     0 ]")
       print("[     0    ]")
       print("[  0     0 ]")
       print("[----------]")
       print()
       print("Type 'q' to Quit")
       endprogram=input()
  if number==6:
       print("[----------]")
       print("[  0    0  ]")
       print("[  0    0  ]")
       print("[  0    0  ]")
       print("[----------]")
       print()
       print("Type 'q' to Quit")
       endprogram=input()
      
    
    
    
    
    
    
    
    
    
    
    
    
