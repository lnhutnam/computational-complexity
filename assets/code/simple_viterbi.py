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


def viterbi_classical(transition_matrix, emission_probability_matrix, initial_probability_matrix, observations):
    """
    Input:
    initial_probability_matrix: An array consisting of initial probabilities: $\pi = \{\pi_1, \pi_2, ..., \pi_k\}$ where $\pi_i$ stores the probability $x_1 = s_i$
    transition_matrix: Transition matrix $A$ of size $K \times K$ where $A_{i,j}$ stores the transition probability of transiting from state $S_i$ to state $S_j$
    emission_probability_matrix: Emission matrix $B$ of size $K \times N$ where $B_{i, j}$ stores the probability of observing $O_j$ from state $S_i$
    observations is sequence of observations: $Y = \{y_1, y_2, ..., y_T\}$
    Output: The most likely hidden state sequence $X = \{x_1, x_2, ..., x_j\}$
    - MAP path
    - maximum probability
    - probabilities of most probable paths
    - most probable path sequence
    """
    probabilities_of_most_probable_paths = np.zeros(
        (observations.shape[0], initial_probability_matrix.shape[-1], ))
    most_probable_path_sequence = np.zeros(
        (observations.shape[0], initial_probability_matrix.shape[-1], ))
    probable_path_probabilities = emission_probability_matrix[:, int(
        observations[0])] * initial_probability_matrix
    """
    V_1(x_1) = \psi(x_1)
    """
    probabilities_of_most_probable_paths[0] = probable_path_probabilities
    probable_path_sequence = [0] * initial_probability_matrix.shape[0]
    most_probable_path_sequence[0] = probable_path_sequence
    # Forward pass
    # for k <- 2 to T do
    for observation in range(1, len(observations)):  # Sequentially
        # V_k(x_k) = max_{x_{k-1}}[\psi_k(x_{k-1}, x_k}V_{k-1}(x_{k-1})]
        psi = emission_probability_matrix[:, int(
            observations[observation])] * transition_matrix
        old_probable_path_probabilities = probable_path_probabilities
        probable_path_probabilities = np.zeros(
            probable_path_probabilities.shape)
        probable_path_sequence = [0] * probable_path_probabilities.shape[0]
        # u_{k-1}(x_k) = argmax_{x_{k-1}}[\psi_k(x_{k-1}, x_k}V_{k-1}(x_{k-1})]
        for _psi in range(psi.shape[0]):
            probable_path_sequence[_psi] = np.argmax(
                (psi[:, _psi] * old_probable_path_probabilities))
            probable_path_probabilities[_psi] = (
                psi[:, _psi] * old_probable_path_probabilities)[probable_path_sequence[_psi]]
        probabilities_of_most_probable_paths[observation] = probable_path_probabilities
        most_probable_path_sequence[observation] = probable_path_sequence
    # Backward pass:
    # x^{*}_T = argmax_{x_T}V_T(x_T)
    map_path = [0] * len(observations)
    map_path[-1] = np.argmax(probabilities_of_most_probable_paths[-1])
    maximum_probability = probabilities_of_most_probable_paths[-1][map_path[-1]]
    # for k <- T to 2 do:
    for observation in reversed(range(len(observations)-1)):  # Sequentially
        # x^{*}_{k-1} = u_{k-1}(x^{*}_k)
        map_path[observation] = int(
            most_probable_path_sequence[observation+1][map_path[observation+1]])
    # print results
    print(map_path)
    print(maximum_probability)
    print(probabilities_of_most_probable_paths)
    print(most_probable_path_sequence)
    return map_path, maximum_probability, probabilities_of_most_probable_paths, most_probable_path_sequence


viterbi_classical(transition_probability_matrix, emission_probability_matrix,
                  inital_probability_matrix, observations_matrix)

"""
MAP path
[0, 0, 1]
maximum probability
0.015119999999999998
probabilities of most probable paths
[[0.3     0.04   ]
 [0.084   0.027  ]
 [0.00588 0.01512]]
most probable path sequence
[[0. 0.]
 [0. 0.]
 [0. 0.]]
([0, 0, 1],
"""
