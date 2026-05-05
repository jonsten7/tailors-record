from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, session, get_db
from schema import CustomerBase, CustomerResponse, CustomerUpdate
import models

app = FastAPI()

origins = [
    "*",  # Allow your Angular app's origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Welcome to Tailor's Record"}

@app.get("/customers", response_model=list[CustomerResponse])
def get_all_customers(db: Session = Depends(get_db)):
    customers = db.query(models.Customer).all()
    return customers

@app.post("/customers", response_model=CustomerResponse)
def add_customer(customer: CustomerBase, db: Session = Depends(get_db)):
    new_customer = models.Customer(
        name=customer.name,
        phone=customer.phone,
        gender=customer.gender,
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    new_measurement = models.Measurement(**customer.measurement.model_dump(), customer_id=new_customer.id)
    db.add(new_measurement)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@app.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.get(models.Customer, customer_id)
    if not customer:
        return {"message": "Customer not found"}
    else:
        return customer

@app.put("/customers/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    selected_customer = db.get(models.Customer, customer_id)
    if not selected_customer:
        return {"message": "Customer not found"}

    selected_customer.name = customer.name
    selected_customer.phone = customer.phone

    measurement = selected_customer.measurement
    if measurement:
        for key, value in customer.measurement.model_dump().items():
            setattr(measurement, key, value)
    db.commit()
    db.refresh(selected_customer)
    return selected_customer

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.get(models.Customer, customer_id)
    db.delete(customer)
    db.commit()
    return