# Base environment built directly on optimized Nvidia CUDA stacks
FROM nvcr.io/nvidia/modulus/modulus:24.04

# Configure enterprise-grade non-root container isolation 
RUN groupadd -r odynex && useradd -r -g odynex -m -s /sbin/nologin mana_worker

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Secure file transfer matching TUTSA defensive compliance protocols
COPY --chown=mana_worker:odynex . .

USER mana_worker

EXPOSE 8080

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
