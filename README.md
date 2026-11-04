# mundoverde Logo Schriftentwurf 02

Die Wortmarke verwendet jetzt eine ruhigere Serifenschrift auf Basis von DejaVu Serif Book. Die Änderung soll dem Naturmagazin eine wärmere, buchnahe und redaktionelle Anmutung geben. Das ist eine gestalterische Einschätzung, kein durch Nutzertests belegtes Wahrnehmungsergebnis.

Das v als Keimling, die beiden Grüntöne, der Name und die grundsätzliche Anordnung bleiben erhalten. Das Symbol ist in der Wortmarke bewusst eine eigene Form und kein getipptes Standard-v. Die Lesetypografie und Bedienoberfläche der Website müssen wegen dieser Logoänderung nicht auf Serifenschrift umgestellt werden.

## Ansehen und verwenden

- vergleich.png zeigt alte und neue Wortmarke mit gleicher Breite der SVG-Zeichenflächen. Die untere Zusatzansicht zeigt die Negativfassung.
- assets enthält transparente SVG- und PNG-Dateien in Farbe, einfarbig und weiß. Weiße Logos auf dunklem Grund ansehen.
- website/assets enthält ausschließlich die drei neuen SVG-Wortmarken mit den bisherigen Dateinamen. Bei späterer Übernahme nur diese Wortmarken im entsprechenden assets-Ordner ersetzen. Keine HTML-, Rechts- oder Beitragsdateien werden überschrieben.
- reference enthält die alte Wortmarke zum Vergleich.
- build_logo.py und specification.json dokumentieren den Aufbau. Zum Erzeugen wird Python mit fontTools und DejaVu Serif am angegebenen Systempfad benötigt. PNGs wurden mit Inkscape exportiert.
- FONT-LICENSE.txt enthält die Lizenzhinweise zur Schriftbasis. Die SVGs bestehen aus Pfaden und laden keine Schriftdatei nach.

## Ergänzung zum CI/CD Leitfaden 01

Die bisherige Logo-Schriftbasis DejaVu Sans wird für die Wortmarke durch DejaVu Serif Book ersetzt. Die feste Vektorform ist der Master. Schutzraum, Farbpalette, Mindestbreiten und Verwendung der separaten Symbole aus dem bisherigen Leitfaden bleiben als Entwurfsregeln bestehen. Minimum für die Wortmarke weiterhin 180 CSS-Pixel; darunter das vorhandene separate v-Zeichen verwenden. Kein Schatten, kein Strecken, keine Kontur ergänzen.

## Geprüft

Die neue Fassung wurde als Bild gerendert und gesichtet. SVG-Struktur, vollständig lesbare PNGs und eine kleine Größenübersicht wurden geprüft. Alle drei SVG-Wortmarken verwenden dieselbe Geometrie und benötigen keine externen Ressourcen. Die Farben sind unverändert; die bisherigen Kontrastberechnungen gelten deshalb weiterhin für die gleichen Farbpaare. Die Wortmarke hat annähernd dieselbe Zeichenflächenproportion wie vorher.

Das ist keine neue vollständige Prüfung der Website, keine Markenfreigabe und kein Andruck. Es wurde keine Live-Änderung durchgeführt.
