import numpy as np
import pandas as pd
from scipy.stats import norm

from gradient_free_optimizers import BayesianOptimizer


def objective_function(para):
    score = -(para["x"] * para["x"])
    return score


search_space = {
    "x": np.arange(-10, 11, 1),
}


def normalize(array):
    num = array - array.min()
    den = array.max() - array.min()

    if den == 0:
        return np.random.random_sample(array.shape)
    else:
        return ((num / den) + 0) / 1


class BayesianOptimizer_plot(BayesianOptimizer):
    def __init__(self, *args, **kwargs):
        super().__init__(search_space)

        self.mu_data = []
        self.sigma_data = []
        self.best_approx_pos_data = []

    def _expected_improvement(self):
        mu, sigma = self.regr.predict(self.all_pos_comb, return_std=True)
        # mu_sample = self.regr.predict(self.X_sample)
        mu = mu.reshape(-1, 1)
        sigma = sigma.reshape(-1, 1)

        self.mu_data.append(mu)
        self.sigma_data.append(sigma)

        Y_sample = normalize(np.array(self.Y_sample)).reshape(-1, 1)
        imp = mu - np.max(Y_sample) - self.xi
        Z = np.divide(imp, sigma, out=np.zeros_like(sigma), where=sigma != 0)

        exploit = imp * norm.cdf(Z)
        explore = sigma * norm.pdf(Z)

        exp_imp = exploit + explore
        exp_imp[sigma == 0.0] = 0.0

        return exp_imp[:, 0]

    def _propose_location(self):
        X_sample = np.array(self.X_sample)
        Y_sample = np.array(self.Y_sample)

        Y_sample = normalize(Y_sample).reshape(-1, 1)
        self.regr.fit(X_sample, Y_sample)

        exp_imp = self._expected_improvement()

        index_best = list(exp_imp.argsort()[::-1])
        all_pos_comb_sorted = self.all_pos_comb[index_best]
        pos_best = all_pos_comb_sorted[0]

        self.best_approx_pos_data.append(pos_best)

        return pos_best


opt = BayesianOptimizer_plot(search_space, rand_rest_p=0)
opt.search(
    objective_function,
    n_iter=10,
    initialize={"random": 1},
    random_state=0,
    # verbosity=False,
    memory=False,
)

opt.mu_data
opt.sigma_data
opt.best_approx_pos_data
