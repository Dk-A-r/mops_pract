import streamlit as st
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

st.write('This chatbot is based on HuggingFace Hub.\
Please, enter your huggingface token.')

x = 0

HUG_TOKEN = st.text_input("Token: ", key=x, type='password',
                          placeholder='Please, enter your huggingface token')

TEMPLATE = """Question: {question}
Answer: Let's think step by step."""
PROMPT = PromptTemplate(template=TEMPLATE, input_variables=["question"])

if HUG_TOKEN:
    llm_chain = LLMChain(prompt=PROMPT,
                         llm=HuggingFaceHub(huggingfacehub_api_token=HUG_TOKEN,
                                            repo_id="google/flan-t5-xxl",
                                            model_kwargs={"temperature": 0.9,
                                                          "max_length": 512}))

    st.write(
        'Now we will start the conversation.\
         If you become bored, you can type "quit"\
          in your prompt to exit. Good luck!')

    x = x + 1

    question = st.text_input("User: ", key=x)

    while question:
        x = x + 1

        if question == 'quit':
            st.write("Goodbye!")
            break
        response = llm_chain.run(question)
        st.write(f"Answer is: {response}")
        st.write("What is your next question?")
        question = st.text_input("User: ", key=x)
