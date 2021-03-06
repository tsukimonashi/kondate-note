from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///db.sqlite3', echo=True)
metadata = MetaData()
metadata.bind = engine

menus = Table(
    'menus', metadata,
    Column('id',Integer, primary_key=True),
    Column('name', String, unique=True),
    Column('kcal', Integer),
    Column('image', String),
)

def create():
    metadata.create_all()

def create_menu(name, kcal, image):
    return menus.insert().execute(name=name, kcal=kcal, image=image)


def create_update(id, name, kcal, image):
    menus.update().where(menus.c.id == id).execute(
        name=name, kcal=kcal, image=image
    )

def create_delete(id):
    menus.delete().where(menus.c.id == id).execute()


def create_fetchall():
    return menus.select().execute().fetchall()


def cleate_fetch(id):
    menus.select().where(menus.c.id == id).execute().fetchone()






