import numpy as np
import matplotlib.pyplot as plt

class DTCEngine:
    """
    Differential Theory of Consciousness (DTC) Simulation Engine.
    Desenvolvido por Luiz Henrique Ribeiro de Moraes.
    """
    def __init__(self, fs=160, A=10.0, k=1.0, N=2.0, threshold=6.0):
        self.fs = fs           # Frequência de amostragem (Hz)
        self.A = A             # Ganho ambiental (Estímulo)
        self.k = k             # Constante de regulação
        self.N = N             # Resistência homeostática (Dissipação)
        self.threshold = threshold # Limiar de Ignição Semântica

    def simulate_consciousness(self, signal, initial_C=1.0):
        c_acc = initial_C
        dtc_history = []
        norm_signal = (signal - np.mean(signal)) / np.std(signal)

        for s in norm_signal:
            dc_dt = (self.A * abs(s) - (self.k * self.N * c_acc)) / self.fs
            c_acc += dc_dt
            c_acc = max(0, c_acc) 
            dtc_history.append(c_acc)
            
        return np.array(dtc_history)

# Exemplo de Simulação
fs = 160
t = np.linspace(0, 10, 10 * fs)
signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.random.normal(size=len(t))

engine = DTCEngine(A=12.0, N=0.85)
c_values = engine.simulate_consciousness(signal)

print(f"Máximo nível de consciência: {np.max(c_values):.2f}")
