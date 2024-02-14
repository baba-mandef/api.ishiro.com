from rest_framework.routers import DefaultRouter

from ishiro.auth.viewsets import login, register


from django.urls import path, include

Router = DefaultRouter(trailing_slash=False)


Router.register("login", login.ObtainAuthToken, basename="login")
Router.register("register", register.RegisterViewSet, basename="register")


urlpatterns = [path("", include(Router.urls))]
