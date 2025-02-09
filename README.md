# Quantum Harmonic Oscillator Visualization Tool

A minimalist and efficient tool to visualize the energy levels and wavefunctions of the **Quantum Harmonic Oscillator** and **Half Harmonic Oscillator** up to the 10th state. The tool includes a side-by-side comparison of the oscillators with an additional superposition plot for better visualization and analysis.

### A preview of the Python App is available for Web - [Try Now](https://shashwatanayak.github.io/minimalist-quantum-lho/)

---

## Features

- **Visualize Full Harmonic Oscillator**:
  - Energy levels and wavefunctions for quantum states from 0 to 10.
- **Visualize Half Harmonic Oscillator**:
  - Energy levels and wavefunctions with boundaries restricted to one side.
- **Superposition Plot**:
  - Compare the Full and Half Harmonic Oscillator states in a single combined plot.
- **Interactive GUI**:
  - Select a specific state using a dropdown and dynamically update the plots.

---

## How to Use

1. To clone this repository, use the following command:
   ```bash
   git clone https://github.com/shashwatanayak/minimalist-quantum-lho.git

2. Alternatively, you can download the [Zip File](https://github.com/shashwatanayak/minimalist-quantum-lho/blob/main/harmonic_oscillator_visualization.zip) directly from the repository.
  
3. Install Required Libraries:
   ```bash
   pip install matplotlib numpy pillow
   ```

4. Run the Program:
   ```bash
   python harmonic_oscillator_visualization.py
   ```

5. Explore the GUI:
   - Select a quantum state (0 to 10) from the dropdown.
   - Click "Calculate" to update the plots.

---

## Libraries Required

- **Matplotlib** - `pip install matplotlib`
- **NumPy** - `pip install numpy`
- **Pillow** - `pip install pillow`

To install all libraries at once:
```bash
pip install matplotlib numpy pillow
```

---

## Program Overview

This tool provides a graphical representation of the energy levels and wavefunctions of the **Quantum Harmonic Oscillator**. It includes:

1. **Full Harmonic Oscillator**:
   - Symmetric wavefunctions across the potential well.
2. **Half Harmonic Oscillator**:
   - Wavefunctions restricted to one side of the potential well.
3. **Superposition Plot**:
   - Overlay of Full and Half Harmonic Oscillator wavefunctions for comparison.

The tool is designed to help users understand the behavior of quantum harmonic oscillators and their boundary conditions.

---

## How the GUI Works

- **Dropdown**:
  - Select a specific quantum state (e.g., 0 for ground state, 1 for the first excited state, etc.).
- **Calculate Button**:
  - Updates all plots dynamically based on the selected state.
- **Plots**:
  - **Left Plot**: Full Harmonic Oscillator wavefunctions and energy levels.
  - **Right Plot**: Half Harmonic Oscillator wavefunctions and energy levels.
  - **Bottom Plot**: Superposition of Full and Half Harmonic Oscillator wavefunctions.

---

## Example Output

Below is an example of the GUI interface and plots:

![Quantum Harmonic Oscillator Visualization - 1st Excited State](screenshot.png)
![Quantum Harmonic Oscillator Visualization - All States](screenshot2.png)

---

## Developed By

**Shashwata Nayak**  
- **GitHub Repository**: [Click Here](https://github.com/shashwatanayak/minimalist-quantum-lho)  
- **Contact**: [shashwata@versatilex.in](mailto:shashwata@versatilex.in)

---

## Future Enhancements

- Include support for arbitrary boundary conditions.
- Add functionality for visualizing higher quantum states.
- Implement additional quantum systems like the anharmonic oscillator.

---

Enjoy exploring the quantum world!

