clase  Personaje :

    def  __init__ ( self , nombre , fuerza , inteligencia , defensa , vida ):
        ser . nombre  =  nombre
        ser . fuerza  =  fuerza
        ser . inteligencia  =  inteligencia
        ser . defensa  =  defensa
        ser . vida  =  vida

    def  atributos ( uno mismo ):
        print ( self.nombre , " : " , sep = "" )
        print ( " ·Fuerza: " , self.fuerza )
        print ( "·Inteligencia:" , self . inteligencia )
        print ( "·Defensa:" , self . defensa )
        print ( "·Vida: " , self .vida )

    def  subir_nivel ( self , fuerza , inteligencia , defensa ):
        ser . fuerza  =  yo . fuerza  +  fuerza
        ser . inteligencia  =  yo . inteligencia  +  inteligencia
        ser . defensa  =  yo . defensa  +  defensa

    def  esta_vivo ( auto ):
        regresar  a uno mismo . vida  >  0

    def  morir ( yo ):
        ser . vida  =  0
        imprimir ( self . nombre , "ha muerto" )

    def  daño ( yo , enemigo ):
        regresar  a uno mismo . fuerza  -  enemigo . defensa

    def  atacar ( yo , enemigo ):
        daño  =  yo . daño ( enemigo )
        enemigo . vida  =  enemigo . vida  -  daño
        print ( self . nombre , "ha realizado" , daño , "puntos de daño a" , enemigo . nombre )
        si  enemigo . esta_vivo ():
            print ( "Vida de" , enemigo . nombre , "es" , enemigo . vida )
        demás :
            enemigo . morir ()


clase  Guerrero ( Personaje ):

    def  __init__ ( self , nombre , fuerza , inteligencia , defensa , vida , espada ):
        súper (). __init__ ( nombre , fuerza , inteligencia , defensa , vida )
        ser . espada  =  espada

    def  cambiar_arma ( auto ):
        opcion  =  int ( input ( "Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10" ))
        si  opción  ==  1 :
            ser . espada  =  8
         opción  elif ==  2 :
            ser . espada  =  10
        demás :
            print ( "Número de arma incorrecta" )

    def  atributos ( uno mismo ):
        súper (). atributos ()
        print ( "·Espada:" , self . espada )

    def  daño ( yo , enemigo ):
        regresar  a uno mismo . fuerza  *  yo . espada  -  enemigo . defensa


clase  Mago ( Personaje ):

    def  __init__ ( self , nombre , fuerza , inteligencia , defensa , vida , libro ):
        súper (). __init__ ( nombre , fuerza , inteligencia , defensa , vida )
        ser . libro  =  libro

    def  atributos ( uno mismo ):
        súper (). atributos ()
        print ( "·Libro: " , self .libro )

    def  daño ( yo , enemigo ):
        regresar  a uno mismo . inteligencia  *  yo . libro  -  enemigo . defensa


def  combate ( jugador_1 , jugador_2 ):
    turno  =  0
    mientras  jugador_1 . esta_vivo () y  jugador_2 . esta_vivo ():
        imprimir ( " \nTurno " , turno )
        print ( ">>> Acción de " , jugador_1 . nombre , ":" , sep = "" )
        jugador_1 . atacar ( jugador_2 )
        print ( ">>> Acción de " , jugador_2 . nombre , ":" , sep = "" )
        jugador_2 . atacar ( jugador_1 )
        turno  =  turno  +  1
    si  jugador_1 . esta_vivo ():
        print ( " \n Ha ganado" , jugador_1 . nombre )
    elif  jugador_2 . esta_vivo ():
        print ( " \n Ha ganado" , jugador_2 . nombre )
    demás :
        imprimir ( " \n Empate" )


personaje_1  =  Guerrero ( "agallas" , 20 , 10 , 4 , 100 , 4 )
personaje_2  =  Mago ( "Vanessa" , 5 , 15 , 4 , 100 , 3 )

personaje_1 . atributos ()
personaje_2 . atributos ()

combate ( personaje_1 , personaje_2 )
