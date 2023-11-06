from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100), default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.commit()
        p1 = Product(name='iPhone 13', price=21000000, category_id=1)
        p2 = Product(name='Samsung Galaxy S21', price=15000000, category_id=1)
        p3 = Product(name='Google Pixel 6', price=18000000, category_id=1)
        p4 = Product(name='OnePlus 9 Pro', price=17000000, category_id=1)
        p5 = Product(name='Xiaomi Mi 11', price=12000000, category_id=1)
        p6 = Product(name='Sony Xperia 1 III', price=20000000, category_id=1)
        p7 = Product(name='LG Velvet 5G', price=14000000, category_id=1)
        p8 = Product(name='Motorola Edge+', price=16000000, category_id=1)
        p9 = Product(name='Nokia 8.3', price=13000000, category_id=1)
        p10 = Product(name='Huawei P40 Pro', price=19000000, category_id=1)
        db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        db.session.commit()