from data.database.models import User, Sign, async_session
from sqlalchemy import select, update


async def select_one_user(id_tg: str):
    async with async_session() as session:
        query = select(User).filter_by(tg_id=id_tg)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        if user:
            return user
        else:
            return None


async def add_new_user(id_tg: str):
    async with async_session() as session:
        new_user = User(tg_id = id_tg, sign_id = 1)
        session.add(new_user)
        await session.commit()


async def update_user_sign(id_tg: str, id_sign: int):
    async with async_session() as session:
        query = select(User).filter_by(tg_id = id_tg)
        res = await session.execute(query)
        user = res.scalar_one_or_none()
        if user:
            user.sign_id = id_sign
            await session.commit()
            return user
        return None


async def get_all_signs():
    async with async_session() as session:
        result = await session.execute(select(Sign))
        sings = result.scalars().all()
        signs_list = []
        for sign in sings:
            if sign.sign_name.lower() == "нет знака":
                continue
            else:
                signs_list.append([sign.id, sign.sign_name, sign.sign_link])
        return signs_list


async def get_one_sign(id_sign: int):
    async with async_session() as session:
        query = select(Sign).filter_by(id = id_sign)
        sign = await session.execute(query)
        sign_info = sign.scalar_one_or_none()
        return sign_info


async def update_sign_content(sign_id: int, new_content: str):
    async with async_session() as session:
        sign = await session.get(Sign, sign_id)
        if sign:
            sign.content = new_content
            await session.commit()
            return sign
        return None