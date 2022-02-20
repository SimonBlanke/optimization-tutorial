import os
import streamlit as st


def overview_app(argument_d):
    title = argument_d["title"]
    _name_ = argument_d["_name_"]
    explanation_ = argument_d["explanation_"]
    here_ = argument_d["here_"]
    implementation_ = argument_d["implementation_"]
    good_ = argument_d["good_"]
    bad_ = argument_d["bad_"]
    info_ = argument_d["info_"]
    para_df = argument_d["para_df"]

    st.title(title)
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.header("Introduction")
    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/" + _name_ + "_0.gif"))
    col3.image(os.path.join(here_, "_images/" + _name_ + "_1.gif"))
    col2.image(os.path.join(here_, "_images/" + _name_ + "_2.gif"))
    col3.image(os.path.join(here_, "_images/" + _name_ + "_3.gif"))
    col2.image(os.path.join(here_, "_images/" + _name_ + "_4.gif"))
    col3.image(os.path.join(here_, "_images/" + _name_ + "_5.gif"))

    col1.header("About the implementation")
    col1.markdown(implementation_)

    col1.header("Characteristics")
    col1.success(good_)
    col1.error(bad_)
    col1.info(info_)

    col1.header("Parameters")
    col1.table(para_df)


def parameter_app(argument_d):
    title = argument_d["title"]
    _name_ = argument_d["_name_"]
    explanation_ = argument_d["explanation_"]
    here_ = argument_d["here_"]

    st.title(title)
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3, col4 = st.columns((1, 1, 1, 1))

    col1.write("")
    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images", _name_ + "_0.gif"))
    col3.image(os.path.join(here_, "_images", _name_ + "_1.gif"))
    col4.image(os.path.join(here_, "_images", _name_ + "_2.gif"))
    col2.image(os.path.join(here_, "_images", _name_ + "_3.gif"))
    col3.image(os.path.join(here_, "_images", _name_ + "_4.gif"))
    col4.image(os.path.join(here_, "_images", _name_ + "_5.gif"))
