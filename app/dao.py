from models import Category, Product, User

def get_categories():
    return Category.query

def get_products(kw = False, product_id = False, cate_id = False):
    products = Product.query


    if kw:
        products = products.filter(Product.name.contains(kw))
    if product_id:
        products = products.filter(Product.id == product_id)
    if cate_id:
        products = products.filter(Product.category_id == cate_id)

    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)