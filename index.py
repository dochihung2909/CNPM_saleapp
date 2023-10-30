from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route("/")
def index_page():
    kw = request.args.get('kw')
    cates = dao.get_categories()
    products = dao.get_products(kw)
    return render_template('index.html', catalogies=cates, products=products)

@app.route("/<slug>")
def slug_page(slug):
    return render_template('notfound.html')


@app.route("/products/<slug>")
def product_page(slug):
    product = dao.get_products(slug = slug)

    return render_template('product.html', slug=slug)

if __name__ == "__main__":
    app.run(debug=True)