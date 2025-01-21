import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
import math
from PIL import Image, ImageTk

def harmonic_oscillator_wavefunction(n, x):
    coeff = np.sqrt(1 / (2**n * math.factorial(n))) * (np.pi**-0.25)
    hermite_poly = np.polynomial.hermite.Hermite([0]*n + [1])(x)
    return coeff * hermite_poly * np.exp(-x**2 / 2)

def potential(x):
    return 0.5 * x**2

def plot_harmonic_oscillator(ax, max_state, selected_state=None):
    x = np.linspace(-4, 4, 500)
    ax.plot(x, potential(x), 'k-', label="Potential (1/2 x²)")
    for n in range(max_state + 1):
        if selected_state is not None and n != selected_state:
            continue
        y = harmonic_oscillator_wavefunction(n, x) + n
        ax.plot(x, y, label=f"State {n}")
        ax.axhline(n, linestyle='dotted', color='gray')
    ax.set_title("Harmonic Oscillator with Potential")
    ax.set_xlabel("x")
    ax.set_ylabel("ψ(x) + Energy Level")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)

def plot_half_harmonic_oscillator(ax, max_state, selected_state=None):
    x = np.linspace(0, 4, 500)
    ax.plot(x, potential(x), 'k-', label="Potential (1/2 x²)")
    for n in range(max_state + 1):
        if selected_state is not None and n != selected_state:
            continue
        y = harmonic_oscillator_wavefunction(n, x) + n
        ax.plot(x, y, label=f"State {n}")
        ax.axhline(n, linestyle='dotted', color='gray')
    ax.set_title("Half Harmonic Oscillator with Potential")
    ax.set_xlabel("x")
    ax.set_ylabel("ψ(x) + Energy Level")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)

def plot_superposition(ax, max_state, selected_state=None):
    x_full = np.linspace(-4, 4, 500)
    x_half = np.linspace(0, 4, 500)
    ax.plot(x_full, potential(x_full), 'k-', label="Potential (1/2 x²)")
    for n in range(max_state + 1):
        if selected_state is not None and n != selected_state:
            continue
        y_full = harmonic_oscillator_wavefunction(n, x_full) + n
        y_half = harmonic_oscillator_wavefunction(n, x_half) + n
        ax.plot(x_full, y_full, label=f"Full State {n}")
        ax.plot(x_half, y_half, '--', label=f"Half State {n}")
        ax.axhline(n, linestyle='dotted', color='gray')
    ax.set_title("Superposition of Full and Half Harmonic Oscillator")
    ax.set_xlabel("x")
    ax.set_ylabel("ψ(x) + Energy Level")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)

def update_plots():
    state = state_var.get()
    max_state = 10
    selected_state = None if state == "All States" else int(state)
    for ax in axes:
        ax.clear()
    plot_harmonic_oscillator(axes[0], max_state, selected_state)
    plot_half_harmonic_oscillator(axes[1], max_state, selected_state)
    plot_superposition(superposition_ax, max_state, selected_state)
    for canvas in canvases:
        canvas.draw()
    superposition_canvas.draw()

def open_github(event):
    import webbrowser
    webbrowser.open("https://github.com/shashwatanayak")

def send_email(event):
    import webbrowser
    webbrowser.open("mailto:shashwata@versatilex.in")

root = tk.Tk()
root.title("Quantum Harmonic Oscillator Visualization Tool")

try:
    logo_img = Image.open("logo.png").resize((50, 50))
    logo = ImageTk.PhotoImage(logo_img)
    root.iconphoto(False, logo)
except:
    pass

header_frame = tk.Frame(root)
header_frame.grid(row=0, column=0, columnspan=3, pady=10)
header_label = tk.Label(header_frame, text="Quantum Harmonic Oscillator - Visualization Tool", font=("Arial", 16, "bold"))
header_label.pack()

state_label = tk.Label(root, text="Select State:", font=("Arial", 10))
state_label.grid(row=1, column=0, padx=5, sticky="e")
state_var = tk.StringVar(value="All States")
states = ["All States"] + [str(i) for i in range(11)]
dropdown = ttk.Combobox(root, textvariable=state_var, values=states, state="readonly")
dropdown.grid(row=1, column=1, padx=10, pady=10)
calc_button = tk.Button(root, text="Calculate", command=update_plots)
calc_button.grid(row=1, column=2, padx=10, pady=10)

info_window = tk.LabelFrame(root, text="Program Information", padx=10, pady=10)
info_window.grid(row=2, column=3, rowspan=3, padx=10, pady=10, sticky="nsew")
info_text = tk.Text(info_window, wrap="word", height=40, width=40)
info_text.insert(
    tk.END,
    "How to Use:\n"
    "- Select a quantum state (0 to 10) from the dropdown menu.\n"
    "- Click 'Calculate' to generate the plots.\n\n"
    "Features:\n"
    "- The left plot shows the wavefunctions and energy levels of the Full Harmonic Oscillator.\n"
    "- The right plot shows the wavefunctions and energy levels of the Half Harmonic Oscillator.\n"
    "- The bottom plot shows the superposition of the Full and Half Harmonic Oscillator.\n\n"
    "------ \n\n"
    "Developed by: Shashwata Nayak\n"
    "Platform: [Python - numpy] \n"
    "Commit Allowed: [Y] \n\n"
    "------ \n\n"
    "Libraries Required:\n"
    "matplotlib - pip install matplotlib\n"
    "numpy - pip install numpy\n"
    "Pillow - pip install pillow\n\n"
    "To install all libraries, open cmd and run:\n"
    "pip install matplotlib numpy pillow\n\n"

)
info_text.config(state="disabled")
info_text.pack()

footer_frame = tk.Frame(root)
footer_frame.grid(row=5, column=0, columnspan=3, pady=10)
developer_label = tk.Label(footer_frame, text="This Program is Developed by ", font=("Arial", 10, "bold"))
developer_label.pack(side="left")
github_link = tk.Label(footer_frame, text="Shashwata Nayak", fg="blue", cursor="hand2", font=("Arial", 10, "bold"))
github_link.pack(side="left")
github_link.bind("<Button-1>", open_github)
github_label = tk.Label(footer_frame, text=" | GitHub Repository: ", font=("Arial", 10, "bold"))
github_label.pack(side="left")
github_repo = tk.Label(footer_frame, text="[Click Here]", fg="blue", cursor="hand2", font=("Arial", 10, "bold"))
github_repo.pack(side="left")
github_repo.bind("<Button-1>", open_github)
contact_label = tk.Label(footer_frame, text=" | For any GitCommit directly Contact: ", font=("Arial", 10, "bold"))
contact_label.pack(side="left")
contact_email = tk.Label(footer_frame, text="shashwata@versatilex.in", fg="blue", cursor="hand2", font=("Arial", 10, "bold"))
contact_email.pack(side="left")
contact_email.bind("<Button-1>", send_email)

figures = [plt.figure(figsize=(6, 4)) for _ in range(2)]
axes = [fig.add_subplot(111) for fig in figures]
canvases = [FigureCanvasTkAgg(fig, root) for fig in figures]

superposition_fig = plt.figure(figsize=(12, 4))
superposition_ax = superposition_fig.add_subplot(111)
superposition_canvas = FigureCanvasTkAgg(superposition_fig, root)

for i, canvas in enumerate(canvases):
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=3, column=i, padx=10, pady=10)

superposition_canvas_widget = superposition_canvas.get_tk_widget()
superposition_canvas_widget.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

update_plots()

root.mainloop()
