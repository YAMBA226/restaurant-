from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, add_to_cart, cart, delete_cart
from shop import settings
from accounts.views import signup, logout_user, login_user

urlpatterns = [
    path('' , index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('login/', login_user, name="login"),
    path('cart/', cart, name="cart"),
    path('cart/delete', delete_cart, name="delete-cart"),
    path('product/<str:slug>', product_detail, name="product"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add_to_cart"),
] + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
