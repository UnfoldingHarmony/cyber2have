import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from config import (
    language_options, page_titles, input_error_messages, required_input_columns,
    phase_titles, qor_titles, maturity_levels_qor, maturity_descriptions_qor,
    maturity_levels_qopi, qopi_titles, maturity_descriptions_qopi, legend_title, color_assignment_title,
    maturity_level_title_qor, upload_prompt, no_qopi_message, color_legend_text,
    baseline_threshold_qor, should_be_threshold_qor, legend_title_qor, factor_descriptions_qor, 
    factor_descriptions_qor_title, baseline_threshold_qopi, should_be_threshold_qopi,
    legend_title_qor, factor_descriptions_qor, factor_descriptions_qor_title,
    legend_title_qopi, maturity_level_title_qopi, factor_descriptions_qopi_title,
    factor_descriptions_qopi
)

# Set page configuration
st.set_page_config(page_title="Cyber Measures Assessment", layout="centered")

# Define language options and default language
selected_language = st.sidebar.radio(
    "Sprache wählen / Choose Language", 
    list(language_options.keys()), 
    index=0
)

# Add a horizontal line for separation
st.sidebar.markdown("---")

# Function to get language-specific text
def get_text(dictionary):
    return dictionary[selected_language]

# Sidebar input for alternative "SHOULD BE" label
st.sidebar.markdown("### " + get_text({
    'de': "Label-Anpassung",
    'en': "Label Customization"
}))

alternative_should_be_label_input = st.sidebar.text_input(
    get_text({
        'de': "Alternative Bezeichnung für SHOULD BE (max. 25)",
        'en': "Alternative label for SHOULD BE (max. 25)"
    }),
    value="",
    max_chars=25
)

st.sidebar.markdown("---")  # Add a horizontal line for separation

# File uploader in the sidebar
uploaded_file = st.sidebar.file_uploader(
    get_text({
        'de': "Bewertungsdatei im XLSX-Format hochladen",
        'en': "Upload Measures XLSX File"
    }), 
    type=["xlsx"]
)

# Use the alternative label if provided, otherwise use the default
should_be_label = alternative_should_be_label_input if alternative_should_be_label_input else "SHOULD BE"

# Calculate dynamic width based on alternative label length
should_be_label_length = len(should_be_label)
fig_width = max(8, should_be_label_length * 0.2)  # Adjust width dynamically

# Function to determine bar color
def determine_bar_color(effectiveness, should_be, baseline_threshold):
    if effectiveness < baseline_threshold:
        if effectiveness < baseline_threshold * 0.5:
            return 'red'
        elif effectiveness < baseline_threshold * 0.8:
            return 'orange'
        else:
            return 'yellow'
    elif effectiveness <= should_be:
        progress = (effectiveness - baseline_threshold) / (should_be - baseline_threshold)
        if progress < 0.5:
            return 'lightgreen'
        elif progress < 0.8:
            return 'green'
        else:
            return 'darkgreen'
    else:
        surplus = effectiveness - should_be
        if surplus <= 10:
            return 'lightblue'
        elif surplus <= 20:
            return 'blue'
        else:
            return 'darkblue'

# Function to create a plot
def create_plot(effectiveness, should_be, baseline_threshold, title):
    bar_color = determine_bar_color(effectiveness, should_be, baseline_threshold)

    fig, ax = plt.subplots(figsize=(8, 0.6))
    ax.barh([0], [effectiveness], color=bar_color, edgecolor='white', height=0.4)

    # Add maturity thresholds
    thresholds = maturity_levels_qor if "Ergebnis" in title else maturity_levels_qopi
    for threshold, en_label, de_label in thresholds:
        ax.axvline(threshold, color='black', linestyle='--', linewidth=0.5)
        label = de_label if selected_language == "de" else en_label
        ax.text(threshold, 0.3, label, rotation=0, va='bottom', ha='left', fontsize=8, color='gray', alpha=0.7)

    # Add baseline
    baseline_label = "CT-Grundlinie" if selected_language == "de" else "CT-Baseline"
    ax.axvline(baseline_threshold, color='red', linestyle='-', linewidth=2)

    # Add prominent SHOULD BE indicator
    if should_be:
        should_be_color = 'green' if effectiveness >= should_be else 'orange'
        ax.axvline(should_be, color=should_be_color, linewidth=3)
        
        # Decide on label positions to avoid overlap
        if abs(baseline_threshold - should_be) <= ((should_be_label_length / 2) + 8):
            ax.text(baseline_threshold, -0.3, baseline_label, rotation=0, va='top', ha='center', fontsize=8, color='red')
            ax.text(should_be, -0.5, should_be_label, rotation=0, va='top', ha='center', fontsize=8, color=should_be_color)
        else:
            ax.text(baseline_threshold, -0.3, baseline_label, rotation=0, va='top', ha='center', fontsize=8, color='red')
            ax.text(should_be, -0.3, should_be_label, rotation=0, va='top', ha='center', fontsize=8, color=should_be_color)

    # Customize plot
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.25, 0.25)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_title(title, fontsize=12, pad=20)
    ax.set_facecolor('white')

    # Adjust subplot parameters to give space for labels
    plt.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.3)

    return fig

# Display page title
st.title(get_text(page_titles))

# Process the uploaded file
if uploaded_file:
    try:
        # Load measures data
        measures_data = pd.read_excel(uploaded_file)
        
        # Check if required columns are present
        if not all(column in measures_data.columns for column in required_input_columns):
            missing_columns_text = get_text(input_error_messages['missing_columns']).format(columns=', '.join(required_input_columns))
            st.error(missing_columns_text)
            st.stop()

        # Validate data ranges for all relevant columns
        range_columns = [
            'QoR effectiviness from 0-100', 
            'QoR SHOULD BE indication from 0-100', 
            'QoPI effectiviness from 0-100', 
            'QoPI SHOULD BE indication from 0-100'
        ]
        
        for column in range_columns:
            if not measures_data[column].between(0, 100).all():
                range_error_text = get_text(input_error_messages['range_error'])
                st.error(range_error_text)
                st.stop()

        # Continue processing...
        # Determine column name for measure title based on selected language
        measure_title_column = 'Measure' if selected_language == 'en' else 'Vorkehrung'

        # Iterate through each phase
        for phase_index, phase_name in enumerate(get_text(phase_titles), start=1):
            # Display phase symbol and title
            symbol_path = f"symbols/{phase_titles['en'][phase_index - 1].lower()}.png"
            col1, col2 = st.columns([0.11,0.89], gap='small', vertical_alignment='center')
            with col1:
                st.image(symbol_path, use_container_width=True)
                #st.image(symbol_path)
            with col2:
                #st.markdown(f"<div style='display:flex; align-items:start;'><h2>{phase_name}</h2></div>", unsafe_allow_html=True)
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
                should_be_qopi = measure.get('QoPI SHOULD BE indication from 0-100', None)

                # Display measure title
                st.markdown(f"### {measure_number}: {measure_title}")

                # Plot Result Maturity
                st.pyplot(create_plot(effectiveness_qor, should_be_qor, baseline_threshold_qor, get_text(qor_titles)))

                # Plot Process Implementation Maturity if applicable
                if pd.notna(effectiveness_qopi) and effectiveness_qopi > 0:
                    st.pyplot(create_plot(effectiveness_qopi, should_be_qopi, baseline_threshold_qopi, get_text(qopi_titles)))
                else:
                    st.markdown(f"<div style='background-color: #e0f7fa; padding: 5px; border-radius: 5px; font-size: 0.9em;'>{get_text(no_qopi_message)}</div>", unsafe_allow_html=True)

                st.markdown("---")

        # Dynamically update the color legend text
        updated_color_legend_text = {
            lang: [text.format(SB_label=should_be_label) for text in texts]
            for lang, texts in color_legend_text.items()
        }

        # Display legend for color assignment logic
        st.header(get_text(legend_title))
        #st.markdown(f"#### {get_text(color_assignment_title)}")
        st.subheader(get_text(color_assignment_title))

        ###
        # Use Matplotlib patches to create a legend
        fig, ax = plt.subplots(figsize=(fig_width, 0.6))
        ax.axis('off')
        # Define the colors and corresponding labels
        colors = ['red', 'orange', 'yellow', 'lightgreen', 'green', 'darkgreen', 'lightblue', 'blue', 'darkblue']
        labels = get_text(updated_color_legend_text)
        # Create patches for each color and corresponding label
        patches = [mpatches.Patch(color=color, label=label) for color, label in zip(colors, labels)]
        # Add the legend to the plot
        ax.legend(handles=patches, loc='center', fontsize=8, ncol=3)
        # Display the plot in a Streamlit app
        st.pyplot(fig)
        ###

        ### QoR ### 
        # Ausklappbarer Bereich mit einem Titel
        with st.expander(get_text(legend_title_qor)):
            #st.subheader(get_text(legend_title_qor))
            # Display maturity descriptions
            st.markdown(f"####  {get_text(maturity_level_title_qor)}")
            for level, title, description in get_text(maturity_descriptions_qor):
                st.markdown(f"- **{level} {title}**: {description}")
            # Display QoR factor_descriptions
            st.markdown(f"####  {get_text(factor_descriptions_qor_title)}")
            for factor, description in get_text(factor_descriptions_qor):
                st.markdown(f"- **{factor}**: {description}")

        ### QoPI ### 
        with st.expander(get_text(legend_title_qopi)):
            #st.subheader(get_text(legend_title_qopi))
            # Display maturity descriptions
            st.markdown(f"####  {get_text(maturity_level_title_qopi)}")
            for level, title, description in get_text(maturity_descriptions_qopi):
                st.markdown(f"- **{level} {title}**: {description}")
            # Display QoR factor_descriptions
            st.markdown(f"####  {get_text(factor_descriptions_qopi_title)}")
            for factor, description in get_text(factor_descriptions_qopi):
                st.markdown(f"- **{factor}**: {description}")

    except Exception as e:
        general_error_text = get_text(input_error_messages['general_error']).format(error=str(e))
        st.error(general_error_text)
else:
    st.info(get_text(upload_prompt))
    
# Run this file with: streamlit run app.py