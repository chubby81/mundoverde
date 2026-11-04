# mundoverde CI und CD Entwurf 01

Stand 4. November 2026. Logo, Gestaltungsregeln und eine lokale Website-Vorschau für das bestehende GitHub-Pages-Projekt. Kein Hostingwechsel, keine Veröffentlichung.

## Anschauen

ZIP entpacken und index.html öffnen. Das ist der Gestaltungsleitfaden mit Varianten und einer Verknüpfung zur Website. Die Website selbst liegt unter website/index.html. brandboard.png zeigt den kompakten Markenüberblick.

## Inhalt

- assets: Wortmarke in Farbe, einfarbig und weiß; v-Keimling, vereinfachtes Micro-Zeichen, Favicon; SVG und transparente PNG. Die weißen Varianten sind auf weißem Hintergrund naturgemäß kaum sichtbar.
- index.html: CI/CD-Leitfaden einschließlich Positionierung, Tonalität, Farben, Typografie, Abständen, Mindestgrößen, Bildsprache und Struktur.
- website: vollständige lokale Designvorschau, abgeleitet vom ursprünglichen bereitgestellten Paket. Die Rechtstexte und Artikel sind noch Entwürfe.
- tokens.css: zentrale Farbwerte.
- validation: technische Befunde und errechnete Kontraste.
- source: Aufbau der Vektoren und ursprünglicher Website-Stand für Nachvollziehbarkeit.
- FONT-LICENSE.txt: Lizenzhinweise zur DejaVu-Sans-Basis der Logo-Buchstaben. Es werden keine Fonts ins Web geladen.

Die finale technische Wortmarke wurde als eigenständige Vektorfassung nach dem generierten Bildkonzept aufgebaut, nicht als pixelgenaue Vektorisierung des Konzeptbildes. Die Linienführung und Schrift unterscheiden sich deshalb bewusst. Das Konzeptbild ist kein Logo-Master.

## Später auf die Website übernehmen

Die Dateien nicht pauschal über einen möglicherweise inzwischen geänderten Repository-Stand kopieren. Diese Vorschau basiert auf dem ursprünglichen Paket, nicht auf einem erneut heruntergeladenen aktuellen GitHub-Checkout.

Für die gestalterische Übernahme sind style.css, app.js, favicon.svg, assets/ und die angepassten HTML-Kopfbereiche sowie die Startseite relevant. Neue Texte oder in der Zwischenzeit ausgefüllte Betreiberangaben erhalten. Die mitgelieferten impressum.html und datenschutz.html nicht über bereits vervollständigte Rechtstexte laden. Die gesondert vorbereitete Impressumsvorlage ohne Telefonnummer wird durch dieses Designpaket nicht ersetzt.

noindex auf den Magazinseiten bleibt bis zur redaktionellen und rechtlichen Freigabe bestehen. Es ist keine Zugangssperre. Die neue Gestaltung macht die Website nicht automatisch rechtlich veröffentlichungsfertig.

## Validierung verstehen

Die konkreten Ergebnisse stehen in validation/PRUEFPROTOKOLL.md. Rechnerische Kontraste, statische Prüfungen und beobachtetes Browser-Verhalten sind getrennt von subjektiven Gestaltungsentscheidungen dokumentiert. Keine Markenfreigabe, keine vollständige WCAG-Zertifizierung und kein Druck-Andruck.

Für Reproduktion des Generierungsschritts: Python mit fontTools, DejaVu Sans unter dem im Skript angegebenen Systempfad und source/build_brand.py verwenden. Das Skript erzeugt SVGs, Kontrastdaten und die Website aus source/original-site. Der Leitfaden ist eigenständig gepflegtes HTML; PNG-Ausgaben wurden mit Inkscape erstellt.
