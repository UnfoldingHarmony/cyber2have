import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgb, to_hex
from matplotlib.patheffects import withStroke  # Import for shadow effects

def draw_simple_explanation_scale_with_colors(determine_bar_color, baseline_threshold, should_be, selected_language, get_text, should_be_label, debug=False):
    """
    Draws a simple scale with colors determined by the `determine_bar_color` function.

    Parameters:
        determine_bar_color (function): Function to determine the bar color based on thresholds.
        baseline_threshold (float): The baseline threshold (e.g., 50).
        should_be (float): The SHOULD_BE threshold (e.g., 71).
        selected_language (str): The selected language ('de' or 'en').
        get_text (function): Function to retrieve language-specific texts.
        should_be_label (str): Dynamic label for the SHOULD_BE indicator.
        debug (bool): If True, prints debugging information to the terminal.
    """
    try:
        # Define the scale steps based on thresholds and logic
        thresholds = [0, 25, 40, baseline_threshold, 65, should_be, should_be + 10, 100]

        # Get the color for each threshold using determine_bar_color
        colors = []
        for value in thresholds:
            color = determine_bar_color(value, should_be, baseline_threshold)
            if isinstance(color, str):  # Convert to RGB if the color is a string
                color = to_rgb(color)
            colors.append(np.array(color))  # Convert to NumPy array

        # Debugging: Print thresholds and colors
        if debug:
            print(f"Thresholds: {thresholds}")
            print(f"Colors: {colors}")

        # Create the figure
        fig, ax = plt.subplots(figsize=(10, 2))
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 1)

        # Draw the gradient for each segment
        for i in range(len(thresholds) - 1):
            start_value = thresholds[i]
            end_value = thresholds[i + 1]
            start_color = colors[i]
            end_color = colors[i + 1]

            # Avoid division by zero
            step_range = end_value - start_value
            if step_range == 0:
                if debug:
                    print(f"Skipping segment: {start_value} to {end_value} (step_range is zero)")
                continue

            # Dynamically adjust the number of steps for smoothness
            steps = max(10, int(step_range * 10))  # Minimum 10 steps, proportional to segment width
            for t in np.linspace(0, 1, steps):
                interpolated_color = start_color * (1 - t) + end_color * t  # Interpolation
                ax.fill_betweenx([0, 1],
                                 start_value + t * step_range - 0.001,  # Slight overlap to avoid white lines
                                 start_value + (t + 1 / steps) * step_range + 0.001,  # Slight overlap
                                 color=to_hex(interpolated_color), edgecolor='none')

        # Add manager-friendly visual zones
        ax.axhspan(-0.4, -0.2, xmin=0, xmax=0.5, facecolor='red', alpha=0.1)  # Handlungsbedarf Zone
        ax.axhspan(-0.4, -0.2, xmin=0.5, xmax=1, facecolor='green', alpha=0.1)  # Optimieren Zone

        # Mark the baseline (50)
        baseline_label = get_text({'de': "CT-Grundlinie", 'en': "CT-Baseline"})
        ax.axvline(baseline_threshold, color='red', linestyle='--', linewidth=3)
        baseline_label_y = 1.05
        ax.text(baseline_threshold, baseline_label_y, get_text({'de': f"{baseline_label} erreicht", 'en': f"{baseline_label} Achieved"}), 
                ha='center', va='bottom', fontsize=10, color='red', fontweight='bold')

        # Mark the SHOULD_BE indicator (e.g., 71)
        ax.axvline(should_be, color='grey', linestyle='-', linewidth=3)
        should_be_label_y = 1.2
        ax.text(should_be, should_be_label_y, get_text({'de': f"{should_be_label} erreicht", 'en': f"{should_be_label} Achieved"}), 
                ha='center', va='bottom', fontsize=10, color='grey', fontweight='bold')

        # Add "Excellent, Keep Optimizing" starting at Baseline with shadow
        ax.text(baseline_threshold, -0.1, get_text({'de': "Bei Bedarf optimieren", 'en': "Optimize if necessary"}), 
                ha='left', va='top', fontsize=16, color='green', fontweight='bold', 
                path_effects=[withStroke(linewidth=3, foreground='white')])

        # Add "Needs Immediate Improvement" prominently between 0 and 50 with shadow
        ax.text(1, -0.1, get_text({'de': "Akut zu verbessern", 'en': "Needs Immediate Improvement"}), 
                ha='left', va='top', fontsize=16, color='red', fontweight='bold', 
                path_effects=[withStroke(linewidth=3, foreground='white')])

        # Add horizontal lines for visual separation
        ax.axhline(y=-0.05, xmin=0.15, xmax=0.85, color='gray', linestyle='--', linewidth=1.5)  # Slightly thicker line

        # Remove axes and frame
        ax.axis('off')

        return fig

    except Exception as e:
        print(f"Error while drawing the scale: {e}")
        raise