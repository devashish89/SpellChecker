import streamlit as st
from gingerit.gingerit import GingerIt

st.title("Devashish's Grammarly!")
incorrect_sent = st.text_area("Enter the sentence to be corrected")
if st.button("Correct!"):
    if incorrect_sent=="":
        st.warning("Please Enter the text!")
    else:
        parser = GingerIt()
        output = parser.parse(incorrect_sent)
        print(output['result'])
        st.text_area("Corrected Sentence:", value=output['result'])
        #Issue in selectbox
        user_rating = st.sidebar.selectbox("Rate the corrected sentence output with 1 being worst and 5 being best", [None,1,2,3,4,5])
        if user_rating==None:
            pass
        else:
            print("User Rating: ", user_rating)
else: pass


