import random

def funcion_abc(x):
    a,b,c=1,1,1
    def operacion(x,a,b,c):
        discriminante=a*x*x+b*x+c
        if(discriminante==0 ):
            return 'valor:a= {} valor:b= {} valor c= {}'.format(a,b,c)
        else:
          
            return operacion(x,a=random.randint(-10,10),b=random.randint(-10,10),c=random.randint(-10,10)) 
    
    return operacion(x,a,b,c)


x=6

if(funcion_abc(x)):
    print(funcion_abc(x))
    
else:
    print("volver a intentar")

        