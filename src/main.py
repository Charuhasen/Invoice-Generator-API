import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import Annotated, List
from pydantic import BaseModel
import services as _services
import schemas.invoice_schema as _schemas

app = _fastapi.FastAPI()

_services.create_database()


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.post("/create-invoice/", response_model=_schemas.Invoice)
async def create_invoice(
    invoice: _schemas.Invoice, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    return _services.create_invoice(db=db, invoice=invoice)


@app.get("/get-all-invoice/", response_model=List[_schemas.Invoice])
async def get_invoice(
    skip: int = 0,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    db_invoices = _services.get_all_invoice(db=db, skip=skip)

    if db_invoices is None:
        raise _fastapi.HTTPException(status_code=404, detail="No Invoices")

    return db_invoices

@app.get("/get-invoice-by-month-year/", response_model=List[_schemas.Invoice])
async def get_invoice_by_month_year(
    month: int,
    year: int,
    skip: int = 0,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    db_invoices = _services.get_invoices_by_year_month(db=db, skip=skip, month=month, year=year)

    if db_invoices is None:
        raise _fastapi.HTTPException(status_code=404, detail="No Invoices")

    return db_invoices

@app.get("/get-invoice-by-customer/", response_model=List[_schemas.Invoice])
async def get_invoice_by_month_year(
    customer_name : str,
    skip: int = 0,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    db_invoices = _services.get_invoices_by_customer(db=db, to_customer=customer_name)

    if db_invoices is None:
        raise _fastapi.HTTPException(status_code=404, detail="No Invoices")
    
    return db_invoices
