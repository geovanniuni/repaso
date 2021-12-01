

class personaje():
    
    bmps = None
    posicion_actual = None
    velocidad = None
    estado= None
    
    def __init__(self,bmps,pos_act,vel,est):
        self.bmps = bmps
        self.posicion_actual = pos_act
        self.velocidad = vel
        self.estado= est
        
    def mover(self):
        nuevaPosicionX= self.posicion_actual[0]+self.velocidad[0]
        nuevaPosicionY= self.posicion_actual[1]+self.velocidad[1]
        nuevaPosicion=(nuevaPosicionX,nuevaPosicionY)
        self.posicion_actual=nuevaPosicion
    def dibujar(self, buf):
        self.bmps=buf
    def cambiar_de_estado(self,nest):
        self.estado=nest
    def detectar_colision(self,personaje2):
        if(personaje2.posicion_actual[0]== self.posicion_actual[0] and personaje2.posicion_actual[1]== self.posicion_actual[1]):
            return True
        return False

     

class vaquero(personaje):
    direccion = None
    pos_destino = None
    
    def __init__(self,bmps,pos_act,vel,est,dir, pos_dest):
        super().__init__(bmps,pos_act,vel,est)
        self.direccion=dir
        self.pos_destino= pos_dest

        
    def getPosicion(self):
        return self.posicion_actual
    def getVelocidad(self):
        return self.velocidad
    def getPos_destino(self):
        return self.pos_destino


class vaca(personaje):
    posicion_inicial=None
    posicion_final=None

    
    def __init__(self,bmps,pos_act,vel,est,pos_inicial,pos_final):
        super().__init__(bmps,pos_act,vel,est)
        self.posicion_inicial=pos_inicial
        self.posicion_final=pos_final

    #TO DO#    
    def getPosInicial(self):
        return self.posicion_inicial
    def getPosFinal(self):
        return self.posicion_final

class cerca():
    posicion_inicial=None
    posicion_final=None

    def __init__(self,pos_inicial,pos_final):
        self.posicion_inicial=pos_inicial
        self.posicion_final=pos_final

    def crear(self, posiciones):
        self.posicion_inicial=posiciones[0]
        self.posicion_final=posiciones[1]
    
    def getPosInicial(self):
        return self.posicion_inicial
    def getPosFinal(self):
        return self.posicion_final

    
    

class juego:
    nivel= None
    puntuacion= None
    cerca_dsiponible=None
    vaquero= None
    listaVacas=None
    cerca=None
    def __init__(self,niv,cerc_disp,vaquerox,cercax, listVacas=[]):
        self.nivel=niv
        self.cerca_dsiponible=cerc_disp
        self.vaquero=vaquerox
        self.cerca=cercax
        self.listaVacas=listVacas


    def getPuntuacion(self):
        return self.puntuacion
    def setVaca(self,objVaca):
        self.listaVacas.append(objVaca)
    
    def setCerca(self,objCerca):
        self.cercax=objCerca


