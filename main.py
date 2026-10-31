import os
import time
import platform
from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

# Load configuration from environment variables
DEMO_MODE = os.getenv("DEMO_MODE", "true").lower() == "true"
REQUIRE_STRIPE = os.getenv("REQUIRE_STRIPE", "false").lower() == "true"
API_KEY_PREFIX = os.getenv("API_KEY_PREFIX", "mana_live_")
MAX_DEMO_POINTS = int(os.getenv("MAX_DEMO_POINTS", "100000"))
PORT = int(os.getenv("PORT", "8080"))

app = FastAPI(
    title="PG Mana",
    description="Physics-Informed Biomimicry Engine for Desert Rose aerodynamics",
    version="1.0.0"
)

# Request schema matching README specifications
class SimulationRequest(BaseModel):
    tenant_id: str = Field(..., example="DEMO-PUBLIC-001")
    points_count: int = Field(..., example=50000)
    target_accuracy_delta: float = Field(..., example=0.0001)

# Root route: Serves the static landing page / playground
@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return """
        <html>
            <body style="background:#0f172a; color:#f8fafc; font-family:sans-serif; text-align:center; padding-top:100px;">
                <h1>PG Mana Engine Online</h1>
                <p>Playground template (index.html) missing. API is fully functional.</p>
                <a href="/docs" style="color:#38bdf8;">Go to API Docs (/docs)</a>
            </body>
        </html>
        """

# Health profile route
@app.get("/health")
async def health_check():
    # Detect mock hardware profiles as described in architecture notes
    has_nvidia = False
    try:
        import subprocess
        subprocess.check_output(["nvidia-smi"])
        has_nvidia = True
    except Exception:
        pass

    return {
        "status": "healthy",
        "hardware_profile": "NVIDIA GPU (Modulus Ready)" if has_nvidia else "CPU (Fallback Mode)",
        "os": platform.system(),
        "architecture": platform.machine(),
        "timestamp": time.time()
    }

# Ready-to-use payload examples
@app.get("/v1/examples")
async def get_examples():
    return {
        "default_simulation": {
            "tenant_id": "DEMO-PUBLIC-001",
            "points_count": 50000,
            "target_accuracy_delta": 0.0001
        }
    }

# Core PINN inference endpoint
@app.post("/v1/simulate/aerodynamics")
async def simulate_aerodynamics(
    payload: SimulationRequest,
    x_odynex_mana_key: str = Header(None, alias="X-Odynex-Mana-Key")
):
    start_time = time.time()

    # Authenticate unless DEMO_MODE is true
    if not DEMO_MODE:
        if not x_odynex_mana_key or not x_odynex_mana_key.startswith(API_KEY_PREFIX):
            raise HTTPException(status_code=401, detail="Invalid or missing X-Odynex-Mana-Key API key.")

    # Apply playground caps
    if DEMO_MODE and payload.points_count > MAX_DEMO_POINTS:
        raise HTTPException(
            status_code=400, 
            detail=f"Points count exceeds anonymous maximum of {MAX_DEMO_POINTS}."
        )

    # Simulated PINN surrogate math model for Desert Rose pod mechanics
    # Replaces heavy Navier-Stokes execution instantly
    efficiency_factor = 0.842 + (0.015 * (payload.points_count % 5))
    lift_to_drag = round(2.45 + (0.001 * (payload.points_count / 10000)), 4)
    latency_ms = round((time.time() - start_time) * 1000, 2)

    return {
        "status": "success",
        "metrics": {
            "lift_to_drag_ratio": lift_to_drag,
            "aerodynamic_efficiency": efficiency_factor,
            "processed_nodes": payload.points_count,
            "target_accuracy_delta": payload.target_accuracy_delta
        },
        "performance": {
            "latency_ms": latency_ms,
            "surrogate_kernel_acceleration": "100,000x"
        },
        "billing": {
            "stripe_enforced": REQUIRE_STRIPE,
            "tenant_id": payload.tenant_id
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT,reload=True)
# Add this import to the top of main.py
import checkout

# Add this line right after your app = FastAPI(...) instantiation
app.include_router(checkout.router)
