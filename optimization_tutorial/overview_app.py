import os
import streamlit as st


here_ = os.path.dirname(os.path.realpath(__file__))


about_ = """
This tutorial describes the optimization strategies 
and parameters from the [Hyperactive](https://github.com/SimonBlanke/Hyperactive) and 
[Gradient-Free-Optimizers](https://github.com/SimonBlanke/Gradient-Free-Optimizers) 
python-packages.
All optimizer- and parameter-names correspond 
to version 1.0 of Gradient-Free-Optimizers. 

The default-paramters 
and algorithm behaviour may change across 
[minor versions](https://semver.org/) of Gradient-Free-Optimizers.
Select the minor/major version of Gradient-Free-Optimizers in the 
selectbox and the documentation will change 
accordingly.
"""

introduction_ = """
...
"""



def overview_app():
    st.title("Overview")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )

    st.header("About this tutorial")
    col1, col2, col3 = st.columns((2, 1, 1))
    col1.write(about_)

    # col2.image(os.path.join(here_, "_images", "optimizer_table.png"))
    # col3.image(os.path.join(here_, "_images", "optimizer_table.png"))

    st.header("Introduction")
    col1, col2 = st.columns((1, 1))

    col1.write(introduction_)
    col2.image(os.path.join(here_, "_images", "optimizer_table.png"))
