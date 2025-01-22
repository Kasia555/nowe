from folder_aplikacji.models import Osoba, Stanowisko
from folder_aplikacji.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# Tworzymy nowe obiekty
stanowisko = Stanowisko.objects.create(nazwa="Kierownik", opis="Zarządza tymi co zarządzają")
osoba = Osoba.objects.create(imie="Jan", nazwisko="Malinowski", plec="2", stanowisko=stanowisko)

# Inicjalizacja serializera dla Osoba
osoba_serializer = OsobaSerializer(osoba)
print(osoba_serializer.data)
# Przykład: {'id': 6, 'imie': 'Jan', 'nazwisko': 'Malinowski', 'plec': 'Mężczyzna', 'stanowisko.id': 4, 'data_dodania': osoba.data_dodania}

# Serializacja do JSON
osoba_json = JSONRenderer().render(osoba_serializer.data)
print(osoba_json)
# Oczekiwany wynik: {'id': 6, 'imie': 'Jan', 'nazwisko': 'Malinowski', 'plec': 'Mężczyzna', 'stanowisko': 4, 'data_dodania': "2025-01-22"}

# Strumień danych JSON
stream = io.BytesIO(osoba_json)

# Pasowanie JSON do słownika
data = JSONParser().parse(stream)

# Tworzymy obiekt deserializera dla danych JSON
deserializer = OsobaSerializer(data=data)

# Walidacja danych
print(deserializer.is_valid())  # True
print(deserializer.errors)      # []

# Błędne dane
invalid_data = {'imie': 'Adam', 'nazwisko': 'Nowak', 'plec': 'Nieznane', 'stanowisko': stanowisko.id}
invalid_serializer = OsobaSerializer(data=invalid_data)
print(invalid_serializer.is_valid())  # False
print(invalid_serializer.errors)      # {'plec': ['"Nieznany" is not a valid choice.']}

# Zapis do BD
if deserializer.is_valid():
    deserializer.save()

# Inicjowanie serializera dla Stanowiska
stanowisko_serializer = StanowiskoSerializer(stanowisko)
print(stanowisko_serializer.data)
# Przykład: {'id': 1, 'nazwa': 'Kierownik', 'opis': 'Zarządza tymi co zarządzają'}

# Serializacja do JSON
stanowisko_json = JSONRenderer().render(stanowisko_serializer.data)
print(stanowisko_json)
# Oczekiwany wynik: {'id': 1, 'nazwa': 'Kierownik', 'opis': 'Zarządza tymi co zarządzają'}

# Deserializacja z JSON
stream = io.BytesIO(stanowisko_json)
data = JSONParser().parse(stream)

deserializer = StanowiskoSerializer(data=data)
print(deserializer.is_valid())

if deserializer.is_valid():
    deserializer.save()




