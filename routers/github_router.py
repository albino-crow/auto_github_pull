from typing import Any
from fastapi import APIRouter, Body, Depends, Header,status
from settings.auth import SERVER_KEY, STAGING_KEY
from utils.github_validation import get_x_hub_signature_256, validate_secret_key
from service.github_webhook import github_update_server, github_update_staging

router = APIRouter(tags=["github"])


@router.post("/server", status_code=status.HTTP_200_OK)
async def update_server(
    payload: Any = Body(None),
    signature: str = Depends(get_x_hub_signature_256)
):
    
    validate_secret_key(payload,SERVER_KEY, signature)
    github_update_server()

@router.post("/staging", status_code=status.HTTP_200_OK)
async def update_staging(
    payload: Any = Body(None),
    signature: str = Depends(get_x_hub_signature_256)
):
    validate_secret_key(payload,STAGING_KEY, signature)
    github_update_staging()

