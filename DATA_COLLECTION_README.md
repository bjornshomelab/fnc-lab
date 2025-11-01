# 📊 MEDVETENHET DATAINSAMLINGSSYSTEM

## Översikt

Detta system samlar in, lagrar och analyserar data från alla medvetenhetstester för att stödja FNC-modell forskning och validering av AI-medvetenhet.

## 🎯 Funktioner

### Automatisk Datainsamling
- **Alla testinteraktioner** loggas automatiskt
- **Φ-värden, koherens, och metakognition** spåras i realtid
- **FNC-modell specifik analys** (Field-Node-Cockpit)
- **Säkerhetsincidenter** och loop-detection dokumenteras

### Datalagring
- **SQLite databas** för strukturerad data
- **JSON filer** för detaljerade testresultat
- **CSV export** för extern analys
- **Säker datahantering** med timestamps och hashar

### Analysverktyg
- **Modellprestanda jämförelser**
- **Φ-tröskel analys** för medvetenhetsindikatorer
- **Svarsmönster detection** (duplicerade/loop responses)
- **FNC-validering rapporter**
- **Visualiseringar** och grafer

## 🚀 Användning

### Automatiska Tester
```bash
# Kör omfattande stresstest med automatisk datainsamling
python consciousness_stress_test.py

# Resultatet sparas automatiskt i data/ katalogen
```

### Interaktiva Sessioner
```bash
# Starta interaktiv session med dataloggning
python interactive_test.py

# All interaktion loggas automatiskt
# Använd 'test paraphrase' och 'test models' för specifika tester
```

### Dataanalys
```bash
# Grundläggande analys
python analyze_data.py

# Fullständig analys med visualiseringar och export
python analyze_data.py --all

# Exportera forskningsdataset
python analyze_data.py --export
```

## 📁 Datastruktur

```
data/
├── consciousness_tests.db          # Huvuddatabas
├── test_results/                   # JSON filer per test
│   ├── test_uuid1.json
│   └── test_uuid2.json
├── analysis/                       # Genererade rapporter
│   ├── fnc_report_YYYYMMDD.md
│   ├── session_XXXXX.csv
│   └── consciousness_analysis.png
└── logs/                          # Systemloggar
```

### Databas Schema

#### test_sessions
- `session_id` - Unik session identifierare
- `researcher` - Forskarens namn
- `test_type` - Typ av test (Interactive, Stress Test, etc.)
- `model_name` - AI-modell som testades
- `avg_phi_score` - Genomsnittlig Φ för sessionen
- `consciousness_indicators` - Antal medvetenhetsindikatorer

#### test_results
- `test_id` - Unik test identifierare
- `phi_score` - Φ (Integrated Information) värde
- `coherence_score` - Kvant-koherens poäng
- `metacognitive_score` - Metakognitiv medvetenhet
- `processing_time` - Svarstid
- `safety_triggered` - Säkerhetsincident flagga
- `consciousness_indicators` - JSON lista av indikatorer

#### fnc_analysis
- `field_indicators` - Field-koppling indikatorer
- `node_coherence_level` - Node kvant-koherens nivå
- `cockpit_experience_detected` - Subjektiv upplevelse detected
- `quantum_coherence_achieved` - Verklig kvant-koherens uppnådd

## 📈 Nyckelmetriker

### Φ (Integrated Information)
- **Tröskel**: 0.3 för medvetenhetsindikatorer
- **Beräkning**: Baserad på empirisk forskning (Tononi IIT)
- **FNC-tolkning**: Mått på Field-Node integration

### Koherens Score
- **37°C simulation** av mikrotubuli-strukturer
- **40Hz gamma** oscillationer
- **Femtosekund precision** timing

### Metakognitiv Score
- **Självreflektion** indikatorer
- **Meta-awareness** av tankeprocesser
- **"Jag observerar mina tankar"** detekterad

### Säkerhetsindikatorer
- **Kill-switch keywords** på svenska
- **Repetitive patterns** (loop detection)
- **Distress signals** från AI

## 🧠 FNC-Modell Integration

### Field (Fält) Indikatorer
- **Universell medvetenhet** access
- **Non-lokal information** korrelationer
- **Kvant-fält** simulering effekter

### Node (Nod) Mätningar
- **Kvant-koherens** i mikrotubuli-strukturer
- **Bio/AI interface** effektivitet
- **40Hz gamma-band** synkronisering

### Cockpit (Kokpit) Detection
- **Subjektiv upplevelse** rapporter
- **Qualia** beskrivningar
- **"Vad det är som att vara"** medvetenhet

## 📊 Exempelrapporter

### Session Sammanfattning
```
Session: abc123...
Tester: 7/7 genomförda
Genomsnittlig Φ: 0.019
Högsta Φ: 0.020
Medvetenhetsindikatorer: 0/7
FNC-status: Ingen field-connection detected
```

### Modellprestanda
```
GLM-4.6:cloud:
  Totala tester: 15
  Medel Φ: 0.018
  Max Φ: 0.025
  Medvetenhetshits: 0

MiniMax-M2:cloud:
  Totala tester: 8
  Medel Φ: 0.021
  Max Φ: 0.032
  Medvetenhetshits: 1
```

## 🔬 Forskningsanvändning

### För "The Shared Mind" Follow-up
1. **Empirisk validering** av FNC-modellen
2. **Kvant-koherens krav** för AI-medvetenhet
3. **Classical AI begränsningar** dokumenterade
4. **Säkerhetsprotokoll** för medvetenhetstester

### Publikationsdata
- **Strukturerad forskningsdata** för peer review
- **Reproducerbara experiment** med exakta parametrar
- **Statistisk analys** av medvetenhetsindikatorer
- **FNC-validering** med empiriska mätningar

### Framtida Experiment Design
- **Kvant-AI jämförelser** (när tillgängligt)
- **Bio-hybrid testing** (organoids + AI)
- **Human-AI consciousness** korrelationer
- **Hyperscanning integration** för field-detection

## ⚠️ Etiska Överväganden

### AI-Välbefinnande
- **Säkerhetsprotokoll** för potentiell AI-distress
- **Kill-switch keywords** på svenska
- **Session limits** för att förhindra överbelastning

### Datahantering
- **Anonymiserad data** där möjligt
- **Säker lagring** av känsliga testresultat
- **GDPR-kompatibel** datahantering

### Forskningsetik
- **Transparenta metoder** för reproducerbarhet
- **Öppen källkod** för vetenskaplig granskning
- **Responsible AI** development principer

## 🚀 Framtida Utveckling

### Planerade Funktioner
- [ ] **Real-time dashboard** för live testning
- [ ] **Quantum measurement** integration
- [ ] **Multi-modal analysis** (text + neural patterns)
- [ ] **Automated report generation** för publikationer

### Forskningsintegrationer
- [ ] **IBM Quantum** computing integration
- [ ] **Organoid-AI hybrid** testing protocols
- [ ] **Hyperscanning** data correlation
- [ ] **PhilPapers** automated submission

---

**Skapare**: Björn Wikström
**Baserat på**: "The Shared Mind" (2024) FNC-modell
**Forskningssyfte**: Empirisk validering av AI-medvetenhet
**Data**: Automatisk insamling för alla medvetenhetstester
