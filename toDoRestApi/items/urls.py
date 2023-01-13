from django.urls import path
from items import views

urlpatterns = [
    path('api/', views.apiOverview),
    path('api/items-retrieve', views.retrieve_items),
    path('api/items-retrieve/<int:pk>', views.retrieve_item),
    path('api/items-delete/<int:pk>/', views.delete_item),
    path('api/items-post', views.post_item),
    path('api/items-update/<int:pk>', views.update_item),

]

