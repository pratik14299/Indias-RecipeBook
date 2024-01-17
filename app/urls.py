from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/',views.CreateRecipe,name = "create_url"),
    path('show/',views.Display,name = "show_url"),
    path('update/<int:id>',views.UpdateRecepe,name = "update_url"),
    path('delete/<int:id>',views.DeleteCard,name = "delete_url"),
    path('content/<int:id>',views.contentView,name = "content_url"),
] 