from settings import *
import json

db = SQLAlchemy(app)


class Units(db.Model):
    __tablename__ = 'units_and_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)

    def to_json(self):
        return {
            'id': self.id, 
            'name': self.name,
            'type': self.type
            }

    def add_unit(_name, _type):
        new_unit = Units(name=_name, type=_type)
        db.session.add(new_unit)
        db.session.commit()

    def get_units():
        return [Units.to_json(_unit) for _unit in Units.query.all()]

    def get_unit_id(_id):
        if Units.query.filter_by(id=_id).first() != None :
            return [Units.to_json(Units.query.filter_by(id=_id).first())]
        else:
            return []

    def get_unit_name(_name):
        if Units.query.filter_by(name=_name).first() != None :
            return [Units.to_json(Units.query.filter_by(name=_name).first())]
        else:
            return []

    def update_unit(_id, _name, _type):
        unit_update = Units.query.filter_by(id=_id).first()
        unit_update.name = _name
        unit_update.type = _type
        db.session.commit()

    def delete_unit_id(_id):
        Units.query.filter_by(id=_id).delete()
        db.session.commit()
    
    def delete_unit_name(_name):
        Units.query.filter_by(name=_name).delete()
        db.session.commit()

class Conversions(db.Model):
    __tablename__ = 'conversion_units'
    id = db.Column(db.Integer, primary_key=True)
    unit1 = db.Column(db.String(80), nullable=False)
    unit2 = db.Column(db.String(80), nullable=False)
    ratio = db.Column(db.Float, nullable=False)

    def to_json(self):
        return {
            'id': self.id, 
            'unit1': self.unit1,
            'unit2': self.unit2,
            'ratio': self.ratio
            }

    def add_conversion(_unit1, _unit2, _ratio):
        new_conversion = Conversions(unit1=_unit1, unit2=_unit2, ratio=_ratio)
        db.session.add(new_conversion)
        db.session.commit()

    def get_conversions():
        return [Conversions.to_json(_conversion) for _conversion in Conversions.query.all()]

    def get_conversion_id(_id):
        if Conversions.query.filter_by(id=_id).first() != None :
            return [Conversions.to_json(Conversions.query.filter_by(id=_id).first())]
        else:
            return []

    def get_conversion_units(_unit1, _unit2):
        if Conversions.query.filter_by(unit1=_unit1, unit2=_unit2).first() != None :
            return [Conversions.to_json(Conversions.query.filter_by(unit1=_unit1, unit2=_unit2).first())]
        elif Conversions.query.filter_by(unit1=_unit2, unit2=_unit1).first() != None :
            return [Conversions.to_json(Conversions.query.filter_by(unit1=_unit2, unit2=_unit1).first())]
        else:
            return []

    def update_conversion(_id, _unit1, _unit2, _ratio):

        conversion_update = Conversions.query.filter_by(id=_id).first()
        conversion_update.unit1 = _unit1
        conversion_update.unit2 = _unit2
        conversion_update.ratio = _ratio
        db.session.commit()

    def delete_conversion_id(_id):
        Conversions.query.filter_by(id=_id).delete()
        db.session.commit()
    
    def delete_conversion_units(_unit1, _unit2):
        Conversions.query.filter_by(unit1=_unit1, unit2=_unit2).delete()
        db.session.commit()



