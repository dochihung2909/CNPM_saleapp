from models import Category, Product

def get_categories():

    return Category.query.all()

def get_products(kw = False, product_id = False, cate_id = False):
    products = Product.query


    if kw:
        products = products.filter(Product.name.contains(kw))
    if product_id:
        products = products.filter(Product.id == product_id)
    if cate_id:
        products = products.filter(Product.category_id == cate_id)

    return products.all()
