epsilon_intro_ = """ 
When climbing to new positions `epsilon` determines how far the hill climbing based algorithm jumps 
from one position to the next points. A higher `epsilon` leads to longer jumps.

In a normal-`distribution` the `epsilon` parameter would correspond to the standard deviation.
"""

epsilon_d_ = {
    "epsilon": ["float", "0.03", "0.01 ... 0.3"],
}

distribution_intro_ = """ 
The mathematical `distribution` the algorithm draws samples from.

The distributions can be found in the [numpy documentation](https://numpy.org/doc/1.16/reference/routines.random.html)
"""
distribution_d_ = {
    "distribution": ["string", "normal", "normal, laplace, logistic, gumbel"],
}

n_neighbours_intro_ = """ 
The number of positions the algorithm explores from its current postion 
before jumping to the best one.
"""
n_neighbours_d_ = {
    "n_neighbours": ["int", "3", "1 ... 10"],
}

rand_rest_p_intro_ = """

"""

n_neighbours_intro_ = """

"""

n_neighbours_intro_ = """

"""

n_neighbours_intro_ = """

"""

n_neighbours_intro_ = """

"""

n_neighbours_intro_ = """

"""

n_neighbours_intro_ = """

"""

n_neighbours_intro_ = """

"""
