from django.urls import path
from . import views

app_name='kounyu'
urlpatterns = [
    path('kounyu_list/',views.KounyuListView.as_view(),name='kounyu_list'),
    path('kounyu_create/',views.KounyuCreateView.as_view(),name='kounyu_create'),
    path('create_done/',views.create_done, name='create_done'),
    path('update/<int:pk>/',views.KounyuUpdateView.as_view(),name='kounyu_update'),
    path('update_done/',views.update_done, name='update_done'),
    path('delete/<int:pk>/', views.KounyuDeleteView.as_view(),name='kounyu_delete'),
    path('delete_done/', views.delete_done, name='delete_done'),
]