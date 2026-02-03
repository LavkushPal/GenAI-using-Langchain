from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import dotenv 

dotenv.load_dotenv()

base=HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model=ChatHuggingFace(llm=base)

res=model.invoke("what is the capital city of india")

print(res.content)