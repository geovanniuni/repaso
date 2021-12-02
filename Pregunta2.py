class persona:
    
    nombre = None
    edad = None
    dni = None
    
    def __init__(self,nomx,edx,dnx):
        self.nombre = nomx
        self.edad = edx
        self.dni = dnx
        
    def getIdentidad(self):
        print(self.nombre,end=" ")
        print(self.edad,end=" ")
        print(self.dni,end=" ")
    
        

class estudiante(persona):
    idEstudiante= None
    materias = list()
    notasMaterias=list()
    universidad=None

    
    def __init__(self,nomx,edx,dnx,idEstx,uni):
        super().__init__(nomx,edx,dnx)
        self.idEstudiante= idEstx
        self.universidad=uni
    def getMaterias(self):
        return self.materias
    def getNotasMaterias(self):
        return self.notasMaterias  
    def setMaterias(self,materiax,notaMateriax):
        self.materias.append(materiax)
        self.notasMaterias.append(notaMateriax)
    

        
    
class trabajador(persona):
    oficio= None
    universidad=None
    def __init__(self,nomx,edx,dnx,oficiox,uni):
        super().__init__(nomx,edx,dnx)
        self.oficio = oficiox
        self.universidad=uni
        
    def getOficio(self):
        return self.oficio
    def getUniversidad(self):
        return self.universidad
        

class estudiantePregrado(estudiante):
    facultad=None
    
    def __init__(self,nomx,edx,dnx,idEstx,uni,facu):
        super().__init__(nomx,edx,dnx,idEstx,uni)
        self.facultad=facu
    def getFacultad(self):
        return self.facultad


class estudianteDoctorado(estudiante):
    tema_investigacion=None
    
    def __init__(self,nomx,edx,dnx,idEstx,uni,tInvestiga):
        super().__init__(nomx,edx,dnx,idEstx,uni)
        self.facultad=tInvestiga
    def getInvestigacion(self):
        return self.tema_investigacion




class departamento():
    nombre=None
    listaEstudiantesPre=list()
    listaEstudiantesDoc=list()
    listaTrabajadores=list()
    def __init__(self,nomx):
        self.nombre=nomx
    def getNombre(self):
        return self.nombre
    def getEstudiantesPre(self):
        return self.listaEstudiantesPre
    def getEstudiantesDoc(self):
        return self.listaEstudiantesDoc
    def setTrabajadores(self):
        return self.listaTrabajadores

    def setEstudiantesPre(self,estudiante):
        self.listaEstudiantesPre.append(estudiante)
    def setEstudiantesDoc(self,estudiante):
        self.listaEstudiantesDoc.append(estudiante)
    def setTrabajadores(self,trabajador):
        self.listaTrabajadores.append(trabajador)

class universidad():
    nombre=None
    departamentos=list()
    def __init__(self,nomx):
        self.nombre=nomx
    
    def setDepartamento(self,departamentox):
        self.departamentos.append(departamentox)
    def getEstudiantes(self):
        estudiantes=[]
        for i in self.departamentos:
           estudiantes.append(i.getEstudiantesPre())
           estudiantes.append(i.getEstudiantesDoc())
        return estudiantes
    


UNI=universidad("UNI")
L2=departamento("Electronica")
L3=departamento("Telecomunicaciones")
jamil=estudiantePregrado("Jamil",21,"574859","32017",UNI,"FIEE")
miguel=estudiantePregrado("Miguel",34,"343434435","434555",UNI,"fiee")
gustavo=estudiantePregrado("Gustavo",24,"434435","54645",UNI,"fiee")

jamil.getIdentidad()
miguel.getIdentidad()
gustavo.getIdentidad()


juan=estudiantePregrado("Juan",21,"574859","32017",UNI,"FIEE")
percy=estudiantePregrado("Percy",34,"343434435","434555",UNI,"fiee")
eduardo=estudiantePregrado("Eduardo",24,"434435","54645",UNI,"fiee")

diego=estudianteDoctorado("Diego",24,"434435","54645",UNI,"AI")
dante=estudianteDoctorado("Dante",24,"434435","54645",UNI,"Electronica de Potencia")

L2.setEstudiantesPre(juan)
L2.setEstudiantesPre(percy)
L2.setEstudiantesPre(eduardo)

L3.setEstudiantesDoc(jamil)
L3.setEstudiantesDoc(miguel)
L3.setEstudiantesDoc(gustavo)

UNI.setDepartamento(L2)
UNI.setDepartamento(L3)


        