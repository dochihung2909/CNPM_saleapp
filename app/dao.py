from models import Category, Product, User, ReceiptDetails, Receipt
import hashlib
from app import app, db
from sqlalchemy import func
from flask_login import  current_user

def get_categories():
    return Category.query.all()

def get_products(kw = False, cate_id = None, page = None, product_id = False,):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))
    if product_id:
        products = products.filter(Product.id == product_id)
    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))
    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size
        return products.slice(start, start + page_size)

    return products.all()

def count_product():
    return Product.query.count()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()


def count_products_by_cate():
    return db.session.query(Category.id, Category.name, func.count(Product.id))\
                    .join(Product, Product.category_id.__eq__(Product.id)).group_by(Category.id).all()

def stats_revenue(kw):
    query = db.session.query(Product.id, Product.name, func.sum(ReceiptDetails.quantity * ReceiptDetails.unit_price))\
            .join(ReceiptDetails, ReceiptDetails.id.__eq__(Product.id))

    if kw:
        query = query.filter(Product.name.contains(kw))
    return query.group_by(Product.id).all()


def add_receipt(cart):
    if (cart):
        c = Receipt(user=current_user)
        db.session.add(receipt)