from pydantic import BaseModel
from typing import List, Optional, Any

class ProjectCreate(BaseModel):
    name: str
    brand_rules: Optional[Any] = None

class LocaleCreate(BaseModel):
    code: str
    currency: str = "T"

class MenuItemIn(BaseModel):
    title: str
    price: float

class PlanIn(BaseModel):
    locales: List[str]         # must be in RU and KZ languages
    hooks: List[str]           # collection of price, speed and quality
    n_per_hook: int = 1

class ScriptOut(BaseModel):
    id: int
    locale: str
    hook_type: str
    text: str

class RenderRequest(BaseModel):
    preset: str = "fast"

class JobOut(BaseModel):
    id: int
    status: str
    video_url: Optional[str] = None
    thumb_url: Optional[str] = None
    logs: Optional[str] = None
