# Testowanie Wydajnościowe z JMeter

## Wprowadzenie
Celem zadania było przetestowanie wydajności dowolnej aplikacji przy użyciu narzędzia JMeter. Poniżej wyniki testów oraz wnioski na temat działania aplikacji w różnych scenariuszach obciążenia.

## Narzędzia i Konfiguracja
- **Narzędzie:** JMeter
- **Liczba próbek:** 1000 (500 próbek dla każdej z dwóch etykiet)
- **Scenariusze:** Testy przeprowadzone dla dwóch etykiet - `pja.edu.pl` i `github.com/s22625-pj`

## Wyniki

### Etykieta: pja.edu.pl
- **Średni czas odpowiedzi:** 18 331 ms
- **Mediana:** 18 246 ms
- **90% linii:** 31 472 ms
- **95% linii:** 33 102 ms
- **99% linii:** 34 332 ms
- **Minimum:** 1 663 ms
- **Maksimum:** 34 818 ms
- **% błędów:** 0,000%
- **Przepustowość:** 12,56 transakcji na sekundę
- **KB/sek:** 889,02 KB/sek
- **Wysłano KB/sek:** 1,41 KB/sek

### Etykieta: github.com/s22625-pj
- **Średni czas odpowiedzi:** 256 ms
- **Mediana:** 239 ms
- **90% linii:** 304 ms
- **95% linii:** 332 ms
- **99% linii:** 602 ms
- **Minimum:** 212 ms
- **Maksimum:** 787 ms
- **% błędów:** 0,000%
- **Przepustowość:** 13,04 transakcji na sekundę
- **KB/sek:** 4539,75 KB/sek
- **Wysłano KB/sek:** 1,58 KB/sek

## Wnioski
1. Aplikacja `pja.edu.pl`:
   - Odpowiedź jest akceptowalna, gdy średni czas odpowiedzi utrzymuje się w granicach normy.
   - Anomalia zaczyna się po przekroczeniu 90% linii czasu odpowiedzi, gdzie dochodzi do wzrostu czasu reakcji.

2. Aplikacja `github.com/s22625-pj`:
   - Odpowiedź utrzymuje się na niskim poziomie, co jest pozytywne.
   - Anomalia zaczyna się w okolicach 99% linii czasu odpowiedzi, gdzie pojawiają się wyższe czasy reakcji.

3. Ogólne wnioski:
   - Brak błędów w obu przypadkach jest pozytywnym sygnałem.
   - Przepustowość dla obu etykiet utrzymuje się na zadowalającym poziomie.
   - Należy monitorować i reagować na wzrost czasów odpowiedzi, zwłaszcza w przypadku aplikacji `pja.edu.pl` po przekroczeniu 90% linii czasu odpowiedzi.

## Inne Informacje
- Plik CSV z pełnymi wynikami testów: `jmeter_aggregate.csv`
