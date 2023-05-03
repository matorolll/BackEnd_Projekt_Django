from django.urls import path
from . import views


#sciezka, funkcja z views, nazwa

urlpatterns = [
    #GENEROWANIE WIDOKOW
    path("", views.showHomePage, name="home"),
    path("Auction/", views.showAuctionPage, name="auction"),
    path("Contact/", views.showContactPage, name="contact"),

    #ZARZADZANIE UZYTKOWNIKIEM
    path("Signup/", views.showSignupPage, name="signup"),
    path("Login/", views.showLoginPage, name="login"),
    path("Logout/", views.showLogoutPage, name="logout"),

    #ZARZADZANIE INNYMI
    path('update-balance/', views.update_balance, name='update_balance'),
    path("addAuction/", views.actionAuction, name="addAuction"),



]