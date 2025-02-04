from sqlalchemy import Integer, Column, ForeignKey, String, Text
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from config_reader import config


connection = f"mysql+aiomysql://{config.db_user.get_secret_value()}@{config.db_address.get_secret_value()}/{config.db_name.get_secret_value()}"
engine = create_async_engine(connection)
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    tg_id = Column(String(20), nullable = False)
    sign_id = Column(Integer, ForeignKey("signs.id"))
    send_state = Column(Integer, nullable = False, default = 0)


class Sign(Base):
    __tablename__ = "signs"

    id = Column(Integer, primary_key = True)
    sign_name = Column(String(15), nullable = False)
    sign_link = Column(String(15), nullable = False)
    content = Column(Text, nullable = False)


async def migration():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)