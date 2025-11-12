import os
import matplotlib.pyplot as plt


def show_and_save_plot(filename: str, image_dir: str):
    """
    Tightens layout, saves the plot to the specified directory, displays it, and prints a save message.

    Parameters:
    - filename (str): The name of the file to save (e.g., 'plot.png').
    - image_dir (str): The directory path where the plot should be saved.

    Returns:
    - None
    """
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, filename), dpi=300, bbox_inches='tight')
    plt.show()
    print(f"Saved: {filename}")
