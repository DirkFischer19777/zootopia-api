# 🦁 Zootopia API Web Generator

Dieses Projekt kombiniert die **[API Ninjas Animals API](https://api-ninjas.com/api/animals)** mit einem Python-HTML-Generator, um eine kleine Website mit Tierinformationen zu erstellen.  

Der Benutzer gibt ein Tier ein → die Daten werden von der API geladen → und in eine HTML-Seite (`animals.html`) eingefügt.

---

## 📂 Projektstruktur

zootopia-api/

 - data_fetcher.py # Lädt Tierdaten von der API
- animals_web_generator.py # Erzeugt eine HTML-Seite mit den Tierinfos
- animals_template.html # HTML-Template mit Platzhalter "REPLACE_ANIMALS_INFO"
- requirements.txt # Python-Abhängigkeiten
- .env # enthält den API_KEY



---

## 🚀 Features

- Abfrage von Tierdaten per **API Ninjas Animals API**  
- Darstellung von **Name, Diet, Location und Type**  
- Automatische Erstellung einer Webseite (`animals.html`)  
- Meldung, wenn das Tier nicht existiert  

---

## 📦 Installation

1. Repository klonen:
   ```bash
   git clone https://github.com/DirkFischer19777/zootopia-api.git

2. Virtuelle Umgebung erstellen und aktivieren:
    - python -m venv venv 
    - source venv/bin/activate   # Mac/Linux 
    - venv\Scripts\activate      # Windows


3. Abhängigkeiten installieren:
    - pip install -r requirements.txt


4. API Key besorgen von API Ninjas
    Datei .env im Projektordner anlegen und folgenden Eintrag hinzufügen:
    API_KEY=dein_api_schlüssel

## ▶️ Nutzung
1. Programm starten: python animals_web_generator.py

2. Tiernamen eingeben (z. B. lion).
3. Die generierte Webseite animals.html öffnen
    