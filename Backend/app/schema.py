from pydantic import BaseModel
from typing import Optional

class MeasurementBase(BaseModel):
    neck: Optional[float] = None
    shoulder: Optional[float] = None
    biceps: Optional[float] = None
    long_sleeves: Optional[float] = None
    short_sleeves: Optional[float] = None
    chest: Optional[float] = None
    waist: Optional[float] = None
    short_trouser_length: Optional[float] = None
    long_trouser_length: Optional[float] = None
    thigh: Optional[float] = None
    full_body_length: Optional[float] = None
    burst: Optional[float] = None
    under_burst: Optional[float] = None
    half_length: Optional[float] = None
    hips: Optional[float] = None
    short_skirt_length: Optional[float] = None
    long_skirt_length: Optional[float] = None
    short_gown_length: Optional[float] = None
    long_gown_length: Optional[float] = None

class CustomerBase(BaseModel):
    name: str
    phone: str
    gender: str
    measurement: MeasurementBase

class MeasurementResponse(MeasurementBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class CustomerResponse(BaseModel):
    id: int
    name: str
    phone: str
    gender: str
    measurement: Optional[MeasurementResponse]

    model_config = {
        "from_attributes": True
    }

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    gender: Optional[str] = None
    measurement: Optional[MeasurementBase] = None
