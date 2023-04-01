# Wstęp

* Inspekcja (recenzja) kodu, znana również jako "Code Review", to popularna praktyka w inżynierii oprogramowania.
* Polega ona na przeczytaniu i ocenie kodu przez programistę niebędącego jego autorem, celem autoryzacji i akceptacji jakości kodu przed jego włączeniem do bazy kodu.
* Często w tym celu otwierane są Pull Requesty w serwisie GitHub.

# Cele

* Potwierdzenie, że kod spełnia wymagania klienta.
* Wykrycie błędów (bugów) w kodzie.
* Sprawdzenie zgodności stylu kodu ze stylem wybranym przez zespół.
* Ewentualne podanie wskazówek do poprawienia czytelności lub architektury kodu.
* Styl tutaj odnosi się nie tylko do kwestii takich jak formatowanie czy nazewnictwo, ale także do wszystkich standardów jakości, w tym użycia odpowiednich wzorców projektowych oraz podziału testów na jednostkowe, funkcjonalne i integracyjne.

# Proces

* Autor kodu samodzielnie sprawdza swój kod.
* Autor kodu oddaje kod do recenzji.
* Recenzenci dzielą się swoimi spostrzeżeniami i uwagami.
* Autor refaktoryzuje kod i ponownie oddaje go do recenzji.
* Recenzenci akceptują kod i integrują go z bazą kodu.

# Korzyści

*  Poprawa jakości kodu poprzez wykrywanie błędów i niedociągnięć.
* Zwiększenie czytelności i zrozumienia kodu przez innych programistów, co ułatwia jego późniejsze modyfikowanie i utrzymanie.
* Wymiana doświadczeń i wiedzy między członkami zespołu.
* Usprawnienie procesu tworzenia oprogramowania poprzez lepsze planowanie i rozdzielenie odpowiedzialności.
* Zwiększenie zaangażowania i motywacji członków zespołu poprzez współodpowiedzialność za kod.
* Poprawa wizerunku firmy poprzez dostarczanie klientom wysokiej jakości produktów.

# Powszechne problemy

* Recenzenci szukają jedynie powierzchownych problemów, takich jak literówki czy nieścisłości w formatowaniu, zamiast skupiać się na krytycznych aspektach kodu.
* Recenzenci usiłują narzucić swój styl pisania kodu na ocenianym kodzie, zamiast skupić się na jego jakości.
* Recenzenci nie znają wymagań, które autor kodu otrzymał od klienta, co może prowadzić do niepotrzebnych sugestii i spowolnienia procesu.
* Autor kodu może mieć trudności z przyjęciem krytyki i sugestii, co może prowadzić do oporu wobec zmian i negatywnych emocji.
* Brak odpowiedniej komunikacji i współpracy między autorem a recenzentami może spowodować opóźnienia i nieporozumienia.

# Wskazówki dotyczące prawidłowego przeprowadzania inspekcji kodu

* Jeśli recenzje są używane jako narzędzie do negocjacji wynagrodzenia lub awansu, programiści mogą zacząć rywalizować ze sobą i rzucać sobie kłody pod nogi, co może prowadzić do niezdrowej atmosfery w zespole i pogorszenia jakości kodu.
* Recenzje powinny być przeprowadzane wyłącznie w gronie programistów, ponieważ osoby nietechniczne mogą nie mieć wystarczającej wiedzy i doświadczenia, aby odpowiednio ocenić kod.
* Recenzje mogą być źródłem negatywnych emocji dla autora kodu, dlatego ważne jest, aby język używany w komentarzach był ściśle nadzorowany i niezrażający dla innych. Warto również pamiętać o tym, aby skupić się na merytorycznych aspektach kodu, a nie na osobach.
