# Roadmap visuelle — Projet oncologie mathématique

## Vue d’ensemble

Objectif : organiser un projet à deux vitesses, avec deux axes réellement parallèles.

- **Axe A — PDE / FEM / PINN** : construire le solveur direct et la modélisation du domaine cérébral.
- **Axe B — Data / Calibration** : construire le pipeline données, calibration, incertitude et validation.

---

## Gantt général

```mermaid
gantt
    title Projet oncologie mathématique — Roadmap 10 semaines
    dateFormat  YYYY-MM-DD
    axisFormat  S%V

    section Socle commun
    Cadrage modèle et interface              :a0, 2026-05-04, 7d
    Architecture repo                        :a1, 2026-05-04, 7d
    Revue bibliographique minimale           :a2, 2026-05-04, 14d

    section Axe A — PDE / FEM / PINN
    Fisher-KPP 1D                            :p1, 2026-05-11, 7d
    Solveur FD 2D carré                      :p2, after p1, 7d
    Domaine cerveau simplifié                :p3, after p2, 7d
    Conditions aux limites / masque           :p4, after p3, 7d
    Prototype FEM                            :p5, after p4, 7d
    PINN Fisher-KPP                          :p6, after p5, 7d
    Coefficient spatial D(x)                 :p7, after p6, 7d
    Benchmark FD / FEM / PINN                :p8, after p7, 14d

    section Axe B — Data / Calibration
    Recherche datasets                       :d1, 2026-05-11, 14d
    Données synthétiques bruitées            :d2, 2026-05-11, 7d
    Objectif de calibration                  :d3, after d2, 7d
    Calibration synthétique                  :d4, after d3, 7d
    Pipeline imagerie minimal                :d5, after d4, 14d
    Premier cas réel ou semi-réel             :d6, after d5, 7d
    Incertitude / bootstrap                  :d7, after d6, 7d
    Analyse critique                         :d8, after d7, 14d

    section Intégration
    Interface solveur-calibration v1          :m1, 2026-05-18, 7d
    Calibration via solveur direct            :m2, 2026-06-08, 14d
    Figures finales                          :m3, 2026-06-29, 14d
    Rapport et slides                        :m4, 2026-07-06, 7d
```

---

| Semaine | Axe A — PDE / FEM / PINN | Axe B — Data / Calibration | Livrable commun |
|---|---|---|---|
| S1 | Modèle Fisher-KPP, Laplacien, conditions initiales | Recherche datasets, observables, littérature | `README.md`, interface solveur/calibration |
| S2 | Solveur FD 1D puis 2D carré | Générateur synthétique, bruit, première loss | Simulation + données synthétiques |
| S3 | Domaine cerveau simplifié avec masque | Calibration synthétique de `D`, `r`, `K` | Figure croissance + tableau paramètres |
| S4 | Conditions aux limites sur domaine masqué, FEM minimal | Optimisation robuste, données manquantes | Note FD vs FEM + calibration robuste |
| S5 | PINN Fisher-KPP | Pipeline imagerie minimal | Comparaison FD / PINN |
| S6 | Diffusion hétérogène `D(x)` | Dataset réel ou semi-réel choisi | Note dataset + figure hétérogénéité |
| S7 | API solveur stable, tests | Premier cas réel calibré | Données observées vs modèle |
| S8 | Benchmark FD / FEM / PINN | Incertitude, bootstrap, sensibilité | Figures erreur / temps / incertitude |
| S9 | Terme de traitement `-c(t)u` | Interprétation et limites cliniques | Figure traitement |
| S10 | Nettoyage code numérique | Nettoyage calibration et discussion | Rapport, slides, README final |

---

## Carte des dépendances

```mermaid
flowchart LR
    A[Modèle Fisher-KPP] --> B[Solveur FD]
    A --> C[PINN]
    A --> D[FEM]

    B --> E[Observables simulées]
    C --> E
    D --> E

    F[Données médicales] --> G[Prétraitement]
    G --> H[Volumes tumoraux observés]

    E --> I[Calibration]
    H --> I

    I --> J[Paramètres estimés]
    J --> K[Analyse incertitude]
    J --> L[Comparaison patients]
    K --> M[Rapport final]
    L --> M
```

---

## Interface technique minimale

```mermaid
flowchart TB
    theta["Paramètres theta = (D, r, K)"]
    geometry["Géométrie : brain_mask, tissue_map"]
    u0["Condition initiale u0"]
    solver["Solveur direct PDE"]
    output["Sorties : u(x,t), volume(t), radius(t)"]
    data["Données observées : V_obs(t_i)"]
    loss["Fonction objectif"]
    optimizer["Optimiseur"]
    theta_est["Paramètres calibrés"]

    theta --> solver
    geometry --> solver
    u0 --> solver
    solver --> output
    output --> loss
    data --> loss
    loss --> optimizer
    optimizer --> theta_est
    theta_est --> solver
```

---

## Jalons de validation

```mermaid
timeline
    title Jalons scientifiques

    Semaine 2 : Solveur FD 2D fonctionnel
              : Données synthétiques générées

    Semaine 3 : Domaine cerveau simplifié
              : Calibration synthétique réussie

    Semaine 5 : Premier benchmark FD vs PINN
              : Pipeline data minimal

    Semaine 7 : Premier cas réel ou semi-réel calibré

    Semaine 8 : Sensibilité et incertitude

    Semaine 10 : Rapport final et repo reproductible
```

---

## Version minimale viable

Si le projet doit être réduit, conserver seulement :

```mermaid
flowchart LR
    A[Solveur FD 2D] --> B[Données synthétiques bruitées]
    B --> C[Calibration D,r]
    C --> D[Analyse d'incertitude]
    A --> E[PINN simple]
    E --> F[Comparaison FD / PINN]
    D --> G[Rapport final]
    F --> G
```

Cette version suffit à produire un projet cohérent : modèle direct, problème inverse, benchmark numérique, discussion critique.
