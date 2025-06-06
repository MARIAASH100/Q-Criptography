import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
N = 100 # number of bits per simulation (you can change)
runs = 1000  # number of simulations (do not change)
p = 0.5  # theoretical agreement probability

agreement_rates = []  # stores percentage of agreements
agreement_strings = []  # stores bit strings of agreements

# simulation:
for _ in range(runs): # Repeat the whole process multiple times (e.g 1000 times)
    # Alice and Bob each randomly choosing measurement bases...+ or x
    alice_bases = np.random.choice(['+', 'x'], N)
    bob_bases = np.random.choice(['+', 'x'], N)
    # checks how often they chose the same basis out of N trials...
    # This checks for each bit if Alice and Bob used the same base
    # It creates a list of True (if they matched) and False (if they didn’t)
    agreement = (alice_bases == bob_bases) # boolean

    # Turns the True/False list into a string of "1"s and "0"s
    # 1 means they agreed on the base => 100% will have the same bit
    # 0 means they didn’t agree on the base => so this basis\bit discarded
    agreement_string = ''.join(['1' if a else '0' for a in agreement])
    agreement_strings.append(agreement_string)
    # Counts how many times they agreed on the basis, divides by N and saves that percentage
    agreement_rate = np.sum(agreement) / N
    agreement_rates.append(agreement_rate)

# === statistics ===
mean_agreement = np.mean(agreement_rates) #simulation: compare real data vs idealized distribution
std_agreement = np.std(agreement_rates) #simulation: also compare
std_binomial = np.sqrt(p * (1 - p) / N) #theoretical => Standard deviation of the fraction (agreement rate) - as we use %
#N_sigma = abs(mean_agreement - p) / std_binomial
combined_std = np.sqrt(std_agreement**2 + std_binomial**2)
N_sigma_combined = abs(mean_agreement - p) / combined_std


# === plot histogram with title ===
plt.figure(figsize=(10, 6))
plt.hist(agreement_rates, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black') #30 bins looks best compared to 25 and 35

# gaussian fit and plot
mu, std = norm.fit(agreement_rates) #same as mu=mean_agreement & std=std_agreement
x = np.linspace(*plt.xlim(), 100)
plt.plot(x, norm.pdf(x, mu, std), 'r', linewidth=2)



plt.title(f"Distribution of Agreement Rates (N={N}, runs={runs})", fontsize=25)
plt.xlabel("Agreement Rate", fontsize=20)
plt.ylabel("Probability Density", fontsize=20)
plt.grid(True)
plt.tight_layout()
plt.show()

# === plot histogram ni title ===
plt.figure(figsize=(10, 6))
plt.hist(agreement_rates, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black') #30 bins looks best compared to 25 and 35

# gaussian fit and plot
mu, std = norm.fit(agreement_rates) #same as mu=mean_agreement & std=std_agreement
x = np.linspace(*plt.xlim(), 100)
plt.plot(x, norm.pdf(x, mu, std), 'r', linewidth=2)



plt.title(f"N={N}, runs={runs}", fontsize=25)
plt.xlabel("Agreement Rate", fontsize=20)
plt.ylabel("Probability Density", fontsize=20)
plt.grid(True)
plt.tight_layout()
plt.show()

# === Print results ===
print(f"Mean agreement rate (mu Normal): {mean_agreement:.4f}")
#print("mu:",mu,"Mean agreement rate:",mean_agreement)  # for personal check
print(f"Standard deviation (simulated std Normal): {std_agreement:.5f}")
print(f"Standard deviation (binomial std theory): {std_binomial:.5f}")
print("mu-theo",p)
print(f"N_sigma (|mean - 0.5| / combined_std ): {N_sigma_combined:.5f}")

# optional: print first 5 agreement strings (good luck with 10000 bits)
#print("\nExample agreement strings (first 5):")
#for i in range(5):
#    print(f"{i + 1}: {agreement_strings[i]}")
