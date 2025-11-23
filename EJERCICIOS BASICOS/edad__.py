ed=int(input("Proporciona tu edad: "))
match ed:
    case ed if ed>=1 and ed<=12:
        print("Usted es un niño")
        
    case ed if ed<=13 and ed<=18:
        print("Usted es un adolescente")
        
    case ed if ed>=19 and ed<=25:
        print("Usted es un joven")
        
    case ed if ed>=26 and ed<=59:
        print("Usted es un adulto")
        
    case ed if ed>=60:
        print("Usted es de la tercera edad")
