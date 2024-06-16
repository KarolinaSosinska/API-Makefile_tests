# API Test Projekt

## Zadanie 1: Automatyzacja testów API z wykorzystaniem curl

### Wymagania:
- Python
- pycurl

### Instrukcja uruchomienia:
1. Zainstaluj bibliotekę `pycurl`:
    ```sh
    pip install pycurl
    ```
2. Uruchom skrypt `api_tests.py`:
    ```sh
    python api_tests.py
    ```

### Opis skryptu:
- Skrypt wysyła żądania GET do wybranych endpointów API.
- Sprawdza status odpowiedzi HTTP.
- Parsuje odpowiedzi JSON i sprawdza obecność kluczowych elementów.
- Wyniki są wyświetlane w czytelny sposób.

# Makefile App Projekt

## Zadanie 2: Automatyzacja procesów z wykorzystaniem Makefile

### Wymagania:
- Python

### Instrukcja uruchomienia:
1. Zainstaluj zależności:
    ```sh
    make install
    ```
2. Uruchom testy jednostkowe:
    ```sh
    make test
    ```
3. Uruchom aplikację:
    ```sh
    make run
    ```

### Opis plików:
- `app.py`: Prosta aplikacja z funkcją `FunkcjaKwadratowa`.
- `test_app.py`: Testy jednostkowe dla aplikacji.
- `Makefile`: Plik Makefile automatyzujący instalację zależności, testowanie i uruchamianie aplikacji.
