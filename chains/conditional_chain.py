import hf_local as hf
import dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableBranch,RunnableLambda
from pydantic import Field,BaseModel
from typing import Literal

dotenv.load_dotenv()

model = hf.get_hf_local_model()
parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] =Field(description=" classify the sentiment feedback")

pd_parser=PydanticOutputParser(pydantic_object=Feedback)


prompt1= PromptTemplate(
    template="classify the given reiview into positive or negative sentiment. \n Reivew: {feedback} \n ",
    input_variables=["feedback"],
    # partial_variables={"format_instruction": pd_parser.get_format_instructions()}
)

prompt2= PromptTemplate(
    template='Write an appropriate response to this positive feedback in a word or string  \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)


chain1= prompt1 | model | parser

# branch_chain=RunnableBranch(
#     (lambda x: x.sentiment=="positive", prompt2| model | parser),
#     (lambda x: x.sentiment=="negative", prompt3| model | parser),
#     RunnableLambda(lambda x:"could not find appropriate result")
# )

branch_chain=RunnableBranch(
    (lambda x: x=="positive", prompt2| model | parser),
    (lambda x: x=="negative", prompt3| model | parser),
    RunnableLambda(lambda x:"could not find appropriate result")
)

final_chain= chain1 | branch_chain

result= final_chain.invoke({'feedback': 'I recently bought this phone and it is a beautiful'})

print(result)

print()

# final_chain.get_graph().print_ascii()



