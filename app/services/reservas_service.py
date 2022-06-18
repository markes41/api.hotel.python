from models.reserva import Reserva
from mkapp import db
from sqlalchemy import and_
from models.habitacion import Habitacion

class Reservas_Service:
    def obtener_habitaciones_reservadas(id):
        return Reserva.query.filter(Reserva.id_habitacion == id).all()

    def obtener_reserva_by_id(id):
        return Reserva.query.get(id)
    
    def agregar_reserva(reserva):
        db.session.add(reserva)
        db.session.commit()
        return True
    
    def obtener_reservas_by_fecha(fecha_desde, fecha_hasta):
        return Reserva.query.join(Habitacion).filter(
            and_(Reserva.fecha_desde >= fecha_desde, Reserva.fecha_hasta <= fecha_hasta)
        ).all()
        
    def obtener_reservas(fecha):
        return Reserva.query.filter(
            and_(fecha >= Reserva.fecha_desde , fecha  <= Reserva.fecha_hasta)
        ).all()