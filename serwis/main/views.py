from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Auta, AutaSprzedane
from .models import balance
from .models import CreateUserForm
from .models import AddAuctionForm
from .models import DelAUctionForm


#Do platnosc paypal
import paypalrestsdk
from django.conf import settings
from django.urls import reverse

#Do platnosci dotpay
import hashlib, json, hmac



################# || ############################# || #############
#               # || #          Rendering        # || #           #
################# \/ ############################# \/ #############

#renderowanie strony bazowej
def index(request):
    return render(request, "main/base.html", {})


#renderowanie strony homepage.html
def showHomePage(request):
    if request.user.is_authenticated:

        if not balance.objects.filter(user=request.user).exists(): # sprawdź, czy użytkownik ma już konto w tabeli balansów
            instance = balance(user=request.user, balance=100) # utwórz nowy rekord dla użytkownika
            instance.save()


        user = balance.objects.get(user=request.user)
        context = {'balance': user.balance}
    else: context={}
    return render(request, "main/homepage.html",context)




#renderowanie strony auction.html
def showAuctionPage(request):
    if request.user.is_authenticated:
        auta = Auta.objects.all()
        typ_paliwa = request.GET.get('fuels')
        typ_sortowania = request.GET.get('sorts')
        slowo = request.GET.get('search')

        if   typ_paliwa: auta = Auta.objects.filter(paliwo=typ_paliwa)
        if   slowo: auta = auta.filter(nazwa__contains=slowo)

        if   typ_sortowania == 'tanie':        auta = auta.order_by('cena')
        elif typ_sortowania == 'drogie':       auta = auta.order_by('-cena')
        elif typ_sortowania == 'popularne':    auta = auta.order_by('-popularnosc')
        elif typ_sortowania == 'niepopularne': auta = auta.order_by('popularnosc')
        elif typ_sortowania == 'mocmin':       auta = auta.order_by('moc')
        elif typ_sortowania == 'mocmax':       auta = auta.order_by('-moc')
        elif typ_sortowania == 'spalaniemin':  auta = auta.order_by('spalanie')
        elif typ_sortowania == 'spalaniemax':  auta = auta.order_by('-spalanie')

        user = balance.objects.get(user=request.user)
        context = {'auta':auta,'balance': user.balance}
    else: context={} 
    return render(request, "main/auction.html",context)




#renderowanie strony contact.html
def showContactPage(request):
    if request.user.is_authenticated:
        user = balance.objects.get(user=request.user)
        context = {'balance': user.balance}
    else: context={}
    return render(request, "main/contact.html", context)




#renderowanie strony contact.html
def showArchivePage(request):
    if request.user.is_authenticated:
        auta = AutaSprzedane.objects.all()
        typ_paliwa = request.GET.get('fuels')
        typ_sortowania = request.GET.get('sorts')
        slowo = request.GET.get('search')

        if   typ_paliwa: auta = AutaSprzedane.objects.filter(paliwo=typ_paliwa)
        if   slowo: auta = auta.filter(nazwa__contains=slowo)

        if   typ_sortowania == 'tanie':        auta = auta.order_by('cena')
        elif typ_sortowania == 'drogie':       auta = auta.order_by('-cena')
        elif typ_sortowania == 'popularne':    auta = auta.order_by('-popularnosc')
        elif typ_sortowania == 'niepopularne': auta = auta.order_by('popularnosc')
        elif typ_sortowania == 'mocmin':       auta = auta.order_by('moc')
        elif typ_sortowania == 'mocmax':       auta = auta.order_by('-moc')
        elif typ_sortowania == 'spalaniemin':  auta = auta.order_by('spalanie')
        elif typ_sortowania == 'spalaniemax':  auta = auta.order_by('-spalanie')

        user = balance.objects.get(user=request.user)
        context = {'auta':auta,'balance': user.balance}
    else: context={} 
    return render(request, "main/archive.html",context)

#renderowanie strony poprawnej platnosc dotpay
def showDotpaySucess(request):
    if request.user.is_authenticated:
        id = request.GET.get('id')

        if request.user.first_name: userid = user.first_name
        else: userid = request.user.username

        try:auto = Auta.objects.get(id=id)
        except Auta.DoesNotExist: return "Samochód o podanym ID nie istnieje"

        auto_sprzedane = AutaSprzedane(
            nazwa=auto.nazwa,
            zdj_url=auto.zdj_url,
            cena=auto.cena,
            model=auto.model,
            popularnosc=auto.popularnosc,
            paliwo=auto.paliwo,
            spalanie=auto.spalanie,
            typ=auto.typ,
            moc=auto.moc,
            uzytkownik=userid
        )
        auto_sprzedane.save()
        auto.delete()

        user = balance.objects.get(user=request.user)
        context = {'auto':auto,'balance': user.balance}
    else: context={} 
    return render(request, "main/archive.html", context)


#renderowanie strony poprawnej platnosc dotpay
def returnCar(request,id):
    if request.user.is_authenticated:
        try:auto_wycofane = AutaSprzedane.objects.get(id=id)
        except AutaSprzedane.DoesNotExist: return "Samochód o podanym ID nie istnieje"

        auto = Auta(
            nazwa=auto_wycofane.nazwa,
            zdj_url=auto_wycofane.zdj_url,
            cena=auto_wycofane.cena,
            model=auto_wycofane.model,
            popularnosc=auto_wycofane.popularnosc,
            paliwo=auto_wycofane.paliwo,
            spalanie=auto_wycofane.spalanie,
            typ=auto_wycofane.typ,
            moc=auto_wycofane.moc,
        )
        auto.save()
        auto_wycofane.delete()

        user = balance.objects.get(user=request.user)
        context = {'auto':auto,'balance': user.balance}
    else: context={} 
    return render(request, "main/archive.html", context)


################# /\ ############################# /\ #############
#               # || #      End of Rendering     # || #           #
################# || ############################# || #############




################# || ############################# || #############
#               # || #        User systems       # || #           #
################# \/ ############################# \/ #############

#rejestracja
def showSignupPage(request):
    if request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('firstname')
            user = authenticate(username=username, password=password, first_name=first_name)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            instance = balance(user = request.user, balance = 100)
            instance.save()

            return redirect('/')
        else: return render(request, 'main/signup.html', {'form': form})
    else:
        form = CreateUserForm()
        return render(request, 'main/signup.html', {'form': form})

#logowanie
def showLoginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else: return redirect('/signup/')
        else: 
            context = {'form': form, 'error_message': 'Nieprawidłowa nazwa użytkownika lub hasło.'}
            return render(request, 'main/login.html', context)
    else: return render(request, 'main/login.html', {'form': AuthenticationForm()})


#wylogowanie
login_required
def showLogoutPage(request):
    logout(request)
    return redirect('/')

#zarzadzanie waluta zalogowanego uzytkownika, dodaje albo odejmuje
login_required
def update_balance(request):
    if request.method == 'POST':
        user = balance.objects.get(user=request.user)
        if 'add' in request.POST: user.balance += 5
        elif 'subtract' in request.POST: user.balance -= 5
        user.save()
        return redirect('/')
    else: return render(request, 'main/auction.html')

################# /\ ############################# /\ #############
#               # || #    End of User systems    # || #           #
################# || ############################# || #############





################# || ############################# || #############
#               # || #    Auctions management    # || #           #
################# \/ ############################# \/ #############

def actionAuction(request):

    if request.method == 'POST':
        add_form = AddAuctionForm(request.POST)
        del_form = DelAUctionForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('/Auction/')
        
        elif del_form.is_valid():
            id = del_form.cleaned_data['id'].id
            Auta.objects.filter(id=id).delete()
            return redirect('/Auction/')
    
    else:
        add_form = AddAuctionForm()
        del_form = DelAUctionForm()

    context = {
        'add_form': add_form,
        'del_form': del_form,
    }
    return render(request, 'main/addAuction.html', context)

################# /\ ############################# /\ #############
#               # || # End of Auction management # || #           #
################# || ############################# || #############





################# || ############################# || #############
#               # || #       Paypal payment      # || #           #
################# \/ ############################# \/ #############

def paypalSite(request):
    if request.method == 'POST':
        paypalrestsdk.configure({
            "mode": "sandbox" if settings.DEBUG else "live",
            "client_id": settings.PAYPAL_CLIENT_ID,
            "client_secret": settings.PAYPAL_CLIENT_SECRET
        })

        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": request.build_absolute_uri(reverse('payment_success')),
                "cancel_url": request.build_absolute_uri(reverse('payment_cancel'))
            },
            "transactions": [{
                "amount": {
                    "total": "10.00", 
                    "currency": "USD" 
                },
                "description": "Opis płatności"
            }]
        })

        if payment.create():
            for link in payment.links:
                if link.method == 'REDIRECT':
                    redirect_url = str(link.href)
                    return HttpResponseRedirect(redirect_url)
        else: print(payment.error) 
    return render(request, 'main/paypalTutorial.html')

################# /\ ############################# /\ #############
#               # || #   End of Paypal payment   # || #           #
################# || ############################# || #############





################# || ############################# || #############
#               # || #       Dotpay payment      # || #           #
################# \/ ############################# \/ #############

#do funkcji dotpay()
def gen_checksum(amount: int, description: any, currency: str, url: str, type: int):
    DOTPAY_PIN = '5DZW0YRq2w46bDWOJukzngQcEKbi3Xdj'
    DOTPAY_ID = '746170'
    subscription = {
        "price": str(amount),
        "description": str(description),
        "url": str(url),
        "type": str(type),
    }
    currency = str(currency)
    paramsArr = {
        "amount": subscription["price"],
        "currency": currency,
        "description": subscription["description"],
        "id": DOTPAY_ID,
        "paramsList": "amount;currency;description;id;type;url",
        "type": subscription["type"],
        "url": subscription["url"],
    }
    paramsArrJson = json.dumps(paramsArr, separators=(",", ":"))
    chk = hmac.new(DOTPAY_PIN.encode("utf-8"), msg=paramsArrJson.encode("utf-8"), digestmod=hashlib.sha256)
    checksum = chk.hexdigest()
    return checksum

#Dotpay payment
login_required
def dotpaySite(request,cena, model,id):
    DOTPAY_ID  = 746170
    DOTPAY_AMOUNT = cena
    DOTPAY_CURRENCY = "PLN"
    DOTPAY_DESCRIPTION = "zaplata za auto (numer katalogowy: {}) {}".format(id,model)
    DOTPAY_URL = "http://127.0.0.1:8000/Dotpay-Success/?id={}".format(id)
    DOTPAY_TYPE = 4
    DOTPAY_CHECKSUM = gen_checksum(DOTPAY_AMOUNT,DOTPAY_DESCRIPTION,DOTPAY_CURRENCY,DOTPAY_URL,DOTPAY_TYPE)
    dotpay_url = "https://ssl.dotpay.pl/test_payment/?id={}&amount={}&currency={}&description={}&chk={}&url={}&type={}".format(
                             DOTPAY_ID,DOTPAY_AMOUNT,DOTPAY_CURRENCY,DOTPAY_DESCRIPTION,DOTPAY_CHECKSUM,DOTPAY_URL,DOTPAY_TYPE)
    return redirect(dotpay_url)

################# /\ ############################# /\ #############
#               # || #   End of Dotpay payment   # || #           #
################# || ############################# || #############