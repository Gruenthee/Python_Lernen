## 1. Die Komponenten (Das "Warum")
* **Python:** Die Programmiersprache (das Gehirn). Führt Berechnungen aus.
* **VS Code:** Der Editor (die Schreibmaschine). Hier tippe ich den Code.
* **Jupyter:** Das Labortagebuch. Erlaubt es, Code in Häppchen (Zellen) auszuführen.

## 2. Wichtige Git-Befehle (Mein Cloud-Datenverkehr)
Wenn der Dozent von Git spricht, nutze ich diese Logik:

* `git clone <link>` = Ich lade das Projekt des Dozenten das erste Mal auf meinen PC.
* `git pull` = Ich hole mir die neuesten Aufgaben vom Server ab (wie "E-Mails abrufen").
* `git push` = Ich lade meine gelösten Aufgaben auf den Server hoch.
* `Branch` = Mein privater Notizblock/Zweig. Hier kann ich programmieren, ohne das Hauptprojekt kaputtzumachen.

#.gitignore Sicherheit: Durch die .gitignore-Datei sorgen wir dafür, dass sensible Rohstoffdaten niemals öffentlich auf GitHub landen
tab taste = pfeile für autocomplete

2. Der Standard-Workflow (Dein täglicher Ablauf)

Wir arbeiten nie direkt auf dem Hauptstrang (dem main-Branch), um unser Projekt nicht zu zerschießen. Wir nutzen den Feature-Branch-Workflow:

    Branch erstellen (Abzweigen): Du erstellst eine eigene Arbeitskopie für eine neue Funktion (z.B. eine neue Risikometrik).

        Befehl: git checkout -b feature/neue-metrik

    Änderungen speichern (Commiten): Du speicherst deine Arbeit lokal.

        Befehl: git add . (sagt Git: „Nimm alle geänderten Dateien in die Liste auf“)

        Befehl: git commit -m "Kurze Beschreibung, was du gemacht hast"

    Hochladen (Push): Du schickst deinen Stand in den Cloud-Tresor (GitHub).

        Befehl: git push origin feature/neue-metrik

    Zusammenführen (Pull Request & Merge): Auf GitHub klickst du auf „Pull Request erstellen“. Das signalisiert: „Mein Code ist fertig, bitte prüfen und in das Hauptprojekt aufnehmen.“ Wenn alles passt, wird der Code gemergt (integriert).
