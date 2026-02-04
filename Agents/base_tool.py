from langchain.tools import tool,BaseTool
from pydantic import BaseModel,Field
from typing import Type


class multi_schema(BaseModel):
    a:int =Field(description=" first input of multiply tool",required=True)
    b:int =Field(description=" second input of multiply tool",required=True)

class add_schema(BaseModel):
    a:int =Field(description=" first input of add tool",required=True)
    b:int =Field(description=" second input of add tool",required=True)


class MultiplyTool(BaseTool):

    name:str = "multiply numbers"
    description:str ="multiply 2 integer numbers"

    arg_schema : Type[BaseModel]=multi_schema

    def _run(self,a:int,b:int)->int:
        return a*b
    

class AddTool(BaseTool):

    name:str = "add numbers"
    description:str ="add 2 integer numbers"

    arg_schema : Type[BaseModel]=multi_schema

    def _run(self,a:int,b:int)->int:
        return a+b
    

ctool=MultiplyTool()
catool=AddTool()

print(ctool.name)
print(ctool.description)
print(ctool.args)

print(ctool.invoke({'a':3, 'b':3}))
