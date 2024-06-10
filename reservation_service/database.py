reservations_db = []

def add_reservation(reservation):
    reservations_db.append(reservation)

def update_reservation(reservation_id, updated_data):
    for reservation in reservations_db:
        if reservation['id'] == reservation_id:
            reservation.update(updated_data)
            return reservation
    return None

def delete_reservation(reservation_id):
    global reservations_db
    reservations_db = [reservation for reservation in reservations_db if reservation['id'] != reservation_id]

def get_all_reservations():
    return reservations_db

def get_reservation(reservation_id):
    for reservation in reservations_db:
        if reservation['id'] == reservation_id:
            return reservation
    return None
