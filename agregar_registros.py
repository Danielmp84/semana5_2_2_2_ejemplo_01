from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import Ciudad
from crear_entidades import Estadio
# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()

# se crea un objetos de tipo Ciudad Estadio

Ciudad1 = Ciudad(nombreCiudad="Portoviejo", pais="Ecuador", poblacion=244129)
Ciudad2 = Ciudad(nombreCiudad="Manta", pais="Ecuador", poblacion=258697)
Ciudad3 = Ciudad(nombreCiudad="Chone", pais="Ecuador", poblacion=54629)

Estadio1 = Estadio(nombreEstadio="RealesTamarindos", direccionEstadio="Portoviejo", capacidad="15691")
Estadio2 = Estadio(nombreEstadio="RealesJocay", direccionEstadio="Manta", capacidad="22000")
Estadio3 = Estadio(nombreEstadio="RealesChonanas", direccionEstadio="Chone", capacidad="3000")


# se agrega los objetos de tipo Ciudad Estadio a la sesión
# a la espera de un commit
session.add(Ciudad1)
session.add(Ciudad2)
session.add(Ciudad3)
session.add(Estadio1)
session.add(Estadio2)
session.add(Estadio3)

# se necesita confirmar los cambios que existan en la sessió
# se usar commit
session.commit()
