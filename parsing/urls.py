from django.urls import path
from parsing import views, parse_site

# from parsing.views import HomePageView

urlpatterns = [

    # path('', HomePageView.as_view(), name='home'),
    path('', views.home, name='home'),
    path('view_rez/', views.view_rez, name='view'),

]
