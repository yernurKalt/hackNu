from fastapi import FastAPI
from BackEnd.db import Base, engine
from .api.routes.projects import router as projects
from .api.routes.menu import router as menu
from .api.routes.plan import router as plan
from .api.routes.render import router as render
from .api.routes.jobs import router as jobs

app = FastAPI(title="Ad-Chef Localizer API")

@app.on_event("start")
def init_db():
    Base.metadata.create_all(bind=engine)

app.include_router(projects)
app.include_router(menu)
app.include_router(plan)
app.include_router(render)
app.include_router(jobs)
