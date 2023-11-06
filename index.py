from flask import Flask, render_template, request
import dao
from app import app

@app.route("/")
def index_page():
    kw = request.args.get('kw')
    cate_id = request.args.get('category_id')
    cates = dao.get_categories()
    products = dao.get_products(kw, cate_id = int(cate_id) if cate_id else None)


    return render_template('index.html', catalogies=cates, products=products)

@app.route("/<slug>")
def slug_page(slug):
    return render_template('notfound.html')


@app.route("/products/<slug>")
def product_page(slug):
    product = dao.get_products(product_id = int(slug))

    return render_template('product.html', product = product[0])

if __name__ == "__main__":
    app.run(debug=True)