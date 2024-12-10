import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Set page configuration
st.set_page_config(page_title="Cyber Measures Assessment", layout="centered")

# Define language options and default language
language_options = {'de': 'Deutsch', 'en': 'English'}
selected_language = st.sidebar.radio("Sprache wählen / Choose Language", list(language_options.keys()), index=0)

# File uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Vorkehrungen Excel-Datei hochladen / Upload Measures Excel File", type=["xlsx"])

# Define captions and phase titles
page_titles = {
    'en': "Minimum standards against ransomware",
    'de': "Mindeststandards gegen Ransomware"
}

phase_titles = {
    'en': ["Governance", "Identify", "Protect", "Detect", "Respond", "Recover"],
    'de': ["Steuern", "Identifizieren", "Schützen", "Erkennen", "Reagieren", "Wiederherstellen"]
}

# Quality of Results Maturity Levels and descriptions
maturity_levels_qor = [
    (0, "Incomplete", "Unvollständig"),
    (15, "Initial", "Initial"),
    (35, "Basic Protection", "Basisabsicher."),
    (50, "Best Practice", "Bewährte Praxis"),
    (65, "Advanced", "Erweitert"),
    (85, "State of the Art", "Stand der Technik")
]

maturity_descriptions_qor = {
    'en': [
        ("Level 1:", "Initial", "Measures show occasional effectiveness, but without consistency. (Features: Inconsistent implementation, no systematic planning, occasional successes, but no reliability.)"),
        ("Level 2:", "Basic Protection", "Basic protective measures are implemented to meet fundamental security requirements. (Features: Fulfillment of minimal security requirements, use of standard protocols, focus on basic protection. Acceptance present)"),
        ("Level 3:", "Best Practice", "Security measures adhere to recognized and proven practices. Few exceptions. (Features: Use of established methods and standards, regular review and adjustment, consistent application with less than 10% exceptions. Good acceptance)"),
        ("Level 4:", "Advanced", "Measures are comprehensive and specifically address targeted threats. Very few exceptions. (Features: Comprehensive coverage of specific threats, proactive security strategies, less than 5% exceptions. High acceptance)"),
        ("Level 5:", "State of the Art", "Security measures are highly developed and set industry standards. Almost no exceptions. (Features: Use of cutting-edge technologies, industry-leading standards, less than 1% exceptions. Excellent acceptance)")
    ],
    'de': [
        ("Level 1:", "Initial", "Maßnahmen zeigen gelegentlich Wirksamkeit, aber ohne Konsistenz. (Merkmale: Inkonsequente Umsetzung, keine systematische Planung, gelegentliche Erfolge, aber keine Verlässlichkeit.)"),
        ("Level 2:", "Basisabsicherung", "Grundlegende Schutzmaßnahmen sind implementiert, um grundlegende Sicherheitsanforderungen zu erfüllen. (Merkmale: Erfüllung minimaler Sicherheitsanforderungen, Standardprotokolle werden genutzt, Fokus auf grundlegenden Schutz. Akzeptanz vorhanden)"),
        ("Level 3:", "Bewährte Praxis", "Sicherheitsmaßnahmen entsprechen anerkannten und erprobten Praktiken. Wenige Ausnahmen. (Merkmale: Nutzung bewährter Methoden und Standards, regelmäßige Überprüfung und Anpassung, konsistente Anwendung mit weniger als 10% Ausnahmen. Gute Akzeptanz)"),
        ("Level 4:", "Erweitert", "Maßnahmen sind umfassend und adressieren spezifische Bedrohungen gezielt. Sehr wenige Ausnahmen. (Merkmale: Umfassende Abdeckung spezifischer Bedrohungen, proaktive Sicherheitsstrategien, weniger als 5% Ausnahmen. Hohe Akzeptanz)"),
        ("Level 5:", "Stand der Technik", "Sicherheitsmaßnahmen sind hochentwickelt und setzen Maßstäbe in der Branche. Nahezu keine Ausnahmen. (Merkmale: Nutzung modernster Technologien, branchenführende Standards, weniger als 1% Ausnahmen. Hervorragende Akzeptanz)")
    ]
}

# Quality of Process Implementation Maturity Levels and descriptions
maturity_levels_qopi = [
    (0, "Incomplete", "Unvollständig"),
    (15, "Initial", "Initial"),
    (35, "Repeatable", "Wiederholbar"),
    (50, "Defined", "Definiert"),
    (65, "Managed", "Verwaltet"),
    (85, "Optimizing", "Optimierend")
]

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

# Define thresholds for multiple maturity levels
baseline_threshold_qor = 50
should_be_threshold_qor = 50  # Standard value, adjust as needed in Excel
baseline_threshold_qopi = 50
should_be_threshold_qopi = 50  # Standard value, adjust as needed in Excel

color_legend_text = {
    'en': [
        "Below Maturity Baseline or >30% from SHOULD BE",
        "20%-30% from SHOULD BE",
        "<20% from SHOULD BE",
        "At or Above SHOULD BE"
    ],
    'de': [
        "Unter Reifegrad-Grundlinie oder >30% vom SOLL",
        "20%-30% vom SOLL",
        "<20% vom SOLL",
        "Am oder über dem SOLL"
    ]
}

# Define legend and label texts
legend_title = {
    'en': "Legend",
    'de': "Legende"
}

color_assignment_title = {
    'en': "Color Assignment Logic",
    'de': "Farbzuweisungslogik"
}

maturity_level_title_qor = {
    'en': "Quality of Results Maturity Levels",
    'de': "Reifegrade der Ergebnisqualität"
}

# Function to determine bar color
def determine_bar_color(effectiveness_qor, should_be_qor):
    if effectiveness_qor < baseline_threshold_qor:
        return 'red'
    distance = should_be_qor - effectiveness_qor
    if distance <= 0:
        return 'green'
    elif distance < 20:
        return 'yellow'
    elif distance <= 30:
        return 'orange'
    else:
        return 'red'

# Display page title
st.title(page_titles[selected_language])

# Process the uploaded file
if uploaded_file:
    # Load measures data
    measures_data = pd.read_excel(uploaded_file)

    # Determine column name for measure title based on selected language
    measure_title_column = 'Measure' if selected_language == 'en' else 'Vorkehrung'

    # Iterate through each phase
    for phase_index, phase_name in enumerate(phase_titles[selected_language], start=1):
        st.header(phase_name)
        
        # Filter measures for the current phase
        phase_measures = measures_data[measures_data['Phase number'] == phase_index]
        
        for _, measure in phase_measures.iterrows():
            # Retrieve measure details
            measure_number = measure['Measure Number']
            measure_title = measure[measure_title_column]
            effectiveness_qor = measure['QoR effectiviness from 0-100']
            should_be_qor = measure['QoR SHOULD BE indication from 0-100']
            effectiveness_qopi = measure['QoPI effectiviness from 0-100']
            should_be_qopi = measure['QoPI SHOULD BE indication from 0-100']

            # Determine color using the algorithm
            bar_color = determine_bar_color(effectiveness_qor, should_be_qor)

            # Create the static plot
            fig, ax = plt.subplots(figsize=(8, 0.6))
            
            # Draw the effectiveness_qor bar
            ax.barh([0], [effectiveness_qor], color=bar_color, edgecolor='white', height=0.4)

            # Add QoR maturity thresholds
            for threshold, en_label, de_label in maturity_levels_qor:
                ax.axvline(threshold, color='black', linestyle='--', linewidth=0.5)
                label = de_label if selected_language == "de" else en_label
                ax.text(threshold, 0.3, label, rotation=0, va='bottom', ha='left', fontsize=8, color='gray', alpha=0.7)

            # Add QoR baseline
            baseline_label = "CT-Grundlinie" if selected_language == "de" else "CT-Baseline"
            ax.axvline(baseline_threshold_qor, color='red', linestyle='-', linewidth=2)

            # Add prominent SHOULD BE indicator
            should_be_color = 'green' if effectiveness_qor >= should_be_qor else 'orange'
            ax.axvline(should_be_qor, color=should_be_color, linewidth=3)

            # Decide on label positions
            if should_be_qor < baseline_threshold_qor and abs(baseline_threshold_qor - should_be_qor) <= 10:
                # SHOULD BE is close and less than baseline
                ax.text(baseline_threshold_qor, -0.3, baseline_label, rotation=0, va='top', ha='center', fontsize=10, color='red')
                ax.text(should_be_qor, -0.6, "SHOULD BE", rotation=0, va='top', ha='center', fontsize=10, color=should_be_color)
            elif should_be_qor < baseline_threshold_qor:
                # SHOULD BE is less and far from baseline
                ax.text(baseline_threshold_qor, -0.3, baseline_label, rotation=0, va='top', ha='center', fontsize=10, color='red')
                ax.text(should_be_qor, -0.3, "SHOULD BE", rotation=0, va='top', ha='center', fontsize=10, color=should_be_color)
            elif should_be_qor > baseline_threshold_qor and abs(should_be_qor - baseline_threshold_qor) <= 10:
                # SHOULD BE is close and greater than baseline
                ax.text(baseline_threshold_qor, -0.3, baseline_label, rotation=0, va='top', ha='center', fontsize=10, color='red')
                ax.text(should_be_qor, -0.6, "SHOULD BE", rotation=0, va='top', ha='center', fontsize=10, color=should_be_color)
            else:
                # SHOULD BE is greater and far from baseline
                ax.text(baseline_threshold_qor, -0.3, baseline_label, rotation=0, va='top', ha='center', fontsize=10, color='red')
                ax.text(should_be_qor, -0.3, "SHOULD BE", rotation=0, va='top', ha='center', fontsize=10, color=should_be_color)

            # Customize plot
            ax.set_xlim(0, 100)
            ax.set_ylim(-0.25, 0.25)
            ax.set_yticks([])
            ax.set_xticks([])
            ax.set_title(f"{measure_number}: {measure_title}", fontsize=12, pad=20)
            ax.set_facecolor('white')

            # Adjust subplot parameters to give space for labels
            plt.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.3)

            st.pyplot(fig)

        st.markdown("---")

    # Display legend for color assignment logic
    st.subheader(legend_title[selected_language])
    st.markdown(f"### {color_assignment_title[selected_language]}")

    # Use Matplotlib patches to create a legend
    fig, ax = plt.subplots(figsize=(8, 0.5))
    ax.axis('off')
    red_patch = mpatches.Patch(color='red', label=color_legend_text[selected_language][0])
    orange_patch = mpatches.Patch(color='orange', label=color_legend_text[selected_language][1])
    yellow_patch = mpatches.Patch(color='yellow', label=color_legend_text[selected_language][2])
    green_patch = mpatches.Patch(color='green', label=color_legend_text[selected_language][3])
    ax.legend(handles=[red_patch, orange_patch, yellow_patch, green_patch], loc='center', fontsize=8, ncol=4)
    st.pyplot(fig)

    # Display maturity descriptions
    st.subheader(maturity_level_title_qor[selected_language])
    for level, title, description in maturity_descriptions_qor[selected_language]:
        st.markdown(f"- **{level} {title}**: {description}")

else:
    st.info("Bitte laden Sie eine Excel-Datei hoch, um Maßnahmen anzuzeigen.")

# Run this file with: streamlit run filename.py