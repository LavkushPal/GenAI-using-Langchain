from langchain_community.document_loaders import WebBaseLoader

url='https://colab.research.google.com/drive/1gv3e-OfHCi6IuVBVR7xWmrcVl6gHsydv?usp=sharing'
loader= WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)