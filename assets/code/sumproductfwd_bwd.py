import numpy as np


"""
Consider a small town where people are either:
- healthy
- have fever
Only the doctor can differentiate or identify the people having fever from healthy people. He does so by inquiring about their symptoms. People can have one of the following answers:
- normal
- dizzy
- cold
The doctor believes that the health condition of his patients operates as a discrete Markov chain.
The two states are:
- healthy
- fever
However, these states are ‘hidden’ from the doctor. The observations can be:
- normal
- dizzy
- cold
Thus, this forms a hidden Markov model which can be represented has:
"""
observations = ("normal", "cold", "dizzy")

observations_matrix = np.array([0, 1, 2])

states = ("Healthy", "Fever")

inital_probability = {"Healthy": 0.6, "Fever": 0.4}

inital_probability_matrix = np.array([0.6, 0.4])

transition__probability = {
    "Healthy": {"Healthy": 0.7, "Fever": 0.3},
    "Fever": {"Healthy": 0.4, "Fever": 0.6},
}

transition_probability_matrix = np.array(
    [
        [0.7, 0.3],
        [0.4, 0.6]
    ]
)

emission_probability = {
    "Healthy": {"normal": 0.5, "cold": 0.4, "dizzy": 0.1},
    "Fever": {"normal": 0.1, "cold": 0.3, "dizzy": 0.6},
}

emission_probability_matrix = np.array(
    [
        [0.5, 0.4, 0.1],
        [0.1, 0.3, 0.6]
    ]
)


def forward_backward_sumproduct(transition_matrix, emission_probability_matrix, initial_probability_matrix, observations):
    all_psi_f = np.zeros((observations.shape[0], transition_matrix.shape[-1]))
    # Forward pass:
    for observation in range(len(observations)):
        if observation > 0:
            psi = emission_probability_matrix[:,
                                              observations[observation]] * transition_matrix
            psi_f = psi_f @ psi
        else:
            psi_f = emission_probability_matrix[:,
                                                observations[observation]] * initial_probability_matrix
        all_psi_f[observation] = psi_f

    psi_b = np.ones(psi_f.shape)
    all_psi_b = all_psi_f.copy()
    all_psi_b[-1] = psi_b

    # Backward pass:
    for observation in reversed(range(len(observations)-1)):
        psi = emission_probability_matrix[:,
                                          observations[observation+1]] * transition_matrix
        psi_b = psi @ psi_b
        all_psi_b[observation] = psi_b
    return all_psi_f, all_psi_b


a, b = forward_backward_sumproduct(
    transition_probability_matrix, emission_probability_matrix, inital_probability_matrix, observations_matrix)
print(a)
print(b)
