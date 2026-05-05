from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String, unique=True)
    gender = Column(String)
    measurement = relationship("Measurement", back_populates="customer", uselist=False)

class Measurement(Base):
    __tablename__ = "measurement"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    neck = Column(Float)
    shoulder = Column(Float)
    biceps = Column(Float)
    long_sleeves = Column(Float)
    short_sleeves = Column(Float)
    chest = Column(Float)
    waist = Column(Float)
    short_trouser_length = Column(Float)
    long_trouser_length = Column(Float)
    thigh = Column(Float)
    full_body_length = Column(Float)
    burst = Column(Float)
    under_burst = Column(Float)
    half_length = Column(Float)
    hips = Column(Float)
    short_skirt_length = Column(Float)
    long_skirt_length = Column(Float)
    short_gown_length = Column(Float)
    long_gown_length = Column(Float)

    customer = relationship("Customer", back_populates="measurement", uselist=False)