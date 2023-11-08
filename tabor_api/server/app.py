import uvicorn
from tabor_api.logging import log
from tabor_api.config import TaborConfig, load_config
from tabor_api.visa.client import TaborClient
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Tabor api server"}


@app.get("/status")
async def status():
    return {"idn": TaborClient.client.query("IDN?")}


def start_server(config: TaborConfig = None):
    config = config or load_config()
    uvicorn.run(
        app,
        port=config.port,
        host=config.host,
        # reload=config.reload,
        # reload_dirs=[config.reload_dir],
    )


if __name__ == "__main__":
    log.info("Starting uvicorn server")
    start_server()
