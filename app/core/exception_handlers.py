from fastapi import Request
from fastapi.responses import JSONResponse

from app.services.auth import InvalidCredentialsError, UsernameAlreadyTakenError


EXCEPTION_STATUS_CODE_MAP = {
    UsernameAlreadyTakenError: 409,
    InvalidCredentialsError: 401,
}


def register_exception_handlers(app):
    for exc_type, status_code in EXCEPTION_STATUS_CODE_MAP.items():

        @app.exception_handler(exc_type)
        async def handler(request: Request, exc, status_code=status_code):
            return JSONResponse(status_code=status_code, content={"detail": str(exc)})
