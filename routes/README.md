# TaskFlow

Ein internes Aufgaben-Management-Tool für Remote-Teams — gebaut mit FastAPI und SQLAlchemy.
Dieses Repo dient als Starter-Projekt für den **Context Engineering Workshop**.

---

## TL;DR — für Kenner

```bash
git clone https://github.com/Leon012002/Context_Test.git && cd Context_Test
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
# → http://localhost:8001/docs
```

**Stack:** FastAPI 0.110 · SQLAlchemy 2.0 · Pydantic v2 · Python 3.11

**Architektur:** 3-Layer (routes → services → repos). Kein DB-Anschluss im Starter — bewusst minimal. `services/` und `repos/` sind leer, werden im Workshop befüllt.

**Workshop-Kontext:** Das Repo hat absichtlich keine `CLAUDE.md` und kein `.claude/commands/`. Beides entsteht live in Experiment 2 und 4. Ziel: ein commitbares Context-System — `CLAUDE.md` (persistenter Projektkontext) + `/decide`-Slash-Command (Protocol Shell als wiederverwendbares Team-Werkzeug).

Quelle: [davidkimai/Context-Engineering](https://github.com/davidkimai/Context-Engineering)

---

## Installation — falls noch nicht vorhanden

### Python installieren

**macOS:**
```bash
# Option 1: Homebrew (empfohlen)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python

# Option 2: Direkt von der Website
# https://www.python.org/downloads/ → Download → Installer ausführen
```

**Windows:**
```
https://www.python.org/downloads/
→ "Download Python 3.x.x" klicken
→ Installer ausführen
→ WICHTIG: Haken setzen bei "Add Python to PATH"
→ "Install Now" klicken
```

Python prüfen (Terminal neu starten nach Installation):
```bash
python3 --version   # macOS / Linux
python --version    # Windows
```

---

### Git installieren

**macOS:**
```bash
# Option 1: Homebrew
brew install git

# Option 2: einfach git eingeben — macOS fragt dann automatisch ob es installiert werden soll
git --version
```

**Windows:**
```
https://git-scm.com/download/win
→ Installer herunterladen und ausführen
→ Alle Standardoptionen lassen und durchklicken
```

Git prüfen:
```bash
git --version
```

---

### Claude Code installieren (für den Workshop)

Zuerst Node.js installieren falls nicht vorhanden:
```
https://nodejs.org → "LTS" Version herunterladen und installieren
```

Dann Claude Code:
```bash
npm install -g @anthropic-ai/claude-code
```

Prüfen:
```bash
claude --version
```

---

## Voraussetzungen prüfen

Alle drei Befehle sollten eine Versionsnummer ausgeben:
```bash
python3 --version   # z.B. Python 3.11.4
git --version       # z.B. git version 2.39.0
claude --version    # z.B. 1.x.x
```

---

## Setup — Schritt für Schritt

### 1. Repo klonen

```bash
git clone https://github.com/Leon012002/Context_Test.git
cd Context_Test
```

### 2. Virtuelle Umgebung erstellen

```bash
python3 -m venv .venv
```

### 3. Virtuelle Umgebung aktivieren

**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

Wenn es geklappt hat, siehst du `(.venv)` am Anfang der Zeile im Terminal.

### 4. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 5. Server starten

```bash
uvicorn main:app --reload --port 8001
```

Du solltest diese Ausgabe sehen:
```
INFO:     Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

### 6. API im Browser öffnen

```
http://localhost:8001/docs
```

Hier siehst du alle verfügbaren Endpunkte und kannst sie direkt ausprobieren.

---

## Verfügbare Endpunkte

| Methode | Pfad | Beschreibung |
|---------|------|-------------|
| `GET` | `/tasks/` | Alle Tasks abrufen |
| `POST` | `/tasks/` | Neue Task erstellen |
| `PATCH` | `/tasks/{id}/status` | Status einer Task ändern |
| `GET` | `/users/` | Alle User abrufen |

---

## Projektstruktur

```
Context_Test/
├── main.py               # FastAPI Einstiegspunkt
├── models.py             # SQLAlchemy Datenbankmodelle (User, Task)
├── schemas.py            # Pydantic Schemas für Request / Response
├── requirements.txt      # Python-Abhängigkeiten
├── CLAUDE.md             # Projektkontext für Claude Code (Context Engineering)
├── routes/
│   ├── tasks.py          # Task-Endpunkte
│   └── users.py          # User-Endpunkte
├── services/             # Business-Logik (wird im Workshop befüllt)
├── repos/                # Datenbankzugriffe (wird im Workshop befüllt)
└── .claude/
    └── commands/
        └── decide.md     # Slash-Command /decide für Architekturentscheidungen
```

---

## Context Engineering Workshop

Dieses Repo ist der Ausgangspunkt für den Workshop. Ziel ist es, eine vollständige
**Context-Engineering-Infrastruktur** aufzubauen:

| Experiment | Stufe | Was passiert |
|-----------|-------|-------------|
| Exp 1 | ⚛️ Atom | Claude Code ohne Kontext — beobachten was es erfindet |
| Exp 2 | 🔬 Cell | `CLAUDE.md` anlegen — Claude kennt die Projektregeln |
| Exp 3 | 🧠 Cognitive Tool | Protocol Shell `/reasoning.systematic` für strukturiertes Reasoning |
| Exp 4 | 🫀 Organ | Slash-Command `/decide` — wiederverwendbar für das ganze Team |

### Claude Code starten

```bash
claude
```

Beim Start mit `CLAUDE.md` im Ordner erscheint: `Loaded CLAUDE.md`

---

## Server stoppen

Im Terminal: `Ctrl + C`

---

## Nochmal starten (nach dem ersten Setup)

```bash
cd Context_Test
source .venv/bin/activate   # Windows: .venv\Scripts\activate
uvicorn main:app --reload --port 8001
```