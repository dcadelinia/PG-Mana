# PG Mana

**Physics-Informed Biomimicry Engine**

> Digitize the passive aerodynamics of the Desert Rose.  
> Design zero-power micro-drones, biodegradable sensor swarms, and smart materials — in milliseconds.

[![Deploy](https://img.shields.io/badge/deploy-any%20cloud-0ea5e9?style=flat-square)](#deploy)
[![API](https://img.shields.io/badge/API-FastAPI-009688?style=flat-square)](http://localhost:8080/docs)
[![License](https://img.shields.io/badge/license-MPL--2.0-blue?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.0.0-purple?style=flat-square)](#)

---

## Why PG Mana

Traditional CFD is too slow for iterative biomimetic design.  
PG Mana replaces heavy Navier-Stokes solvers with a **Physics-Informed Neural Network surrogate** that runs **up to 100,000× faster** while preserving the core aerodynamic invariants of *Adenium obesum* (Desert Rose) seed pods.

One container. Beautiful product UI + production API.  
Works on any cloud, any hardware, no GPU required.

---

## 60-Second Start

```bash
docker compose up --build -d
open http://localhost:8080
```

That’s it. You get:

- A polished dark-mode product experience
- Live interactive playground (no account needed)
- Full OpenAPI docs at `/docs`
- Health & telemetry endpoints ready for monitoring

---

## Product Surface

| Route | Description |
|-------|-------------|
| `/` | Product landing + interactive playground |
| `/docs` | Interactive API documentation (Swagger) |
| `/health` | Liveness + hardware profile |
| `/v1/simulate/aerodynamics` | Core PINN inference endpoint |
| `/v1/examples` | Ready-to-use payload examples |

---

## API Example

```bash
curl -X POST http://localhost:8080/v1/simulate/aerodynamics \
  -H "X-Odynex-Mana-Key: mana_live_demo" \
  -H "Content-Type: application/json" \
  -d '{
    "tenant_id": "DEMO-PUBLIC-001",
    "points_count": 50000,
    "target_accuracy_delta": 0.0001
  }'
```

Response includes lift/drag efficiency, latency, processed nodes, and hardware context.

---

## Deploy Anywhere

### One-command platforms

```bash
# Google Cloud Run
gcloud run deploy pg-mana --source . --region us-central1 --allow-unauthenticated --memory 512Mi

# Fly.io
fly launch && fly deploy

# Railway
railway up
```

### Classic
```bash
docker build -t pg-mana .
docker run -d -p 8080:8080 --name pg-mana pg-mana
```

Works on Render, DigitalOcean App Platform, AWS Fargate, Azure Container Apps, Kubernetes, bare metal — anything that speaks Docker.

---

## Configuration

| Variable | Default | Purpose |
|----------|---------|---------|
| `DEMO_MODE` | `true` | Public playground without keys |
| `REQUIRE_STRIPE` | `false` | Enforce live billing |
| `API_KEY_PREFIX` | `mana_live_` | Accepted key prefix |
| `MAX_DEMO_POINTS` | `100000` | Soft limit for anonymous runs |
| `PORT` | `8080` | Listen port (cloud platforms inject this) |

Copy `.env.example` → `.env` when you need secrets.

---

## Architecture Notes

- **Portable by default** — pure Python + FastAPI, multi-stage slim image (~120 MB)
- **GPU optional** — automatically detects NVIDIA hardware; falls back gracefully
- **Stripe optional** — metered billing hooks exist but are off by default
- **Frontend** — zero-build Tailwind + vanilla JS served by the same process
- **Ready for real Modulus** — swap the surrogate kernel when you have NGC + Tensor Core nodes

---

## Use Cases

- **Agricultural sensor swarms** — long-duration, zero-power, biodegradable
- **Micro-UAV / ISR** — extreme endurance passive flight optimization
- **Smart materials & 3D print export** — geometry-ready industrial blueprints

---

## License

MPL-2.0  

Conceptual pipeline and trade-secret protections from the original Odynex Axis Logistics work remain in force for the underlying biomimetic methodology.
