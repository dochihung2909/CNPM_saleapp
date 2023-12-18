from flask import render_template, request, redirect, session, jsonify
import dao
import utils
from app import app, login
from flask_login import login_user

@app.route("/")
def index_page():
    kw = request.args.get('kw')
    cate_id = request.args.get('category_id')
    page = request.args.get('page') or 0
    products = dao.get_products(kw, cate_id, page)
    product_page = int(dao.count_product() / 4 + 1)
    return render_template('index.html', products=products, product_page = product_page, current_page = int(page))

@app.route("/<slug>")
def slug_page(slug):
    return render_template('notfound.html')


@app.route("/products/<slug>")
def product_page(slug):
    product = dao.get_products(product_id = int(slug))

    return render_template('product.html', product = product[0])

@app.route('/admin/login', methods =['post'])
def login_page():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username, password)
    if user:
        login_user(user=user)
    return redirect('/admin')

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

@app.route('/api/cart', methods =["post"])
def add_to_cart():

    cart = session.get("cart")
    if cart is None:
        cart = {}

    data = request.json
    id = str(data.get('id'))

    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            "id" : id,
            "name" : data.get('name'),
            "price" : data.get('price'),
            "quantity" : 1
        }
    session['cart'] = cart
    return jsonify(utils.count_cart(cart))

@app.route('/cart')
def index():
    return render_template('cart.html')

@app.context_processor
def common_resp():
    return {
        'catalogies': dao.get_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }

if __name__ == "__main__":
    from app import admin
    app.run(debug=True, host='localhost', port=3000)