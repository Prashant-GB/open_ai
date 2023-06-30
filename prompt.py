# Import PromptTemplat from langchain
from langchain import PromptTemplate

# Import OpenAI from llms
from langchain.llms import OpenAI

# Import LLMChain from chains
from langchain.chains import LLMChain

# Demo template for testing the template generation
demo_template = """
I need you to serve as a legal advisor for the launch of a new startup in Bengaluru.
In an accessible manner for {law_concept}.
"""

# Declare the Prompt Template with input paramaters and prompt object is representing LLMChain
prompt=PromptTemplate(
    input_variables=['law_concept'],
    template=demo_template
)
prompt.format(law_concept='local laws')


# In OpenAI with tempature represents  governs the randomness and thus the creativity of the responses.
llm = OpenAI(temperature=0.7, openai_api_key="YOUR_API_KEY")

# Declare the LLMChain 
chain= LLMChain(llm=llm,prompt=prompt)

# Generate the responce from the prompt.
chain.run('Local Law')

