from sqlalchemy import Column, Integer, String
from .database import Base

class TodoDB(Base):
  __tablename__ = 'pedidos'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False)
  description = Column(String(255), nullable=False)

  def __repr__(self):
    return f'<User:[id:{self.id}, name:{self.name}, email:{self.email}, description:{self.description}]>'
    
  def serialize(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
      "description": self.description
    }
