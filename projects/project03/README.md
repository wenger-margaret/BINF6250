# Introduction
Identifying regulatory motifs — short, recurring sequence patterns such as transcription factor binding sites — is a 
central problem in computational biology. Because these motifs are typically short, degenerate, and scattered across 
many sequences without exact alignment, they cannot be found through simple string matching alone; the search space of 
possible motif positions and compositions grows too large for exhaustive search to be practical.

This project implements Gibbs sampling, a Markov Chain Monte Carlo (MCMC) approach to identifying sequence enrichment. 
Gibbs sampling uses a stochastic, optimization-based strategy: it starts from a random guess, iteratively scores 
candidate positions against a position weight matrix (PWM) representing the current best estimate of the motif, and 
resamples one sequence's position at a time — conditioned on the model built from all other sequences — to converge 
toward an optimal solution.

# Pseudocode
```
    
```

# Successes

# Struggles

# Personal Reflections

# Generative AI Appendix
