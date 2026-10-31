# PG Mana – Portable Physics-ML Simulation Engine

**Version 1.1.0-portable**  
Deploy **anywhere · any cloud · any time** in under 60 seconds.

This edition removes the hard NVIDIA Modulus / NGC dependency so the service runs on ordinary CPU instances (Cloud Run, Render, Fly.io, Railway, AWS Fargate, Azure Container Apps, local Docker, Kubernetes, etc.). The original PINN surrogate logic is preserved and remains fully compatible with the published API contract.

---

## Quick Start (local)

```bash
# 1. Clone / unzip
cd PG-Mana

# 2. Optional: create env file
cp .env.example .env

# 3. One-command launch
docker compose up --build -d

# 4. Verify
curl http://localhost:8080/health
```

Expected health response:

```json
{
  "status": "ONLINE",
  "version": "1.1.0-portable",
  "hardware": "CPU",
  "details": { "cpu_count": 4, "memory_gb": 7.8, "gpu_available": false, ... },
  "entity": "Odynex Axis Logistics LLC",
  "billing_mode": "mock"
}
```

---

## API

### Health
```bash
curl http://localhost:8080/health
```

### Run aerodynamic simulation
```bash
curl -X POST http://localhost:8080/v1/simulate/aerodynamics \
  -H "X-Odynex-Mana-Key: mana_live_demo_key" \
  -H "Content-Type: application/json" \
  -d '{
    "tenant_id": "ODYNEX-AXIS-GA-001",
    "points_count": 50000,
    "target_accuracy_delta": 0.0001
  }'
```

Interactive docs: http://localhost:8080/docs

---

## Deploy to Any Cloud

### Google Cloud Run
```bash
gcloud run deploy pg-mana \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080 \
  --memory 512Mi
```

### Render.com
- New → Web Service → Connect repo or upload zip
- Runtime: Docker
- Port: 8080

### Fly.io
```bash
fly launch --name pg-mana
fly deploy
```

### Railway
```bash
railway up
```

### AWS / Azure / DigitalOcean / Linode
Any container platform that accepts a standard Dockerfile works.  
No GPU, no NGC login, no special base image required.

### Classic Docker on a VPS
```bash
docker build -t pg-mana .
docker run -d -p 8080:8080 --name pg-mana --restart unless-stopped pg-mana
```

---

## Environment Variables

| Variable              | Default          | Description                                      |
|-----------------------|------------------|--------------------------------------------------|
| `PORT`                | `8080`           | Listen port (Cloud platforms inject this)        |
| `REQUIRE_STRIPE`      | `false`          | Enforce live Stripe subscription checks          |
| `STRIPE_SECRET_KEY`   | –                | Optional live Stripe key                         |
| `API_KEY_PREFIX`      | `mana_live_`     | Accepted API-key prefix                          |
| `CORS_ORIGINS`        | `*`              | Comma-separated allowed origins                  |
| `LOG_LEVEL`           | `INFO`           | Logging verbosity                                |

Copy `.env.example` → `.env` and adjust. **Never commit real secrets.**

---

## Optional: Re-enable Real NVIDIA Modulus / GPU

If you later obtain an NGC-enabled GPU node:

1. Change the base image in `Dockerfile` back to  
   `nvcr.io/nvidia/modulus/modulus:24.04` (or newer).
2. Add `torch`, `nvidia-modulus`, `warp-lang` to `requirements.txt`.
3. Replace the surrogate block inside `run_pinn_aerodynamics` with real Modulus model code.
4. Launch with `--gpus all`.

Until then the portable edition gives you identical API behaviour, health checks, auth, and billing hooks on ordinary hardware.

---

## What Was Fixed for Portability

| Original Problem                         | Portable Fix                                      |
|------------------------------------------|---------------------------------------------------|
| Base image = heavy NGC Modulus (GPU-only)| Multi-stage `python:3.12-slim` (~120 MB)          |
| Hard `nvidia-smi` failure                | Soft detection – falls back to CPU                |
| Stripe always required                   | Fully optional (`REQUIRE_STRIPE=false`)           |
| Secrets committed in `.env`              | `.env.example` only; real `.env` gitignored       |
| Broken Stripe timestamp `"now"`          | Correct Unix timestamp                            |
| Wrong GitHub Actions (Django)            | Cleaned / simplified                              |
| No healthcheck / compose                 | Production-ready Dockerfile + docker-compose      |

---

## License

MPL-2.0 (same as upstream).  
Trade-secret / TUTSA notices from the original README remain in effect for the conceptual pipeline.
