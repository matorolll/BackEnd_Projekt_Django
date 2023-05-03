# BackEnd_Projekt_Django
Django+Bootstrap+mysql

Celem projektu jest kontynuacj projektu z repo frontendu, przepisanie z reacta+js na django, dodanie logowania poprzez media oraz sposobu płatności online
Poprzednia wersje projektu znajdziemy pod: https://github.com/matorolll/React_projekt/tree/master , posiada ona wiecej dzialajacych funkcji oraz poprawniejszy wyglad (wystarczy przepisac z js na pythona)

Instrukcja do instalacji i uruchomienia:


Instalacja Dockera i uruchomienie bazy danych
  1. Przechodzimy na strone dockera i pobieramy najnowsza wersje desktop https://docs.docker.com/desktop/install/windows-install/
  2. Instalujemy dockera z ustawieniam podstawowymi
  3. Pobieramy obraz kontenera obrazMySql.tar z dysku google https://drive.google.com/drive/folders/1m82G2kfLlRYtmyk5FjUq1miaSpiESsNy?usp=sharing
  4. Instalujemy go lokalnie na dockerze poprzez komende docker load -i obrazMySql.tar
  5. Uruchamiamy kontener docker run obrazMySql
  6. Jeżeli nie bedzie domyslnie, musimy zbindowac obraz na 3306:3306

![image](https://user-images.githubusercontent.com/121674957/235904778-b6fab002-ea57-48ad-a38c-9defa03653f1.png)


Dodatkowo do podglądu można pobrać MySQL Workbench i podłączyć bazę w celu wyświetlania zawartość
Standard(TCP/IP) , 127.0.0.1:3306 , root root
  
 
Uruchomienie projektu django
  1. Pobieramy caly projekt, w terminalu będąc w tym folderze (na poziomie manage.py) używamy następujących komend:
    python manage.py runserver       - Główna komenda do uruchamiana serwera
    python manage.py makemigrations  - Tworzy pliki migracyjne (używać gdy zmieniana jest struktura bazy danych)
    python manage.py migrate         - Przesyła pliki migracyjne i zmienia strukture bazy danych
    python manage.py createsuperuser - Tworzy admina w celu dostępu do dashboarda
  
  2. Dostęp do projektu poprzez 127.0.0.1:8000
  3. Przykladowe logowanie user3 useruser itd
  4. Dodajemy plik z autoryzacja google do folderu z dysku google (tam gdzie manage.py)
  
![image](https://user-images.githubusercontent.com/121674957/235900345-b62ed8db-1563-4e7c-9871-c28f4f1f778e.png)
 
Lista zadań do wykonania
- [x] Instalacja mysql, docker
- [x] Przepisanie podstron z js na django
- [x] Utworzenie widokow, url
- [x] Utworzenie modeli dla uzytkownikow
- [x] Dodanie dostepu do panelu administratora
- [x] Podlaczenie z mysql
- [x] ---
- [x] Dodanie Rejestracji nowych kont w mysql poprzez formularz
- [x] Dodanie Logowania na konta w mysql poprzez formularz
- [x] Dodanie wylogowywania
- [x] Dodanie strone z zarzadzaniem aukcjami
- [x] Utworzyc funkcjonalnosc dodawania / usuwania aukcji
- [ ] Dodanie funkcjonalnosc modyfikacji aukcji
- [ ] Dodanie filtrowanie po typie paliwa
- [ ] Dodanie filtrowanie po typie nadwozia
- [ ] Dodanie wyszukiwanie po tekscie
- [x] Dodanie prywatnego portfela
- [x] Zarzadzanie portfelem (mysql) ze strony
- [x] ---
- [x] Dodanie rejestracji i logowania poprzez google
- [x] Edycja panelu logowania przez google
- [x] ---
- [ ] Dodanie mozliwosc platnosci online
- [ ] Dodanie funkcjonalonosc zmiany wartosc portfela poprzez platnosc online
- [x] ---
- [ ] Dodanie podstrony Archiwum z aukcjami juz wykupionymi
- [ ] Dodanie mozliwosc zakupu aukcji (aukcja zostaje przeniesiona z Aukcje do Archiwum oraz do innej tabeli mysql)
- [ ] Poprawa styli bootstrap na calej stronie
- [ ] Poprawa wygladu Aukcji 
- [ ] Poprawa wygladu dodawania / usuwania aukcji
- [ ] Dodanie mozliwosc wyrejestrowania uzytkownika






