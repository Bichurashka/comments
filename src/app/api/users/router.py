from fastapi import APIRouter, Depends

from app.core.security import get_current_user_id
from app.schemas.user import CurrentUserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=CurrentUserResponse)
async def read_current_user(user_id: int = Depends(get_current_user_id)) -> CurrentUserResponse:
    return CurrentUserResponse(user_id=user_id)