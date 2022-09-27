from django.urls import path


from .views import CategoryLCView

urlpatterns = [
    path('categories/', CategoryLCView.getCategories, name='category'),
    ]