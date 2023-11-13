from models import Category, Product
from app import app, db
from flask_admin import  Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name='Quản lý bán hàng', template_mode='bootstrap4')

class ProductViewModel(ModelView):
    column_list = ('id', 'name', 'price', 'active')
    column_searchable_list = ['name']
    column_filters = ['name', 'price']

class MyStatisView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

admin.add_view(ProductViewModel(Product, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(MyStatisView(name='Thong ke bao cao'))