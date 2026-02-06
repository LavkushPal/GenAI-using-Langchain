from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


base=HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=1000,
        skip_special_tokens=True,
        return_full_text=False
    )
)



model=ChatHuggingFace(llm=base)

def get_hf_local_model():
    return model

# res=model.invoke("list down the all top iits in india")
# print(res.content)