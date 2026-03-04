import uuid
from utils.db import db

class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    
    
    """
    Funcion init redundante, util para agregar validaciones
    Ejemplo: 
            self.name = name.strip().title()  # Limpia y capitaliza
            self.email = email.strip().lower()  # Limpia y convierte a minúsculas
            self.phone = phone.strip()  # Limpia espacios en blanco
    """
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone