from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import hf_local as hf

model=hf.get_hf_local_model()

chat_history=[SystemMessage(content="hii, LLM")]

while True:
    user_input=input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit" :
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)


# print(chat_history)