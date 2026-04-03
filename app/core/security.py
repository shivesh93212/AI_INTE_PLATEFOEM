import httpx
from jose import jwt
from app.core.config import settings

jwks_cache=None

async def get_jwks():
    global jwks_cache

    if jwks_cache:
        return jwks_cache
    
    async with httpx.AsyncClient() as client:
        response = await client.get(settings.CLERK_JWKS_URL)
        jwks_cache=response.json()
    
    return jwks_cache

async def verify_token(token:str):
    jwks = await get_jwks()

    unverified_header=jwt.get_unverified_header(token)
    kid=unverified_header["kid"]

    key=next((k for k in jwks["keys"] if k["kid"]==kid),None)

    if not key:
        raise Exception("Invalid token key")
    
    payload =jwt.decode(
        token,key,
        algorithms=["RS256"],
        audience=None,
        options={"verify_aud":False}

    )

    return payload
