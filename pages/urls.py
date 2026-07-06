from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    # path function receives the name of the endpoint, the function or class based view to render and
    # the internal name to use it on htmls
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]