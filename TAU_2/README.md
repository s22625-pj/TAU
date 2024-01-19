# Testy Automatyczne

## Test 1: Rejestracja na GitHub

### Opis Testu
Ten test automatyzuje proces nawigacji ze strony głównej GitHub do strony rejestracji przy użyciu przeglądarki Chrome.

### Jak Uruchomić
1. Zainstaluj Pythona na swoim komputerze.
2. Zainstaluj niezbędne zależności: `pip install selenium`.
3. Uruchom skrypt: `python test_chrome.py`.

## Test 2: Wyszukiwanie w Google

### Opis Testu
Ten test automatyzuje proces wyszukiwania w Google przy użyciu przeglądarki Edge. Akceptuje okno z informacją o cookies i wyszukuje frazy "github".

### Jak Uruchomić
1. Zainstaluj Pythona na swoim komputerze.
2. Zainstaluj niezbędne zależności: `pip install selenium`.
3. Uruchom skrypt: `python test_edge.py`.

### Scenariusze Testów

#### Scenariusz 1: Nawigacja ze Strony Głównej GitHub do Strony Rejestracji

1. **Krok 1: Otwórz Stronę Główną GitHub**
   - Otwórz stronę główną GitHub: [https://github.com](https://github.com).

2. **Krok 2: Kliknij na Zarejestruj Się**
   - Kliknij na link "Zarejestruj się".

3. **Krok 3: Zweryfikuj Przekierowanie do Strony Rejestracji**
   - Zweryfikuj, czy zostałeś przekierowany do strony rejestracji.

#### Scenariusz 2: Wyszukaj w Google frazę "github"

1. **Krok 1: Otwórz Google**
   - Otwórz główną stronę Google: [https://www.google.com](https://www.google.com).

2. **Krok 2: Akceptuj Okno z Informacją o Cookies**
   - Akceptuj okno z informacją o cookies, jeśli się pojawi.

3. **Krok 3: Wprowadź "github" w Pole Wyszukiwania**
   - Wprowadź frazę "github" w pole wyszukiwania.

4. **Krok 4: Zweryfikuj Wyniki Wyszukiwania**
   - Zweryfikuj, czy strona wyników wyszukiwania zawiera odpowiednie informacje na temat "github".

### Uwaga
- Upewnij się, że twój komputer jest podłączony do internetu podczas wykonania testów.
- Dostosuj czasy oczekiwania w skryptach testowych, jeśli to konieczne.
