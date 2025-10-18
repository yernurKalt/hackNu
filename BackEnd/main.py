from fastapi import FastAPI
from BackEnd.db import Base, engine
from BackEnd.routes.projects import router as projects
from BackEnd.api.routes.menu import router as menu
from BackEnd.api.routes.plan import router as plan
from BackEnd.api.routes.render import router as render
from BackEnd.api.routes.jobs import router as jobs

app = FastAPI(title="Ad-Chef Localizer API")

@app.lifespan("start")
def init_db():
    Base.metadata.create_all(bind=engine)

app.include_router(projects)
app.include_router(menu)
app.include_router(plan)
app.include_router(render)
app.include_router(jobs)
