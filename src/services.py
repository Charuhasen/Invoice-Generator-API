import database.database as _database
import sqlalchemy.orm as _orm, models.invoice_model as _model
import schemas.invoice_schema as _schemas
from sqlalchemy import extract, func


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close

def create_invoice(db: _orm.Session, invoice: _schemas.Invoice):
    db_invoice = _model.Invoice(
        invoice_id = invoice.invoice_id,
        to_customer = invoice.to_customer,
        suppliers_tin = invoice.suppliers_tin,
        date_of_supply = invoice.date_of_supply,
        customer_tin = invoice.customer_tin,
        date_of_invoice = invoice.date_of_invoice,
        quantity_one = invoice.quantity_one,
        description_one = invoice.description_one,
        unit_price_one = invoice.unit_price_one,
        quantity_two = invoice.quantity_two,
        description_two = invoice.description_two,
        unit_price_two = invoice.unit_price_two,
        quantity_three = invoice.quantity_three, 
        description_three = invoice.description_three,
        unit_price_three = invoice.unit_price_three,
        quantity_four = invoice.quantity_four,
        description_four = invoice.description_four,
        unit_price_four = invoice.unit_price_four,
        quantity_five = invoice.quantity_five,
        description_five = invoice.description_five,
        unit_price_five = invoice.unit_price_five,
        terms_of_payment = invoice.terms_of_payment,
    )
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_all_invoice(db: _orm.Session, skip:int):
    return db.query(_model.Invoice).offset(skip).all()

def get_invoices_by_year_month(db: _orm.Session, year: int = None, month: int = None, skip: int = 0):
    query = db.query(_model.Invoice)

    if year is not None:
        query = query.filter(extract('year', _model.Invoice.date_of_invoice) == year)

    if month is not None:
        query = query.filter(extract('month', _model.Invoice.date_of_invoice) == month)

    query = query.offset(skip)

    invoices = query.all()
    return invoices

def get_invoices_by_customer(db: _orm.Session, to_customer: str, skip: int = 0):

    query = db.query(_model.Invoice).filter(func.lower(_model.Invoice.to_customer).ilike(func.lower(f"%{to_customer}%")))

    query = query.offset(skip)

    invoices = query.all()
    return invoices