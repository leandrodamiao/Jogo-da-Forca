def enforcado(arg):
  match arg:
    case 0:
      print("""
_______
       |

      
      
      """)
    case 1:
      print("""
_______
       |
       O
      
      
      """)
  
    case 2:
      print("""
_______
       |
       O
       |
      
      """)
    case 3:
      print("""
_______
       |
       O
      /|
      
      """)
    case 4:
      print("""
_______
       |
       O
      /|\\
    
      """)
      
    case 5:
      print("""
_______
       |
       O
      /|\\
      /
           """)
      
    case _:
      print("""
\033[31m_______
       |
       O
      /|\\
      / \\
            \033[m""")
  

