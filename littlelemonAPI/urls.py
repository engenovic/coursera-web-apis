from django.urls import path
from . import views

urlpatterns = [
    # path('menu-items/', views.MenuItemsView.as_view()),
    # path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu-items', views.menu_items),
    path('menu-items/<int:id>', views.single_item),
]
