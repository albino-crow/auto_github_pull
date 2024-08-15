from typing import Any
from fastapi import APIRouter, Body, Depends, Header, Request,status
from settings.auth import SERVER_KEY, STAGING_KEY
from utils.github_validation import get_x_hub_signature_256, validate_secret_key
from service.github_webhook import github_update_server, github_update_staging

router = APIRouter(tags=["github"])


@router.post("/server", status_code=status.HTTP_200_OK)
async def update_server(
    request: Request,
    signature: str = Depends(get_x_hub_signature_256)
):
    
    validate_secret_key(await request.body(),SERVER_KEY, signature)
    github_update_server()

@router.post("/staging", status_code=status.HTTP_200_OK)
async def update_staging(
    request: Request,
    signature: str = Depends(get_x_hub_signature_256)
):
    validate_secret_key(await request.body(),STAGING_KEY, signature)
    github_update_staging()

