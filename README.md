# BackEnd_Projekt_Django
Django+Bootstrap+mysql

Celem projektu jest kontynuacj projektu z repo frontendu, przepisanie z reacta+js na django, dodanie logowania poprzez media oraz sposobu płatności online

Instrukcja do instalacji i uruchomienia:


Instalacja Dockera i uruchomienie bazy danych
  1. Przechodzimy na strone dockera i pobieramy najnowsza wersje desktop https://docs.docker.com/desktop/install/windows-install/
  2. Instalujemy dockera z ustawieniam podstawowymi
  3. Pobieramy obraz kontenera obrazMySql.tar z dysku google https://drive.google.com/drive/folders/1m82G2kfLlRYtmyk5FjUq1miaSpiESsNy?usp=sharing
  4. Instalujemy go lokalnie na dockerze poprzez komende docker load -i obrazMySql.tar
  5. Uruchamiamy kontener docker run obrazMySql


Dodatkowo do podglądu można pobrać MySQL Workbench i podłączyć bazę w celu wyświetlania zawartość
Standard(TCP/IP) , 127.0.0.1:3306 , root root
  
 
Uruchomienie projektu django
  1. Pobieramy caly projekt, w terminalu będąc w tym folderze (na poziomie manage.py) używamy następujących komend:
    python manage.py runserver       - Główna komenda do uruchamiana serwera
    python manage.py makemigrations  - Tworzy pliki migracyjne (używać gdy zmieniana jest struktura bazy danych)
    python manage.py migrate         - Przesyła pliki migracyjne i zmienia strukture bazy danych
    python manage.py createsuperuser - Tworzy admina w celu dostępu do dashboarda
  
  2. Dostęp do projektu poprzez 127.0.0.1:8000
  
![image](https://user-images.githubusercontent.com/121674957/235900345-b62ed8db-1563-4e7c-9871-c28f4f1f778e.png)
 
Lista zadań do wykonania
- [x] Instalacja mysql, docker
- [x] Przepisanie podstron z js na django
- [x] Utworzenie widokow, url
- [x] Utworzenie modeli dla uzytkownikow
- [ ] Dodanie dostepu do panelu administratora
- [ ] Podlaczenie z mysql
- [ ] ---
- [ ] Dodanie Rejestracji nowych kont w mysql poprzez formularz
- [ ] Dodanie Logowania na konta w mysql poprzez formularz
- [ ] Dodanie wylogowywania
- [ ] Dodanie strone z zarzadzaniem aukcjami
- [ ] Utworzyc funkcjonalnosc dodawania / usuwania aukcji
- [ ] Dodanie funkcjonalnosc modyfikacji aukcji
- [ ] Dodanie filtrowanie po typie paliwa
- [ ] Dodanie filtrowanie po typie nadwozia
- [ ] Dodanie wyszukiwanie po tekscie
- [ ] Dodanie prywatnego portfela
- [ ] Zarzadzanie portfelem (mysql) ze strony
- [ ] ---
- [ ] Dodanie rejestracji i logowania poprzez google
- [ ] Edycja panelu logowania przez google
- [ ] ---
- [ ] Dodanie mozliwosc platnosci online
- [ ] Dodanie funkcjonalonosc zmiany wartosc portfela poprzez platnosc online
- [ ] ---
- [ ] Dodanie podstrony Archiwum z aukcjami juz wykupionymi
- [ ] Dodanie mozliwosc zakupu aukcji (aukcja zostaje przeniesiona z Aukcje do Archiwum oraz do innej tabeli mysql)
- [ ] Poprawa styli bootstrap na calej stronie
- [ ] Poprawa wygladu Aukcji 
- [ ] Poprawa wygladu dodawania / usuwania aukcji
- [ ] Dodanie mozliwosc wyrejestrowania uzytkownika






