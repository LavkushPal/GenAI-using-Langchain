from langchain_openai import ChatOpenAI
import dotenv

dotenv.load_dotenv()

model=ChatOpenAI(model='gpt-4',temperature=1.5,max_completion_totkens=10)
response=model.invoke('what is the capital of india?')

print(response.content)