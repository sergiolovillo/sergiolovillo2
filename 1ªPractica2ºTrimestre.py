class Alumno:
    'Clase base común para todos los alumnos'
    totalAlum = 0

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        Alumno.totalAlum += 1

    def totalAlumnos(self):
        print ("Total de alumnos %d" % Alumno.totalAlum)

    def caracAlumnos(self):
        print ("Nombre: ", self.nombre,  ", Apellido: ", self.apellido ", Edad: ", self.edad)


"Esto creará el primer objeto de la clase Alumno."
alum1 = Alumno("Antonio", "Blazquez", 25)
"Esto creará el segundo objeto de la clase Alumno."
alum2 = Alumno("Ana", "Mata", 21)
alum1.caracAlumnos()
alum2.caracAlumnos()
print ("Total de alumnos %d" % Alumno.totalAlum)
