from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Car

@app.route('/')
def index():
    cars = Car.query.order_by(Car.created_at.desc()).all()
    return render_template('index.html', cars=cars)

@app.route('/add', methods=['POST'])
def add_car():
    make = request.form.get('make')
    model = request.form.get('model')
    plate_number = request.form.get('plate_number')
    owner_name = request.form.get('owner_name')
    
    if not all([make, model, plate_number, owner_name]):
        flash('All fields are required!', 'danger')
        return redirect(url_for('index'))
    
    new_car = Car(make=make, model=model, plate_number=plate_number, owner_name=owner_name)
    try:
        db.session.add(new_car)
        db.session.commit()
        flash('Car added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding car: {str(e)}', 'danger')
        
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_status(id):
    car = Car.query.get_or_404(id)
    new_status = request.form.get('status')
    if new_status in ['Pending', 'In Progress', 'Ready']:
        try:
            car.status = new_status
            db.session.commit()
            flash(f'Status updated for {car.plate_number}', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating status: {str(e)}', 'danger')
    else:
        flash('Invalid status value provided.', 'warning')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_car(id):
    car = Car.query.get_or_404(id)
    try:
        db.session.delete(car)
        db.session.commit()
        flash('Car removed from system', 'info')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting car: {str(e)}', 'danger')
    return redirect(url_for('index'))

