from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from Backend.db import Base

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    brand_name = Column(String, nullable=False)
    created_at = Column(String, default=datetime.now(datetime.timezone.utc).isoformat())
    locales = relationship("Locale", back_populates="project")
    menu_items = relationship("MenuItem", back_populates="project")
    


class Locale(Base):
    __tablename__ = 'locales'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    code = Column(String, nullable=False)
    currency = Column(String, nullable=False, default='T')
    slang_pack = Column(String, nullable=False)
    project = relationship("Project", back_populates="locales")

class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    title = Column(String(200), nullable=False)
    image_url = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    #tags?
    project = relationship("Project", back_populates="menu_items")

class RenderJob(Base):
    __tablename__ = 'render_jobs'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    locale_id = Column(Integer, ForeignKey('locales.id'))
    preset_id = Column(String, default='fast')
    status = Column(String, nullable=False, default='pending')
    video_url = Column(String)
    duration = Column(Float, default=0.0)
    logs = Column(Text, default='')


