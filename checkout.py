import os
import stripe
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/v1/billing", tags=["Billing & Payouts"])

# Safely binding your gate keys out of live code repos
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

class CheckoutSessionRequest(BaseModel):
    tenant_id: str
    tier_plan: str

@router.post("/create-checkout-session")
async def create_checkout_session(payload: CheckoutSessionRequest):
    if not stripe.api_key:
        raise HTTPException(
            status_code=500, 
            detail="Stripe credentials not configured on host environment."
        )
    
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f"PG-Mana Biomimetic Compute: {payload.tier_plan}",
                        'description': 'Metered physical seed-pod simulation acceleration pass.',
                    },
                    'unit_amount': 4900,  # $49.00 USD Example compute tier flat rate
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url="https://fly.dev",
            cancel_url="https://fly.dev",
            client_reference_id=payload.tenant_id
        )
        return {"checkout_url": session.url}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
