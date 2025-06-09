import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

# === parameters ===
N = 1000              # number of bits per run
runs = 1000           # number of simulations (don't change)
p_error = 0.25        # theoretical error rate

error_rates = []

for _ in range(runs):
    # Alice's random bits and bases
    alice_bits = np.random.randint(0, 2, N)
    alice_bases = np.random.choice(['+', 'x'], N)

    # Eve's random bases
    eve_bases = np.random.choice(['+', 'x'], N)
    eve_bits = []

    # Eve measures
    for a_bit, a_base, e_base in zip(alice_bits, alice_bases, eve_bases):
        if a_base == e_base:
            eve_bits.append(a_bit)
        else:
            eve_bits.append(np.random.randint(0, 2))

    # Eve sends to Bob using her basis
    bob_bases = np.random.choice(['+', 'x'], N)
    bob_bits = []
    for e_bit, e_base, b_base in zip(eve_bits, eve_bases, bob_bases):
        if e_base == b_base:
            bob_bits.append(e_bit)
        else:
            bob_bits.append(np.random.randint(0, 2))

    # compare Alice and Bob only when bases match
    mask = alice_bases == bob_bases
    valid_a_bits = alice_bits[mask]
    valid_b_bits = np.array(bob_bits)[mask]
    if len(valid_a_bits) > 0:
        disagreements = np.sum(valid_a_bits != valid_b_bits)
        error_rate = disagreements / len(valid_a_bits)
        error_rates.append(error_rate)

# === Statistics ===
mu = np.mean(error_rates)
std = np.std(error_rates)
sigma_binom = math.sqrt(p_error * (1 - p_error) / N)
N_sigma = abs(mu - p_error) / sigma_binom

# === Plot ===
plt.figure(figsize=(10, 6))
plt.hist(error_rates, bins=30, density=True, alpha=0.6, color='mediumorchid', edgecolor='black', label=f"Simulated (N={N})")
x = np.linspace(min(error_rates), max(error_rates), 100)
plt.plot(x, norm.pdf(x, mu, std), 'r', label=f"Gaussian Fit\nMean={mu:.4f}\nStd Dev={std:.4f}")
plt.title(f"Eve Error Rate Distribution (N={N}, {runs} runs)")
plt.xlabel("Error Rate")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === Print Results ===
print(f"N = {N}")
print(f"Mean error rate: {mu:.4f}")
print(f"Standard deviation (simulated): {std:.5f}")
print(f"Standard deviation (binomial expected): {sigma_binom:.5f}")
print(f"N_sigma (|mean - 0.25| / sigma_binom): {N_sigma:.5f}")
