import pygame as pg
from figura_class import Pelota,Raqueta

pg.init()

pantalla_principal = pg.display.set_mode( (800,600) )
pg.display.set_caption("Pong")
#definir tasa de refresco en nuestro bucle de fotogramas, fps= fotograma por segundos
tasa_refresco= pg.time.Clock()

#creamos un objeto de la clase Pelota o instanciamos la clase pelota
pelota = Pelota(400,300,(228, 231, 19),15)

raqueta1 = Raqueta(0 ,300 )#raqueta izquierda
raqueta2 = Raqueta(780,300 )#raqueta derecha

game_over = True

while game_over:
    #obtener la tasa de refresco en milisegundos
    valor_tasa = tasa_refresco.tick(350)#variable para controlar la velocidad entre fotogramas
    #print(valor_tasa)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = False


    pantalla_principal.fill( ( 27, 149, 47 ) )
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=10)
    
    raqueta1.dibujar(pantalla_principal) 
    raqueta2.dibujar(pantalla_principal)
    pelota.dibujar(pantalla_principal)
    
    raqueta1.mover(pg.K_w,pg.K_s)
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    pelota.mover()

    #logica de choque
    #raqueta derecha
    if pelota.derecha >= raqueta2.izquierda and\
        pelota.izquierda <= raqueta2.derecha and\
        pelota.abajo >= raqueta2.arriba and\
        pelota.arriba <= raqueta2.abajo            :
            pelota.vx *= -1

    if pelota.derecha >= raqueta1.izquierda and\
        pelota.izquierda <= raqueta1.derecha and\
        pelota.abajo >= raqueta1.arriba and\
        pelota.arriba <= raqueta1.abajo            :
            pelota.vx *= -1

    pelota.mostrar_marcador(pantalla_principal)

    pg.display.flip()

pg.quit()

