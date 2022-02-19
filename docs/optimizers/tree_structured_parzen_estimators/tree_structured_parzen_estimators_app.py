import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
Tree of Parzen Estimators also chooses new positions by calculating the expected improvement. It does so by calculating the ratio of probability being among the best positions and the worst positions. Those probabilities are determined with a kernel density estimator, that is trained on alrady evaluated positions.
"""

para_d = {
    "Parameter": ["epsilon", "distribution", "n_neighbours"],
    "Type": ["float", "string", "int"],
    "default": ["0.03", "normal", "3"],
    "typical range / possible values": [
        "0.01 ... 0.3",
        "normal, laplace, logistic, gumbel",
        "1 ... 10",
    ],
}
para_df = pd.DataFrame(para_d)


properties_ = """
- If model evaluations take a long time
- If you do not want to do many iterations
- If your search space is not to big
"""


implementation_ = """
The hill climbing algorithm is saving the current position in the search space and finds a new position by selecting a random position around it. This is done with a gaussian distribution. So if the position is further away the probability of getting selected is lower, but never zero. This makes the hill climbing more heuristic and a bit more adaptable. The standard deviation of the gaussian distribution in each dimension is dependend on the size of the search space in the corresponding dimension. This improves the exploration performance if the sizes of the search space dimensions are differing from each other.
"""


def tree_structured_parzen_estimators_app():
    st.title("Tree Structured Parzen Estimators")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/tree_structured_parzen_estimators_0.gif"))
    col3.image(os.path.join(here_, "_images/tree_structured_parzen_estimators_1.gif"))
    col2.image(os.path.join(here_, "_images/tree_structured_parzen_estimators_2.gif"))
    col3.image(os.path.join(here_, "_images/tree_structured_parzen_estimators_3.gif"))

    col1.subheader("About the implementation")
    col1.markdown(implementation_)

    col1.subheader("Available parameters")
    col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
