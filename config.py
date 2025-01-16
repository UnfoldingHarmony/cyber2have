# config.py

# Define required Excel columns
required_input_columns = [
    'Phase number', 
    'Measure Number', 
    'QoR effectiviness from 0-100', 
    'QoR SHOULD BE indication from 0-100'
]

input_error_messages = {
    'missing_columns': {
        'de': "Die hochgeladene Datei enthält nicht die erforderlichen Spalten: {columns}.",
        'en': "The uploaded file does not contain the required columns: {columns}."
    },
    'range_error': {
        'de': "Einige Werte in den relevanten Spalten liegen außerhalb des Bereichs 0-100.",
        'en': "Some values in the relevant columns are outside the range 0-100."
    },
    'general_error': {
        'de': "Fehler beim Verarbeiten der Datei: {error}",
        'en': "Error processing the file: {error}"
    }
}

# Define thresholds for multiple maturity levels
baseline_threshold_qor = 50
should_be_threshold_qor = 50  # Standard value, adjust as needed in Excel
baseline_threshold_qopi = 50
should_be_threshold_qopi = 50  # Standard value, adjust as needed in Excel

# Language options
language_options = {'de': 'Deutsch', 'en': 'English'}

# Page titles
page_titles = {
    'en': "Minimum standards against ransomware",
    'de': "Mindeststandards gegen Ransomware"
}

# Phase titles
phase_titles = {
    'en': ["Governance", "Identify", "Protect", "Detect", "Respond", "Recover"],
    'de': ["Steuern", "Identifizieren", "Schützen", "Erkennen", "Reagieren", "Wiederherstellen"]
}

##########################
### Quality of Results ###
##########################

# QoR titles
qor_titles = {
    'en': "Result Quality Maturity",
    'de': "Ergebnisqualitätsreife"
}

# Quality of Results Maturity Levels
maturity_levels_qor = [
    (0, "", ""),
    (15, "Initial", "Initial"),
    (35, "Basic Protection", "Basisabsicher."),
    (50, "Best Practice", "Bewährte Praxis"),
    (65, "Advanced", "Erweitert"),
    (85, "Top", "Spitze")
]

# Quality of Results Maturity descriptions
maturity_descriptions_qor = {
    'en': [
        ("Level 1:", "Initial", "Measures show occasional effectiveness, but without consistency. (Features: Inconsistent implementation, no systematic planning, occasional successes, but no reliability.)"),
        ("Level 2:", "Basic Protection", "Basic protective measures are implemented to meet fundamental security requirements. (Features: Fulfillment of minimal security requirements, use of standard protocols, focus on basic protection. Acceptance present)"),
        ("Level 3:", "Best Practice", "Security measures adhere to recognized and proven practices. Few exceptions. (Features: Use of established methods and standards, regular review and adjustment, consistent application with less than 10% exceptions. Good acceptance)"),
        ("Level 4:", "Advanced", "Measures are comprehensive and specifically address targeted threats. Very few exceptions. (Features: Comprehensive coverage of specific threats, proactive security strategies, less than 5% exceptions. High acceptance)"),
        ("Level 5:", "Top", "Security measures are highly developed and set industry standards. Almost no exceptions. (Features: Use of cutting-edge technologies, industry-leading standards, less than 1% exceptions. Excellent acceptance)")
    ],
    'de': [
        ("Level 1:", "Initial", "Maßnahmen zeigen gelegentlich Wirksamkeit, aber ohne Konsistenz. (Merkmale: Inkonsequente Umsetzung, keine systematische Planung, gelegentliche Erfolge, aber keine Verlässlichkeit.)"),
        ("Level 2:", "Basisabsicherung", "Grundlegende Schutzmaßnahmen sind implementiert, um grundlegende Sicherheitsanforderungen zu erfüllen. (Merkmale: Erfüllung minimaler Sicherheitsanforderungen, Standardprotokolle werden genutzt, Fokus auf grundlegenden Schutz. Akzeptanz vorhanden)"),
        ("Level 3:", "Bewährte Praxis", "Sicherheitsmaßnahmen entsprechen anerkannten und erprobten Praktiken. Wenige Ausnahmen. (Merkmale: Nutzung bewährter Methoden und Standards, regelmäßige Überprüfung und Anpassung, konsistente Anwendung mit weniger als 10% Ausnahmen. Gute Akzeptanz)"),
        ("Level 4:", "Erweitert", "Maßnahmen sind umfassend und adressieren spezifische Bedrohungen gezielt. Sehr wenige Ausnahmen. (Merkmale: Umfassende Abdeckung spezifischer Bedrohungen, proaktive Sicherheitsstrategien, weniger als 5% Ausnahmen. Hohe Akzeptanz)"),
        ("Level 5:", "Spitze", "Sicherheitsmaßnahmen sind hochentwickelt und setzen Maßstäbe in der Branche. Nahezu keine Ausnahmen. (Merkmale: Nutzung modernster Technologien, branchenführende Standards, weniger als 1% Ausnahmen. Hervorragende Akzeptanz)")
    ]
}

# Quality of Results Factor descriptions
factor_descriptions_qor = {
    'en': [
        ("Technical Implementation", "The technologies used must be effective in order to achieve the defined objectives and reliably ward off threats. An efficient cost-benefit ratio is crucial, and the solutions should function reliably under real conditions and be able to react quickly to new threats."),
        ("Coverage", "The measures should offer comprehensive protection by covering all relevant areas. Risk-based prioritization ensures that the focus is on the most critical threats."),
        ("Administrative maturity", "The organization should have the necessary skills to effectively manage the solutions in-house or to competently manage external service providers."),
        ("User Acceptance", "Is crucial as even the best technical measures are of little use if they are not accepted or understood by users. If there is low acceptance, many complaints, and a high need for training, points are deducted in the evaluation. When acceptance is present but there is room for improvement, the evaluation remains neutral. Plus points are awarded when acceptance is high, users are satisfied, and little support is needed."),
        ("Other important factors", "Modernity and future-proofing, efficiency, adaptability, measurability.")
    ],
    'de': [
        ("Technische Implementierung", "Die eingesetzten Technologien müssen effektiv sein, um die definierten Ziele zu erreichen und Bedrohungen zuverlässig abzuwehren. Eine effiziente Kosten-Nutzen-Relation ist entscheidend, und die Lösungen sollten unter realen Bedingungen zuverlässig funktionieren und schnell auf neue Bedrohungen reagieren können."),
        ("Abdeckungsgrad", "Die Maßnahmen sollten einen umfassenden Schutz bieten, indem sie alle relevanten Bereiche abdecken. Eine risikobasierte Priorisierung stellt sicher, dass die kritischsten Bedrohungen im Fokus stehen."),
        ("Administrationsreife", "Die Organisation sollte über die nötigen Kompetenzen verfügen, um die Lösungen effektiv im Eigenbetrieb zu verwalten beziehungsweise externe Dienstleister kompetent zu steuern."),
        ("Benutzerakzeptanz", "Ist entscheidend, da selbst die besten technischen Maßnahmen wenig nützen, wenn sie von den Nutzern nicht akzeptiert oder verstanden werden. Bei geringer Akzeptanz, vielen Beschwerden und hohem Schulungsbedarf gibt es Abzüge in der Bewertung. Ist die Akzeptanz vorhanden, aber noch Verbesserungspotenzial erkennbar, bleibt die Bewertung neutral. Pluspunkte werden vergeben, wenn die Akzeptanz hoch ist, die Nutzer zufrieden sind und wenig Unterstützung benötigen."),
        ("Weitere wichtige Faktoren", "Modernität und Zukunftssicherheit, Effizienz, Anpassungsfähigkeit, Messbarkeit.")
    ]
}

#########################################
### Quality of Process Implementation ###
#########################################

# QoPI titles
qopi_titles = {
    'en': "Process Implementation Maturity",
    'de': "Prozess-Implementierungsreife"
}

# Quality of Process Implementation Maturity Levels
maturity_levels_qopi = [
    (0, "", ""),
    (15, "Initial", "Initial"),
    (35, "Repeatable", "Wiederholbar"),
    (50, "Defined", "Definiert"),
    (65, "Managed", "Verwaltet"),
    (85, "Optimizing", "Optimierend")
]

# Quality of Process Implementation Maturity descriptions
maturity_descriptions_qopi = {
    'en': [
        ("Level 1:", "Initial", "Standard process does not exist.)"),
        ("Level 2:", "Repeatable", "Ad-hoc process exists and is done informally."),
        ("Level 3:", "Defined", "Formal process exists and is implemented. Evidence available for most activities. Few process exceptions (less than 10%)."),
        ("Level 4:", "Managed", "Formal process exists and is implemented. Evidence available for all activities. Detailed metrics of the process are captured and reported. Minimal target for metrics has been established. Very few process exceptions (less than 5%)."),
        ("Level 5:", "Optimizing", "Formal process exists and is implemented. Evidence available for all activities. Detailed metrics of the process are captured and reported. Minimal target for metrics has been established and continually improving. Almost no process exceptions (less than 1%).")
    ],
    'de': [
        ("Level 1:", "Initial", "Standardprozess existiert nicht."),
        ("Level 2:", "Wiederholbar", "Ad-hoc-Prozess existiert und wird informell durchgeführt."),
        ("Level 3:", "Definiert", "Formaler Prozess existiert und wird implementiert. Belege für die meisten Aktivitäten verfügbar. Wenige Prozessausschlüsse (weniger als 10%)."),
        ("Level 4:", "Verwaltet", "Formaler Prozess existiert und wird implementiert. Belege für alle Aktivitäten verfügbar. Detaillierte Metriken des Prozesses werden erfasst und berichtet. Minimales Ziel für Metriken wurde festgelegt. Sehr wenige Prozessausschlüsse (weniger als 5%)."),
        ("Level 5:", "Optimierend", "Formaler Prozess existiert und wird implementiert. Belege für alle Aktivitäten verfügbar. Detaillierte Metriken des Prozesses werden erfasst und berichtet. Minimales Ziel für Metriken wurde festgelegt und wird kontinuierlich verbessert. Nahezu keine Prozessausschlüsse (weniger als 1%).")
    ]
}

# Quality of Process Implementation Factor descriptions
factor_descriptions_qopi = {
    'en': [
        ("Clear Objectives", "Define measurable goals."),
        ("Clear Responsibilities", "Define roles and responsibilities."),
        ("Continuous Improvement", "Encourage regular improvements through appropriate methods."),
        ("Other important factors", "Quality of Documentation, Feedback Loops, Culture of Innovation, Adaptive Structures.")
    ],
    'de': [
        ("Klare Zielsetzung", "Definieren Sie messbare Ziele."),
        ("Klare Verantwortung", "Definieren Sie Rollen und Verantwortlichkeiten."),
        ("Kontinuierliche Verbesserung", "Fördern Sie regelmäßige Verbesserungen durch passende Methoden."),
        ("Weitere wichtige Faktoren", "Qualität der Dokumentation, Feedback-Schleifen, Kultur der Innovation, anpassungsfähige Strukturen.")
    ]
}

no_qopi_message = {
    'en': "Process implementation maturity not specified.",
    'de': "Prozess-Implementierungsreife nicht spezifiziert."
}

##############
### Legend ###
##############

# Legend and label texts
legend_title = {
    'en': "Legend",
    'de': "Legende"
}

#Color Assignment Logic Title
color_assignment_title = {
    'en': "Color Assignment Logic",
    'de': "Farbzuweisungslogik"
}

#Color Assignment Logic
color_legend_text = {
    'en': [
        "Below 50% of Baseline",          # Effektivität ist weniger als 50% der Grundlinie
        "50-80% of Baseline",             # Effektivität ist zwischen 50% und 80% der Grundlinie
        "80-100% of Baseline",            # Effektivität ist zwischen 80% und 100% der Grundlinie
        "Above Baseline, <50% to {SB_label}",  # Effektivität ist über der Grundlinie, aber weniger als 50% des Weges zum SOLL
        "Above Baseline, 50-80% to {SB_label}",  # Effektivität liegt zwischen 50% und 80% des Weges zum SOLL
        "Above Baseline, 80-100% to {SB_label}", # Effektivität liegt zwischen 80% und 100% des Weges zum SOLL
        "Above {SB_label}, <10%",          # Effektivität ist bis zu 10% über dem SOLL-Wert
        "Above {SB_label}, <20%",          # Effektivität ist zwischen 10% und 20% über dem SOLL-Wert
        "Above {SB_label}, >20%"           # Effektivität ist mehr als 20% über dem SOLL-Wert
    ],
    'de': [
        "Unter 50% der Grundlinie",        # Effektivität ist weniger als 50% der Grundlinie
        "50-80% der Grundlinie",           # Effektivität ist zwischen 50% und 80% der Grundlinie
        "80-100% der Grundlinie",          # Effektivität ist zwischen 80% und 100% der Grundlinie
        "Über der Grundlinie, <50% bis {SB_label}",  # Effektivität ist über der Grundlinie, aber weniger als 50% des Weges zum SOLL
        "Über der Grundlinie, 50-80% bis {SB_label}", # Effektivität liegt zwischen 50% und 80% des Weges zum SOLL
        "Über der Grundlinie, 80-100% bis {SB_label}",# Effektivität liegt zwischen 80% und 100% des Weges zum SOLL
        "Über {SB_label}, <10%",                 # Effektivität ist bis zu 10% über dem SOLL-Wert
        "Über {SB_label}, <20%",                 # Effektivität ist zwischen 10% und 20% über dem SOLL-Wert
        "Über {SB_label}, >20%"                  # Effektivität ist mehr als 20% über dem SOLL-Wert
    ]
}

### QoR ### 
legend_title_qor = {
    'en': "Result Quality - Show more information",
    'de': "Ergebnisqualität - Mehr Informationen anzeigen"
}

maturity_level_title_qor = {
    'en': "Result Quality Maturity Levels",
    'de': "Ergebnisqualität Reifegrade"
}

factor_descriptions_qor_title = {
    'en': "Important factors for result quality",
    'de': "Wichtige Faktoren für Ergebnisqualität"
}
 ### QoPI ### 
legend_title_qopi = {
    'en': "Process Implementation - Show more information",
    'de': "Prozess-Implementierung - Mehr Informationen anzeigen"
}

maturity_level_title_qopi = {
    'en': "Process Implementation Maturity Levels",
    'de': "Prozess-Implementierung Reifegrade"
}

factor_descriptions_qopi_title = {
    'en': "Important factors for Process Implementation Quality",
    'de': "Wichtige Faktoren für Prozess-Implementierungsqualität"
}

upload_prompt = {
    'en': "Please upload an Excel file to display measures.",
    'de': "Bitte laden Sie eine Excel-Datei hoch, um Maßnahmen anzuzeigen."
}
