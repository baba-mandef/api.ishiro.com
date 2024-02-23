from rest_framework.routers import DefaultRouter

from ishiro.auth.viewsets import login, register
from ishiro.category.viewsets import CategoryViewSet
from ishiro.extra.data.viewsets import PopulateViewSet
from ishiro.wallet.viewsets import WalletViewSet


from django.urls import path, include

Router = DefaultRouter(trailing_slash=False)

# authentication
Router.register("login", login.ObtainAuthToken, "login")
Router.register("register", register.RegisterViewSet, "register")

#category
Router.register(r"(?P<category_type>(wallet|income|expense))/category", CategoryViewSet, "category")


#wallet
Router.register("wallet", WalletViewSet, "wallet")

#populate
Router.register("populate", PopulateViewSet, "populate")

urlpatterns = [path("", include(Router.urls))]
