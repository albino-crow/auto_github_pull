import hashlib
import hmac
from typing import Any, Dict, Optional
from fastapi import HTTPException, Header


def get_x_hub_signature_256(x_hub_signature_256: Optional[str] = Header(None)):

    if x_hub_signature_256 is None:
        raise HTTPException(status_code=400, detail="X-Hub-Signature-256 header missing")
    
    return x_hub_signature_256 

def validate_secret_key(body,key: str, singature_header: str):
    hash_object = hmac.new(key.encode('utf-8'), msg=body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    if not hmac.compare_digest(expected_signature, singature_header):
        print("not match")
        raise HTTPException(status_code=403, detail="Request signatures didn't match!")