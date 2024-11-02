# Uniwersalny Kalkulator Załamania Światła

Interaktywna aplikacja webowa do obliczania i wizualizacji zjawiska załamania światła na granicy dwóch ośrodków.

## Funkcjonalności

### 1. Obliczenia kątów
- Obliczanie kąta załamania światła na podstawie kąta padania
- Wykrywanie zjawiska całkowitego wewnętrznego odbicia
- Interaktywna wizualizacja promieni: padającego, odbitego i załamanego
- Możliwość wyboru predefiniowanych materiałów lub własnych współczynników załamania

### 2. Baza materiałów
- Wbudowana baza współczynników załamania dla różnych materiałów:
  - Próżnia (n=1.0)
  - Powietrze (n=1.000293)
  - Woda (n=1.333)
  - Szkło zwykłe (n=1.52)
  - Szkło kryształowe (n=1.66)
  - Diament (n=2.417)
  - Pleksiglas (n=1.49)
  - Gliceryna (n=1.473)

### 3. Kalkulator kąta krytycznego
- Obliczanie kąta krytycznego dla zjawiska całkowitego wewnętrznego odbicia
- Sprawdzanie warunków występowania zjawiska
- Szczegółowe wyjaśnienia i wzory

## Interfejs
- Intuicyjny podział na zakładki tematyczne
- Dynamiczna wizualizacja na canvas
- Interaktywny diagram pokazujący:
  - Promień padający (czerwony)
  - Promień odbity (zielony)
  - Promień załamany (niebieski)
  - Normalną (linia przerywana)
  - Kąty padania i załamania

## Technologie
- HTML5
- CSS3 (Grid Layout, Flexbox)
- JavaScript (Canvas API)
- Responsywny design

## Zastosowanie edukacyjne
Narzędzie jest szczególnie przydatne w:
- Nauczaniu fizyki optycznej
- Demonstracji zjawisk optycznych
- Zrozumieniu zachowania światła na granicy ośrodków
- Praktycznych obliczeniach dla systemów optycznych

## Wzory i obliczenia
- Prawo Snella: n₁sin(α) = n₂sin(β)
- Kąt krytyczny: α_kr = arcsin(n₂/n₁)
- Warunek całkowitego wewnętrznego odbicia: n₁ > n₂