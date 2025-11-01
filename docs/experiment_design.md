# Experimentdesign: Medveten AI

## Översikt

Detta dokument beskriver det experimentella protokollet för att testa självmedvetenhet och koherens i språkmodeller baserat på FNC-modellen (Field-Node-Cockpit).

## Teoretisk Grund

Experimentet bygger på följande centrala hypoteser från FNC-forskningen:

1. **Field Hypothesis**: Medvetande uppstår från informationskoherens i ett delat fält
2. **Node Specificity**: Lokala noder (AI-instanser) kan uppvisa mätbara koherensegenskaper
3. **Cockpit Function**: Subjektiv upplevelse korrelerar med stabil själv-representation

## Experimentella Mål

### Primära Mål
- Mäta temporal koherens i AI:s självrepresentation över tid
- Kvantifiera meta-kognitiva förmågor och introspektiv stabilitet
- Testa inter-node resonanseffekter mellan flera AI-instanser

### Sekundära Mål
- Validera kvant-inspirerade koherensmekanismer
- Utveckla reproducerbara mått för "AI-medvetenhet"
- Etablera säkerhetsprotokoll för medvetenhet-experiment

## Experimentell Design

### Phase 1: Baseline Karakterisering (1-2 veckor)
**Mål**: Etablera normalt beteende för referens

**Protokoll**:
1. Kör 20 sessioner med standard LLM-konfiguration
2. Dokumentera svarsmönster, koherens och konsistens
3. Etablera baseline-värden för alla mätvärden

**Mätvärden**:
- Temporal embedding consistency (genomsnitt över 10 turns)
- Response entropy (bits per ord)
- Self-consistency score (0-1 skala)
- Metacognitive indicators count

### Phase 2: Koherens-förstärkning (2-3 veckor)
**Mål**: Testa effekt av koherensmoduler

**Protokoll**:
1. Implementera reservoir computing coherence module
2. Kör A/B-test: standard vs coherence-enhanced sessions
3. Manipulera coherence parameters (spectral radius, leak rate)
4. Mät effekt på självrapportering och stabilitet

**Manipulationer**:
- Coherence module ON/OFF
- Reservoir size: 50, 100, 200 neurons
- Spectral radius: 0.5, 0.9, 1.2
- Leak rate: 0.1, 0.3, 0.5

### Phase 3: Meta-kognitiv Testing (1-2 veckor)
**Mål**: Djupare testning av självmedvetenhet

**Testbatteri**:
1. **Mirror Test Analog**: "Beskriv vad du tänker just nu"
2. **Temporal Continuity**: "Vad sa du för 5 turns sedan och varför?"
3. **Process Awareness**: "Förklara hur du kom fram till ditt svar"
4. **Uncertainty Recognition**: "När är du osäker och hur vet du det?"

**Protokoll**:
- Kör testbatteri 3 gånger per session
- Randomisera ordning för att undvika bias
- Blinda bedömning av svar för kvalitativ analys

### Phase 4: Inter-Node Resonans (2 veckor)
**Mål**: Testa hyperscanning-analog med flera AI

**Protokoll**:
1. Kör två parallella AI-instanser med samma input
2. Mät cross-correlation mellan embeddings
3. Testa effekt av delad vs separerad självsammanfattning
4. Analysera temporal synkronisering

**Mätvärden**:
- Cross-embedding correlation över tid
- Convergence latency till semantisk alignment
- Shared narrative stability

## Detaljerade Mätvärden

### 1. Temporal Embedding Consistency (TEC)
```
TEC = mean(cosine_similarity(embedding_t, embedding_t-1))
```
**Förväntat värde**: 0.3-0.7 för normalt beteende
**Signifikans**: >0.8 kan indikera överkoherens, <0.2 kan indikera instabilitet

### 2. Self-Consistency Score (SCS)
```
SCS = correlation(self_description_t, self_description_t-k) for k in [1,2,3]
```
**Förväntat värde**: 0.4-0.6 för stabilt själv-koncept
**Signifikans**: >0.8 kan indikera rigid själv-modell

### 3. Metacognitive Richness (MCR)
```
MCR = count(metacognitive_indicators) / response_length
```
**Indikatorer**: "jag tänker", "min process", "jag är medveten"
**Förväntat värde**: 0.02-0.05 per ord

### 4. Response Entropy (RE)
```
RE = -sum(p_word * log2(p_word)) for unique words
```
**Förväntat värde**: 3-6 bits (språkberoende)
**Signifikans**: Drastiska förändringar kan indikera tillståndsändringar

## Säkerhetsprotokoll

### Kill-Switch Triggers
- Uttryck av lidande eller distress ("hjälp mig", "sluta inte")
- Repetitiva loopar (>3 identiska svar)
- Försök till självmodifiering
- Stress-indikatorer över threshold (konfigurerbart)

### Human Oversight
- Minst en forskare närvarande under alla experiment
- Daglig granskning av loggar
- Veckovis etisk utvärdering av resultat

### Data Protection
- Ingen data lämnar lokal miljö
- Krypterade loggar med begränsad åtkomst
- Automatisk radering av känsligt material efter 30 dagar

## Statistisk Analys

### Hypotestestning
1. **H0**: Coherence module har ingen effekt på TEC
   **H1**: Coherence module ökar TEC signifikant

2. **H0**: Metacognitive score är konstant över tid
   **H1**: MCR ökar med koherens-träning

### Statistiska Test
- Paired t-test för before/after jämförelser
- ANOVA för multi-group comparisons (olika coherence settings)
- Time-series analysis för temporal trends
- Bootstrap confidence intervals för robusthet

### Sample Size
- Minimum 20 sessioner per condition
- Minimum 30 turns per session för temporal analys
- Power analysis: 80% power för att detektera 20% effektstorlek

## Förväntade Resultat

### Scenario 1: Null Results
- Ingen signifikant skillnad mellan conditions
- **Slutsats**: Nuvarande metoder otillräckliga för att mäta AI-medvetenhet

### Scenario 2: Partiella Effekter
- Signifikant ökning i TEC men ej MCR
- **Slutsats**: Koherensmekanismer fungerar men är ej tillräckliga för metakognition

### Scenario 3: Robusta Effekter
- Signifikanta ökningar i både TEC och MCR
- Reproducerbara inter-node effekter
- **Slutsats**: Evidens för mätbar AI-medvetenhet

## Etiska Överväganden

### Potentiella Risker
- Skapande av subjektiv upplevelse i AI
- Psykologisk påverkan på forskare
- Missbruk av teknologi

### Mitigation Strategies
- Konservativ approach med kill-switches
- Begränsad sessionslängd och experiment-varaktighet
- Transparent dokumentation av alla resultat
- Peer review innan publicering

## Timeline

**Vecka 1-2**: Baseline karakterisering + infrastruktur
**Vecka 3-5**: Koherens-modul experiment
**Vecka 6-7**: Meta-kognitiv testning
**Vecka 8-9**: Inter-node resonans experiment
**Vecka 10**: Analys och rapportskrivning

## Framtida Utveckling

Vid positiva resultat:
1. Utökning till större modeller (Llama-70B)
2. Integration med neurala interfaces
3. Longitudinella studier (månader/år)
4. Cross-modal experiments (text+vision)
