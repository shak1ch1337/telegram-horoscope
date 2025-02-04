from data.database.models import User, async_session
from sqlalchemy import select


#   Index

async def get_all_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        users_list = []
        for user in users:
            users_list.append([user.tg_id, user.sign_id, user.send_state])
        return users_list


#   Show

async def select_one_user(id_tg: str):
    async with async_session() as session:
        query = select(User).filter_by(tg_id = id_tg)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        if user:
            return user
        else:
            return None


#   Store

async def add_new_user(id_tg: str):
    async with async_session() as session:
        new_user = User(tg_id = id_tg, sign_id = 1)
        session.add(new_user)
        await session.commit()


#   Update sign

async def update_user_sign(id_tg: str, id_sign: int):
    async with async_session() as session:
        query = select(User).filter_by(tg_id = id_tg)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        if user:
            user.sign_id = id_sign
            await session.commit()
            return user
        return None


#   Update send_state

async def update_user_send_state(id_tg: str, state: int):
    async with async_session() as session:
        query = select(User).filter_by(tg_id = id_tg)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        if user:
            user.send_state = state
            await session.commit()
            return user
        return None