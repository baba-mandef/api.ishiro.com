from rest_framework.routers import DefaultRouter

from ishiro.auth.viewsets import login, register
from ishiro.category.viewsets import CategoryViewSet
from ishiro.extra.data.viewsets import PopulateViewSet
from ishiro.wallet.viewsets import WalletViewSet
from ishiro.activity.viewsets import ActivityViewSet


from django.urls import path, include

Router = DefaultRouter(trailing_slash=False)

# authentication
Router.register("login", login.ObtainAuthToken, "login")
Router.register("register", register.RegisterViewSet, "register")

#category
Router.register(r"(?P<category_type>(wallet|income|expense))/category", CategoryViewSet, "category")

#activity
Router.register(r"(?P<activity_type>(income|expense))/activity", ActivityViewSet, "activity")

#wallet
Router.register("wallet", WalletViewSet, "wallet")

#populate
Router.register("populate", PopulateViewSet, "populate")

urlpatterns = [path("", include(Router.urls))]
