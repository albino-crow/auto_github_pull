import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.github_router import router as github_router
from utils.argparse_manager import get_server_port





app = FastAPI(
    title="Lumina Back",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(github_router)



@app.get("/")
def read_root():
    return {"start": "another"}




if __name__ == "__main__":
    uvicorn.run(app, port=get_server_port())