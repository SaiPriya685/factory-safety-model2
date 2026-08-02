from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.database import get_db
from backend.auth import create_access_token
from backend.models.user import User
from backend.dependencies import get_current_user
from backend.schemas.user_schema import UserRegister
from backend.schemas.user_schema import UserLogin

from backend.auth import hash_password
from backend.auth import verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.get("/me")
def current_user(
    user=Depends(get_current_user),
):
    return user
@router.post("/register")
def register(user: UserRegister,
             db: Session = Depends(get_db)):

    existing = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "Registration Successful"
    }


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):

    existing = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    if not verify_password(
        user.password,
        existing.password,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials",
        )

    token = create_access_token(
    {
        "sub": existing.email,
        "username": existing.username
    }
)

    return {
    "access_token": token,
    "token_type": "bearer"
    }