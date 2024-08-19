from pydantic import BaseModel


class NatalData(BaseModel):
    day: str
    month: str
    year: str
    hour: str
    minute: str
    city: str


class CompatibilityData(BaseModel):
    f_day: str
    f_month: str
    f_year: str
    m_day: str
    m_month: str
    m_year: str
