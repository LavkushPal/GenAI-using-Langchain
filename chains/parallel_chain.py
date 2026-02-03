
import hf_local as hf
import dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

dotenv.load_dotenv()

model = hf.get_hf_local_model()
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Give me about {topic} in 2-5 paragraphs.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Create short notes on the given text:\n{text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Generate 5-10 quiz questions on the given text:\n{text}",
    input_variables=["text"]
)

prompt4 = PromptTemplate(
    template="Merge the given Notes:\n{notes}\n\nand Quizzes:\n{quiz}",
    input_variables=["notes", "quiz"]
)

# topic -> text
chain_topic = prompt1 | model | parser

# create dict {"topic":..., "text":...}
base = RunnablePassthrough.assign(text=chain_topic)

# now parallel gets the dict and uses {text}
parallel_chain = RunnableParallel({
    "notes": prompt2 | model | parser,
    "quiz":  prompt3 | model | parser
})

chain_last = prompt4 | model | parser

final_chain = base | parallel_chain | chain_last

result = final_chain.invoke({"topic": "machine learning, deep learning and gen ai"})
print(result)
