from contextlib import asynccontextmanager
import asyncio

from fastapi import FastAPI

from app.services.device_manager import DeviceStateManager
from app.simulator.simulator import DeviceSimulator
from app.api.routes import router

from app.core.state import manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs once when FastAPI starts.
    """

    simulator = DeviceSimulator(manager)

    # Start simulator in background
    simulator_task = asyncio.create_task(simulator.start())

    print("✅ Simulator started.")

    yield

    # Stop simulator when FastAPI shuts down
    simulator_task.cancel()

    print("🛑 Simulator stopped.")


app = FastAPI(
    title="Smart Office Device Management API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Smart Office Backend Running"
    }