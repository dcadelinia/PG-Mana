import os
import stripe
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

# Initialize the router to mount directly into main.py
router = APIRouter(prefix="/v1/billing", tags=["Billing & Payouts"])

# Retrieve keys securely via platform environment variables
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

class CheckoutSessionRequest(BaseModel):
    tenant_id: str
    tier_plan: str  # e.g., "micro-drone-pinn-tier"

@router.post("/create-checkout-session")
async def create_checkout_session(payload: CheckoutSessionRequest):
    if not stripe.api_key:
        raise HTTPException(
            status_code=500, 
            detail="Stripe credentials not configured on host environment."
        )
    
    try:
        # Generate an absolute tokenized checkout flow
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f"PG-Mana Biomimetic Compute: {payload.tier_plan}",
                        'description': 'Metered physical simulation acceleration pass.',
                    },
                    'unit_amount': 4900,  # $49.00 USD example billing tier
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f"https://fly.dev{{CHECKOUT_SESSION_ID}}",
            cancel_url="https://fly.dev",
            client_reference_id=payload.tenant_id
        )
        return {"checkout_url": session.url}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
