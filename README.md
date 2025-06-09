# Q-Criptography
Simulations that tests the BB84 quantum key distribution protocol by modeling the key agreement process with and without an eavesdropper to verify expected error and agreement rates.
## QC - agreement rate (sim1).py
This simulation models the key generation stage of the BB84 protocol in the absence of an eavesdropper. Alice and Bob each randomly choose a sequence of $N$ measurement bases (+ or ×), and the simulation checks how often their choices match. Repeating this process 1000 times, we compute the agreement rate for each run and compare the distribution to the expected binomial behavior with $p=0.5$. The results confirm that about half the bits can be used for key generation when no interference is present.
