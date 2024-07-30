from flask import Blueprint, request, jsonify
from app import db
from app.models import Booking, Inventory
from app.auth import auth

api = Blueprint('api', __name__)

@api.route('/inventory/checklist', methods=['GET'])
def get_inventory():
    inventories = Inventory.query.all()
    result = [{'home_type': inv.home_type, 'item_name': inv.item_name} for inv in inventories]
    return jsonify(result)

@api.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    user_id = data.get('user_id')
    quote = data.get('quote')
    details = data.get('details')
    
    new_booking = Booking(user_id=user_id, quote=quote, details=details)
    db.session.add(new_booking)
    db.session.commit()
    
    return jsonify({'message': 'Booking created'}), 201

@api.route('/bookings/<int:id>', methods=['GET'])
def get_booking(id):
    booking = Booking.query.get(id)
    if not booking:
        return jsonify({'message': 'Booking not found'}), 404
    
    return jsonify({
        'id': booking.id,
        'user_id': booking.user_id,
        'quote': booking.quote,
        'status': booking.status,
        'details': booking.details
    })
