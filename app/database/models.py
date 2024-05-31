from sqlalchemy import BigInteger, String ,ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import (
    AsyncAttrs, 
    async_sessionmaker,
    create_async_engine
    )

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')#---------------------- create db

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id = mapped_column(BigInteger)


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(50))

class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(50))
    price: Mapped[int] = mapped_column()
    description:Mapped[str] = mapped_column(String(500))
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))

#--------------------------------------------------------------------------------------Створюємо таблиці, якщо їх не існує
async def  async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)