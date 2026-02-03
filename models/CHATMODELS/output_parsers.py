import hf_local as hf
from typing import TypedDict,Annotated,Optional,Literal
import dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

dotenv.load_dotenv()

model=hf.get_hf_local_model()

parser= JsonOutputParser()

template=PromptTemplate(
    template='give me a list of top 5 cities in india with their state name,population, known places \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt=template.format()
res=model.invoke(prompt)
final_res=parser.parse(res.content)

print(final_res)
