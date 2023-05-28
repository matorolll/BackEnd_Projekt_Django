from django.urls import path
from . import views

urlpatterns = [
    #GENEROWANIE WIDOKOW
    path("", views.showHomePage, name="home"),
    path("Auction/", views.showAuctionPage, name="auction"),
    path("Archive/", views.showArchivePage, name="archive"),
    path("Contact/", views.showContactPage, name="contact"),

    #ZARZADZANIE UZYTKOWNIKIEM
    path("Signup/", views.showSignupPage, name="signup"),
    path("Login/", views.showLoginPage, name="login"),
    path("Logout/", views.showLogoutPage, name="logout"),

    #ZARZADZANIE INNYMI
    path('update-balance/', views.update_balance, name='update_balance'),
    path("addAuction/", views.actionAuction, name="addAuction"),

    #ZARZADZANIE PLATNOSCIAMI
    path("Paypal-checkout/", views.paypalSite, name='paypalTutorial'),
    path("Dotpay-checkout/<int:cena>/<str:model>/<int:id>", views.dotpaySite, name='dotpay'),
    path("Dotpay-Success/", views.showDotpaySucess, name="dotpaysuccess"),

    path("Return-Car/<int:id>", views.returnCar, name="returncar"),
]