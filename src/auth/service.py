from datetime import timedelta
from fastapi.responses import JSONResponse
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc

from src.auth.models import User
from src.auth.schemas import UserCreateModel, UserLoginModel
from src.auth.utils import create_access_token
from src.utils.passwordconverter import generate_password_hash, verify_password


REFRESH_TOKEN_EXPIRY = 7 

class UserService:
    async def get_all_users(self, session: AsyncSession):
        statement = select(User).order_by(desc(User.created_at))

        result = await session.exec(statement)

        return result.all()

    async def get_user_by_email(self, email: str, session: AsyncSession):
        statement = select(User).where(User.email == email)

        result = await session.exec(statement)

        user = result.first()

        return user

    async def user_exists(self, email, session: AsyncSession):
        user = await self.get_user_by_email(email, session)

        return True if user is not None else False

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)

        new_user.password_hash = generate_password_hash(user_data_dict["password"])

        session.add(new_user)

        await session.commit()

        return new_user
    

    async def login_user(self, login_data: UserLoginModel, session: AsyncSession):
        email = login_data.email
        password = login_data.password

        user = await self.get_user_by_email(email, session)

        if user is not None:
            password_valid = verify_password(password, user.password_hash)

            if password_valid:
                access_token = create_access_token(
                    user_data={"email": user.email, "user_uid": str(user.uid)}
                )

                refresh_token = create_access_token(
                    user_data={"email": user.email, "user_uid": str(user.uid)},
                    refresh=True,
                    expiry=timedelta(days=REFRESH_TOKEN_EXPIRY),
                )

                return {
                    "message": "Login successful",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "email": user.email,
                    "uid": str(user.uid),
                }

        else:
            return {"message": "Login failed"}