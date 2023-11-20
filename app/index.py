from flask import render_template, request, redirect
import dao
from app import app, login
from flask_login import login_user

@app.route("/")
def index_page():
    kw = request.args.get('kw')
    cate_id = request.args.get('category_id')
    page = request.args.get('page')
    cates = dao.get_categories()
    products = dao.get_products(kw, cate_id, page)
    product_page = int(dao.count_product() / 4 + 1)

    return render_template('index.html', catalogies=cates, products=products, product_page = product_page, current_page = int(page))

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

if __name__ == "__main__":
    from app import admin
    app.run(debug=True, host='localhost', port=3000)