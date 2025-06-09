# Q-Criptography
Simulations that tests the BB84 quantum key distribution protocol by modeling the key agreement process with and without an eavesdropper to verify expected error and agreement rates.
## QC - agreement rate (sim1).py
This simulation models the key generation stage of the BB84 protocol in the absence of an eavesdropper. Alice and Bob each randomly choose a sequence of $N$ measurement bases (+ or ×), and the simulation checks how often their choices match. Repeating this process 1000 times, we compute the agreement rate for each run and compare the distribution to the expected binomial behavior with $p=0.5$. The results confirm that about half the bits can be used for key generation when no interference is present.
## QC - error rate (sim3).py
This simulation models how an eavesdropper (Eve) affects the BB84 protocol during message transmission, after key agreement. Alice sends a random bit string, and Eve intercepts it by measuring each bit in a randomly chosen basis (+ or ×). She then resends the result to Bob, who always measures in the + basis. When Eve chooses the wrong basis, her measurement introduces errors. Repeating this process 1000 times, we record the error rate—the percentage of bits where Bob's result differs from Alice’s. The average error rate converges to the theoretical value of $p=0.25$, demonstrating the impact of Eve’s presence on the transmission and highlighting how BB84 enables eavesdropper detection.

NOTE: Although this simulation is described as the message transmission stage, it is effectively equivalent to the key generation stage in BB84 with Eve present. In both cases, Alice and Bob only compare bits where their bases match. In this simulation, we assume they always use the same basis (e.g. +), so there's no need to discard mismatched bases—just like in the post-selection step of BB84. The error rate we compute here reflects how many of the kept bits are affected by Eve’s interference.
For a full simulation that includes random and independent basis choices by Alice and Bob (and discards mismatched ones), see the third script: "QC - error rate in BB84.py"

## Inputs
N - Number of bits per simulation (e.g. 100)
runs: Number of repeated simulations (e.g. 1000)

## Outputs:
1)  Simulation Without Eve (Ideal BB84 Key Agreement):
* Output: Distribution of agreement rates — how often Alice and Bob choose the same basis
* Expected mean: ≈ 0.5 (since + or × are chosen randomly and independently)
* Used for: Verifying that ~50% of bits can be used to form a shared key when Eve is absent.
2)   Simulation With Eve (Message Transmission with Interference):
* Output: Distribution of error rates — how often Bob’s bit differs from Alice’s due to Eve
* Expected mean: ≈ 0.25
* Used for: Showing that Eve causes 25% errors on average in bits that Alice and Bob keep (i.e., same basis).

## Underlying Math:
When analyzing agreement or error rates (i.e., the fraction of bits out of a total of $N$), we normalize the standard deviation of the binomial distribution.

For a binomial variable with:
* Success probability $p$
* Number of trials $N$
* The standard deviation of the count is: $\sigma_{count} = \sqrt{p(1-p)N}$
But when we’re measuring the rate (e.g., error rate or agreement rate):
* We divide the count by $N$
So the standard deviation of the rate becomes:  $\sigma_{rate} = \sqrt{p(1-p)/N}$
