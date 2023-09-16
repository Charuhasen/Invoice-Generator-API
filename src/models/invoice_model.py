import database.database as _database
import sqlalchemy.orm as _orm
import sqlalchemy as _sql
import datetime as _dt

class Invoice(_database.Base):
    __tablename__ = "invoices"
    
    invoice_id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    to_customer = _sql.Column(_sql.String, index=True)
    suppliers_tin = _sql.Column(_sql.String)
    date_of_supply = _sql.Column(_sql.DateTime, index=True, default=_dt.datetime.utcnow)
    customer_tin = _sql.Column(_sql.String)
    date_of_invoice = _sql.Column(_sql.DateTime, index=True, default=_dt.datetime.utcnow)
    quantity_one = _sql.Column(_sql.Integer)
    description_one = _sql.Column(_sql.String)
    unit_price_one = _sql.Column(_sql.Float)
    quantity_two = _sql.Column(_sql.Integer)
    description_two = _sql.Column(_sql.String)
    unit_price_two = _sql.Column(_sql.Float)
    quantity_three = _sql.Column(_sql.Integer)
    description_three = _sql.Column(_sql.String)
    unit_price_three = _sql.Column(_sql.Float)
    quantity_four = _sql.Column(_sql.Integer)
    description_four = _sql.Column(_sql.String)
    unit_price_four = _sql.Column(_sql.Float)
    quantity_five = _sql.Column(_sql.Integer)
    description_five = _sql.Column(_sql.String)
    unit_price_five = _sql.Column(_sql.Float)
    terms_of_payment = _sql.Column(_sql.String)