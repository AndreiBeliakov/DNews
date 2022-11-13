from django.urls import path

from .views import NewsList, NewDetail, NewSearch,  NewCreate, NewEdit, NewDelete

urlpatterns = [

   path('', NewsList.as_view(), name= 'new_list'),

   path('<int:pk>', NewDetail.as_view(), name='new_detail'),

   path('search/', NewSearch.as_view(), name='search'),

   path('create/', NewCreate.as_view(), name='create'),

   path('<int:pk>/edit/', NewEdit.as_view(), name='edit'),

   path('<int:pk>/delete/', NewDelete.as_view(), name='delete'),



]