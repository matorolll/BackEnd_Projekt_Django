from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Auta
from .models import balance
from .models import CreateUserForm
from .models import AddAuctionForm
from .models import DelAUctionForm


########################### RENDEROWANIE ###########################

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
        user = balance.objects.get(user=request.user)
        context = {'auta':auta,
                'balance': user.balance}
    else: context={} 
    return render(request, "main/auction.html",context)

#renderowanie strony contact.html
def showContactPage(request):
    if request.user.is_authenticated:
        user = balance.objects.get(user=request.user)
        context = {'balance': user.balance}
    else: context={}
    return render(request, "main/contact.html", context)

####################################################################



####################### SYSTEMY UZYTKOWNIKA ########################

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

##################### ZARZADZANIE AUKCJAMI ########################

#widok do dodawania i usuwania aukcji
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

####################################################################
