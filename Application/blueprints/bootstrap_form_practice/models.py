from Application import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Student(db.Model): # type: ignore
    id: Mapped[int] = mapped_column(primary_key=True, init=False)

    fname: Mapped[str] = mapped_column(String(20), nullable=False)
    mname: Mapped[str] = mapped_column(String(20), nullable=False) 
    lname: Mapped[str] = mapped_column(String(20), nullable=False) 
    course: Mapped[str] = mapped_column(String(8), nullable=False)
    gender: Mapped[str] = mapped_column(String(8), nullable=False)
    phone: Mapped[str] = mapped_column(String(10), nullable=False)
    current_address: Mapped[str] = mapped_column(String(300), nullable=False)
    email: Mapped[str] = mapped_column(String(320), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(16), nullable=False)