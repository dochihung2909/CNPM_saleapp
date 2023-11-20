from models import Category, Product, User, UserRoleEnum
from app import app, db
from flask_admin import  Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from flask import redirect



admin = Admin(app=app, name='Quản lý bán hàng', template_mode='bootstrap4')

class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN

class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class ProductViewModel(AuthenticatedAdmin):
    column_list = ('id', 'name', 'price', 'active')
    column_searchable_list = ['name']
    column_filters = ['name', 'price']

class MyCategoryView(AuthenticatedAdmin):
    column_list = ['name', 'products']

class MyStatisView(AuthenticatedUser):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

class LogoutView(AuthenticatedUser):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(ProductViewModel(Product, db.session))
admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyStatisView(name='Thong ke bao cao'))
admin.add_view(LogoutView(name='Đăng Xuất'))