import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# === parameters ===
N = 100       # number of bits per simulation (you may change)
runs = 1000       # number of repeated simulations (do nor touch)
p_error_theory = 0.25  # theoretical error rate due to Eve

error_rates = []
# Alice and Bob work in the + basis. Eve doesn't know that so she geusses + or x (this may give errors)
for _ in range(runs): # Repeat the simulation many times (e.g., 1000 times) to get a distribution of error rates
    # Alice creates a random bit string of length N (each bit is 0 or 1) and sends the string
    alice_bits = np.random.randint(0, 2, N)

    # Eve doesn't know the correct basis, so she randomly picks + or x for each bit Alice sent
    eve_bases = np.random.choice(['+', 'x'], N)
    eve_bits = []

    # Eve measures the bits=> For each bit:
    # If Eve used the correct basis (+), she gets Alice’s bit.
    # If she used the wrong basis (x), she gets a random guess.
    for a_bit, e_base in zip(alice_bits, eve_bases):
        if e_base == '+':
            eve_bits.append(a_bit)  # correctly gets the bit
        else:
            eve_bits.append(np.random.randint(0, 2))  # guesses randomly

    # Eve resends the bit to Bob
    # Bob always measures in + basis
    # If Eve used the + basis => Bob gets her bit correctly
    # If Eve used x => Bob’s measurement is random → possible error
    bob_bits = []

    for e_bit, e_base in zip(eve_bits, eve_bases):
        if e_base == '+':
            bob_bits.append(e_bit)  # perfect transmission
        else:
            # Eve sent in x basis, Bob measures in + basis -> result is random
            bob_bits.append(np.random.randint(0, 2))  # 50% chance to get Alice's bit correctly

    # Compare Alice's original bits to Bob's final bits
    # count errors
    errors = np.sum(alice_bits != bob_bits) # Count how many bits Bob received incorrectly, and store the error rate for this simulation round
    error_rate = errors / N
    error_rates.append(error_rate)

    # Get a list of error_rates => one for each round => showing how often Eve caused errors
    # On average yields about 25%=0.25 error rate, which matches the theoretical prediction

# === statistics ===
mean_error = np.mean(error_rates)
std_error = np.std(error_rates)
std_binomial = np.sqrt(p_error_theory * (1 - p_error_theory) / N)
#N_sigma = abs(mean_error - p_error_theory) / std_binomial
combined_std = np.sqrt(std_error**2 + std_binomial**2)
N_sigma_combined = abs(mean_error - p_error_theory) / combined_std

# === plot with title ===
plt.figure(figsize=(10, 6))
plt.hist(error_rates, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')
x = np.linspace(min(error_rates), max(error_rates), 100)
plt.plot(x, norm.pdf(x, mean_error, std_error), 'r', linewidth=2)
#plt.title(f"Eve Induced Error Distribution (Fixed Basis, N={N}, {runs} runs)")
#plt.title(f"Eve Induced Error Distribution (N={N}, runs={runs})",fontsize=25)
plt.title(f"Eve Induced Error Distribution (N={N}, runs={runs})",fontsize=25)
plt.xlabel("Error Rate",fontsize=20)
plt.ylabel("Probability Density",fontsize=20)
#plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === plot no title ===
plt.figure(figsize=(10, 6))
plt.hist(error_rates, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')
x = np.linspace(min(error_rates), max(error_rates), 100)
plt.plot(x, norm.pdf(x, mean_error, std_error), 'r', linewidth=2)
#plt.title(f"Eve Induced Error Distribution (Fixed Basis, N={N}, {runs} runs)")
#plt.title(f"Eve Induced Error Distribution (N={N}, runs={runs})",fontsize=25)
plt.title(f"N={N}, runs={runs}",fontsize=25)
plt.xlabel("Error Rate",fontsize=20)
plt.ylabel("Probability Density",fontsize=20)
#plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === Print Results ===
print(f"N = {N}")
print(f"Mean error rate: {mean_error:.7f}")
print(f"Standard deviation (simulated): {std_error:.5f}")
print(f"Standard deviation (binomial expected): {std_binomial:.5f}")
print(f"N_sigma (|mean - 0.25| / σ_tot): {N_sigma_combined:.5f}")
