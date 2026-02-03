from langchain_google_genai import ChatGoogleGenerativeAI
import dotenv

dotenv.load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')

resp=model.invoke('what is the cpaital of india')

print(resp.content)