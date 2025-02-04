from data.database.models import Sign, async_session
from sqlalchemy import select


#   Index

async def get_all_signs():
    async with async_session() as session:
        result = await session.execute(select(Sign))
        signs = result.scalars().all()
        signs_list = []
        for sign in signs:
            if sign.sign_name.lower() == "нет знака":
                continue
            else:
                signs_list.append([sign.id, sign.sign_name, sign.sign_link])
        return signs_list


#   Show

async def get_one_sign(id_sign: int):
    async with async_session() as session:
        query = select(Sign).filter_by(id = id_sign)
        sign = await session.execute(query)
        sign_info = sign.scalar_one_or_none()
        return sign_info


#   Update

async def update_sign_content(sign_id: int, new_content: str):
    async with async_session() as session:
        sign = await session.get(Sign, sign_id)
        if sign:
            sign.content = new_content
            await session.commit()
            return sign
        return None