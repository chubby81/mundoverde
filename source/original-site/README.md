# mundoverde.ws – Website-Entwurf

Stand: 3. November 2026. Statisches deutschsprachiges Magazin für Nachhaltigkeit, Ökologie, Natur und bewussten Alltag.

## Vorschau
ZIP entpacken und index.html im Browser öffnen. Keine Installation erforderlich. HTML, CSS und JavaScript funktionieren ohne Build. Alle Schriftarten und Illustrationen sind lokal beziehungsweise im Code enthalten. Keine externen Laufzeitbibliotheken, Tracker oder Cookies im Website-Code. Der Hostinganbieter kann dennoch Besuchsdaten verarbeiten.

Enthalten: Startseite, Themenfilter, Suche, sechs eigenständige Beitragsseiten, skalierbare botanische Illustrationen, Favicon, Entwürfe für Impressum und Datenschutz. Responsive Gestaltung mit ein- und zweispaltiger Mobilansicht.

## Vor der öffentlichen Veröffentlichung
- Anbieterangaben im Impressum mit den tatsächlichen Angaben vervollständigen und rechtliche Anforderungen für den konkreten Betrieb prüfen.
- Datenschutzhinweise auf tatsächlichen Betreiber und Hosting abstimmen. Die vorhandene Seite ist ausdrücklich noch keine vollständige Datenschutzerklärung.
- Sechs Beitragsentwürfe inhaltlich redigieren und die externen Leseempfehlungen prüfen. Sie sind keine abgeschlossene wissenschaftliche Quellenprüfung.
- Entwurfshinweise erst danach entfernen.
- Jede HTML-Seite enthält vorsorglich `noindex,nofollow`. Nach Fertigstellung entfernen, wenn Suchmaschinen die Seite aufnehmen sollen. noindex schützt NICHT vor öffentlichem Zugriff.

## GitHub Pages ohne lokale Software einrichten
1. Bei GitHub ein neues öffentliches Repository anlegen, beispielsweise `mundoverde`. Mit GitHub Free muss das Repository für Pages öffentlich sein. Keine Zugangsdaten oder privaten Dateien hochladen.
2. ZIP auf dem eigenen Gerät entpacken. Über „Add file → Upload files“ die enthaltenen Website-Dateien direkt in die oberste Ebene des Repositorys laden und committen. Nicht die ZIP selbst und nicht einen zusätzlichen äußeren Ordner hochladen. index.html muss im Hauptverzeichnis liegen. `.nojekyll` ist optional und unter manchen Dateimanagern unsichtbar; falls möglich mit hochladen. Keine Framework-Konfiguration nötig.
3. „Settings → Pages → Build and deployment“ öffnen. „Deploy from a branch“ wählen, Branch `main`, Ordner `/(root)`, speichern.
4. Nach erfolgreicher Bereitstellung die von GitHub angezeigte github.io-Adresse öffnen und die Seiten prüfen. Die relativen Dateiverweise funktionieren auch unter einem Repository-Unterpfad.
5. Vor der Domain-Anbindung die Domain in den GitHub-Profileinstellungen unter Pages verifizieren. Den von GitHub angezeigten individuellen TXT-Eintrag beim Domainanbieter eintragen. Dies dient dem Schutz vor Domainübernahme.
6. Im Repository unter „Settings → Pages → Custom domain“ `mundoverde.ws` eintragen und speichern. Bei Veröffentlichung aus einem Branch legt GitHub dafür die CNAME-Datei an. Sie ist absichtlich noch nicht im Paket enthalten: zuerst die Seite auf github.io prüfen.
7. Beim Domainanbieter die Domain per A-, ALIAS- oder ANAME-Eintrag entsprechend der aktuellen GitHub-Dokumentation auf GitHub Pages zeigen lassen. Für `www` einen CNAME auf `DEIN-GITHUB-NAME.github.io` setzen, ohne Repositorynamen. Den Platzhalter durch deinen echten Nutzernamen ersetzen. Keine Wildcard-Einträge verwenden. Bestehende E-Mail-Einträge (MX/TXT) nicht pauschal löschen.
8. DNS-Prüfung abwarten und „Enforce HTTPS“ einschalten, sobald verfügbar. GitHub weist darauf hin, dass die Option bis zu 24 Stunden benötigen kann. Beide Varianten, mit und ohne www, testen.

Du benötigst weiterhin die Domainregistrierung und Zugriff auf ihre DNS-Verwaltung, aber keinen zusätzlichen klassischen Webspace. Das Paket ist noch nicht in deinem GitHub-Konto veröffentlicht und deine Domain wurde nicht verändert.

## Beiträge später pflegen
Bestehende HTML-Beitragsseite kopieren, Dateinamen ändern und Titel, Beschreibung, Kategorie, Inhalt und Quellen anpassen. Auf index.html eine passende article.card ergänzen; data-category muss mit dem Filternamen übereinstimmen und data-search die Suchwörter in Kleinschreibung enthalten. `app.js` filtert diese Karten automatisch. Den anfänglichen Zähler auf der Startseite ebenfalls anpassen. Bei vielen Beiträgen ist ein statischer Generator mit Markdown-Beiträgen sinnvoll, damit diese Pflege automatisiert wird. Aktuell gibt es keinen WordPress-artigen Redaktionsbereich.

## Grenzen von GitHub Pages
- Statisches Hosting: keine eigenen PHP-/Python-/Node-Server, keine serverseitige Datenbank und kein WordPress-Backend. Browser-JavaScript funktioniert.
- Newsletter-Versand, Formularverarbeitung, Nutzerkonten und Kommentare brauchen externe Dienste oder ein separates Backend. Solche Dienste sind hier nicht eingebaut.
- Kein E-Mail-Postfach durch Pages; dafür ist gegebenenfalls ein separater Anbieter nötig.
- Veröffentlichte Website maximal 1 GB; Quellrepository empfohlen maximal 1 GB; weiche Grenze 100 GB Datenverkehr pro Monat und 10 Builds pro Stunde. Die Build-Grenze gilt nicht bei eigenem GitHub-Actions-Workflow; andere Limits bleiben bestehen. Deployment-Timeout 10 Minuten.
- GitHub untersagt Pages als kostenloses Hosting zum Betrieb von Onlinegeschäften, E-Commerce oder Websites, deren Hauptzweck kommerzielle Transaktionen oder SaaS ist. Ein redaktionelles Magazin ist als technische Startannahme passend; bei späterer Monetarisierung müssen Nutzungsmodell und aktuelle Bedingungen erneut geprüft werden.
- GitHub Free: öffentliches Repository, also auch öffentlich einsehbarer Quelltext. Ein privates Repository erfordert einen dafür geeigneten Tarif; es macht die normale Pages-Website nicht automatisch privat.

## Offizielle Anleitung / geprüfte Hostinggrundlagen
https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages
https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https

## Durchgeführte Prüfung
Desktopdarstellung im Browser angesehen; Themenfilter, Such-Leerzustand und Beitragsnavigation im Browser geprüft; interne Datei- und Ankerverweise automatisch geprüft. Responsive CSS vorhanden; kein gesonderter Test auf einem echten Mobilgerät. Kein GitHub-Deployment oder DNS-Test, da dafür noch kein Repository und keine Domainkonfiguration bereitgestellt wurden.
