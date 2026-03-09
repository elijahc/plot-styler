import os  # pathlib.Path.walk not available in Python <3.12
import matplotlib.pyplot as plt

from scienceplots.styles_discovery import read_styles_in_folders

import plot_styler

# register the bundled stylesheets in the matplotlib style library
mylib_path = plot_styler.__path__[0]
styles_path = os.path.join(mylib_path, "styles")

# Reads styles in /styles folder and all subfolders
stylesheets = read_styles_in_folders(styles_path)

# Update dictionary of styles - plt.style.library
plt.style.core.update_nested_dict(plt.style.library, stylesheets)
# Update `plt.style.available`, copy-paste from:
# https://github.com/matplotlib/matplotlib/blob/a170539a421623bb2967a45a24bb7926e2feb542/lib/matplotlib/style/core.py#L266  # noqa: E501
plt.style.core.available[:] = sorted(plt.style.library.keys())

def hello() -> str:
    return "Hello from plot-styler!"