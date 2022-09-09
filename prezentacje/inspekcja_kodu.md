## Wstęp

* Inspekcja (recenzja) kodu, z angielskiego "Code Review" to powszechna praktyka w dziedzinie inżynierii oprogramowania.
* Polega na przeczytaniu oraz ocenianiu kodu przez programistę niebędącego jego autorem w celu autoryzacji, oraz akceptacji jakości przed włączeniem go do bazy kodu.
* Częstą praktyką jest otwarcie Pull Request w serwisie GitHub.

## Cele

* Potwierdzenie, że kod spełnia wymagania klienta.
* Wykrycie błędów (bugów) w kodzie.
* Sprawdzenie, czy styl kodu zgadza się ze stylem wybranym przez zespół.
* Ewentualnie danie wskazówek do poprawienia czytelności lub architektury kodu.

*Styl tutaj odnosi się nie tylko do kwestii takich jak formatowanie, czy nazewnictwo, ale wszystkich standardów jakości, czyli też użycie odpowiednich wzorców projektowych, podział testów między jednostkowe, funkcjonalne i integracyjne.*

## Proces

* Autor kodu samodzielnie sprawdza swój kod.
* Autor kodu oddaje kod do recenzji.
* Recenzenci dzielą się swoimi spostrzeżeniami i uwagi.
* Autor refaktoryzuje kod i ponownie oddaje go do recenzji.
* Recenzenci akceptują kod i integrują go z bazą kodu.

## Korzyści

* Świadomość, że kod zostanie oceniony przez innych programistów, wywiera presję na autorze mającą podnieść próg jakości.
• Zmusza autora kodu do usprawiedliwienia swoich decyzji.
* Daje możliwość, dzielenia się wiedzą między członkami zespołu.
* Każdy członek zespołu wie coś o tym, co robią inni programiści.
* Łatwiej jest unikać powtórzeń w pisanym kodzie (wiedząc, co napisali inni, mogę korzystać z gotowych rozwiązań).
• Rozdzielenie odpowiedzialności za kod między kilku członków zespołu.

## Powszechne problemy

* Recenzent szuka jedynie powierzchownych problemów (literówki, nieścisłości w formatowaniu itd.).
* Recenzent usiłuje wymusić użycie swoich nawyków pisania kodu na ocenianym kodzie.
* Recenzent nie zna wymagań, które autor kodu otrzymał od klienta.

## Jak nie przeprowadzać inspekcji kodu?

* Jeśli recenzje używane są do negocjacji wynagrodzenia bądź awansu to programiści szybko zaczną sobie rzucać kłody pod nogi.
* Recenzje powinny być prowadzone jedynie w gronie programistów, żadna nietechniczna osoba nie ma przy nich prawa bytu.
* Recenzje mogą budzić negatywne emocje, język używany w komentarzach powinien być ściśle nadzorowany.
