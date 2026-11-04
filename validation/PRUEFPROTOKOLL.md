# Validierung mundoverde Entwurf 01

Prüfung am 4. November 2026. Prüfobjekt ist die lokale Marken- und Websitefassung, nicht die veröffentlichte Website.

## Gestalterische Prüfung und Überarbeitung

- Generiertes Konzeptbild als erster Ansatz gesichtet. Die digitale Produktionsfassung anschließend eigenständig in SVG aufgebaut; Schrift und Geometrie sind bewusst keine pixelgenaue Kopie des Bildkonzepts.
- Blattader und unregelmäßige Konturen entfernt, damit das v als Buchstabe erkennbar bleibt. Das Motiv kann dennoch an ein Häkchen erinnern. Seine eindeutige Wiedererkennung ist nicht durch Nutzertests bestätigt.
- Blatt nur für größere Symbolgrößen; Micro-Zeichen ohne Blatt. Die Micro-Variante nach Durchsicht vertikal korrigiert, damit das v auf kleinen quadratischen Flächen mittig sitzt.
- Farbige, einfarbige und weiße Wortmarke verwenden dieselben Umrisse. SVG-Logos enthalten nur Pfade, keine fontabhängigen Texte, Skripte oder externen Ressourcen.
- Brandboard gerendert und visuell gesichtet. PNG-Exporte auf vollständig lesbare Bilddaten geprüft.
- Wortmarke ab 180 CSS-Pixel empfohlen, Blattsymbol ab 32 Pixel. Die Größenbeispiele sind im Leitfaden verfügbar. Keine empirisch festgestellte Mindestgröße; kein physischer Druck-Andruck.

## Berechnete Farbkontraste

Die sechs vorgesehenen Text-/Hintergrundkombinationen erreichen 5,19:1 bis 11,34:1. Einzelwerte und Rechenmethode im Leitfaden und contrast.json. Berechnung über relative sRGB-Luminanz. Für normale Schrift wird 4,5:1 als AA-Grenze angesetzt. Diese Teilprüfung ist keine vollständige Barrierefreiheitsprüfung.

## Im Chrome-Browser beobachtet

Die Website wurde über die lokale Vorschau geöffnet und visuell geprüft. Der Gestaltungsleitfaden wurde ebenfalls geöffnet; Inhalt und Varianten waren erreichbar.

Funktionen:

- Initial sechs sichtbare Beiträge.
- Themenfilter Natur: ein sichtbarer Beitrag und Status „1 Beitrag entdecken“.
- Suchbegriff xyz-unbekannt: keine Beiträge, Leermeldung und Status „0 Beiträge entdecken“.
- Alle plus Suchbegriff „  WETTER  “: ein sichtbarer Beitrag; Großschreibung und Leerzeichen werden verarbeitet.
- Leeren der Suche: wieder sechs Beiträge.
- Erster Tastaturschritt mit Tab: „Zum Inhalt springen“ erhält den Fokus.

Responsive Ansichten wurden in Browser-Iframes mit vier Breiten geprüft. Die verfügbare Inhaltsbreite ist wegen der Scrollleiste jeweils 15 Pixel geringer als die Rahmenbreite:

| Rahmenbreite | Inhaltsbreite | Scrollbreite | Seitlicher Überlauf |
|---|---:|---:|---|
| 320 px | 305 px | 305 px | nein |
| 390 px | 375 px | 375 px | nein |
| 768 px | 753 px | 753 px | nein |
| 1440 px | 1425 px | 1425 px | nein |

In allen vier Ansichten waren sechs Beiträge und alle drei Navigationslinks im DOM vorhanden. Die schmalste Ansicht wurde zusätzlich visuell gesichtet; Navigation und Inhalte waren ohne seitlichen Überlauf angeordnet. Das prüft nicht sämtliche Zwischenbreiten oder alle Endgeräte.

Ohne JavaScript in einem sandboxed Iframe: sechs Beiträge bleiben vorhanden, das Suchfeld ist deaktiviert und die Filter sind verborgen. Ein noscript-Hinweis ist im HTML enthalten. Inhaltsbreite und Scrollbreite betrugen beide 305 Pixel. Das ist kein separater vollständiger Test mit einem Browser, dessen JavaScript global deaktiviert ist.

## Statische Prüfung

JavaScript-Syntax, lokale Datei- und Sprungziele, SVG-XML, externe Referenzen in Logo-Mastern und vollständige PNG-Bilddaten werden vor Verpackung geprüft. Das Ergebnis steht in static-checks.json.

## Offene Punkte und Grenzen

- Keine bestätigte markenrechtliche Alleinstellung. v/Blatt-Motive sind verbreitet; Name und Zeichen wurden nicht auf kollidierende Marken recherchiert.
- Keine Screenreader-Komplettprüfung, keine automatisierte WCAG-Gesamtprüfung und keine Zertifizierung.
- Keine Android-/iOS-Geräteprüfung; die responsive Prüfung erfolgte in Chrome-Iframes.
- Keine Druckfreigabe oder überprüften CMYK-/Pantone-Entsprechungen. HEX ist der digitale Master.
- Keine neue Prüfung der Rechtstexte. Sie und die Artikel bleiben in der Websitekopie Entwürfe. Die gesonderte Impressumsvorlage ohne Telefonnummer besteht unabhängig davon.
- Die Website wurde nicht live ersetzt. Der aktuelle GitHub-Quellstand wurde für dieses Design nicht neu heruntergeladen.

## Quellen

- https://dle.rae.es/mundo
- https://dle.rae.es/verde
- https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum
- https://w3c.github.io/wcag/understanding/non-text-contrast

Gestalterische Wertungen und die Markenmetapher sind eigene Entwurfsentscheidungen. Die Kontrastwerte stammen aus eigener Berechnung.
