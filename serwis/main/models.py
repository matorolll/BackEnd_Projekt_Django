from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

########################### BAZA DANYCH ###########################

#Glowny model aut, odpowiada za tabele w mysql auta
class Auta(models.Model):
    id= models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=255)
    zdj_url = models.CharField(max_length=255,default="https://media.istockphoto.com/id/1281739158/vector/car-vector-logo-fit-for-automotive-repair-transportation-or-car-shop-logo-flat-color-style.jpg?s=612x612&w=0&k=20&c=cuUSEnzQUQZ7sLfsoFmaKoMxLtCMMYVM2nh3QvhbEMc=")
    cena = models.IntegerField(default="666")
    model = models.CharField(max_length=255,default="null")
    popularnosc = models.IntegerField(default="0")
    paliwo = models.CharField(max_length=255,default="null")
    spalanie = models.FloatField(default=0.0)
    typ = models.CharField(max_length=255,default="null")
    moc = models.IntegerField(default="0")
    class Meta:
        db_table = 'auta'



#Glowny model portfela, odpowiada za tabele w mysql portfel
class balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default = 0)
    class Meta:
        db_table = 'portfel'

##################################################################


########################### FORMULARZE ###########################

#zmienia podatawowy model formularza do rejestracji i dodaje pola fields
class CreateUserForm(UserCreationForm):
    class  Meta:
        model = User
        fields = ['username', 'password1','password2', 'first_name']


class AddAuctionForm(forms.ModelForm):
    class Meta:
        model = Auta
        fields = ('nazwa','zdj_url','cena','model','popularnosc','paliwo','spalanie','typ','moc')


class DelAUctionForm(forms.Form):
    id  = forms.ModelChoiceField(queryset=Auta.objects.all())

##################################################################
