from langchain_community.document_loaders import PyPDFLoader


loader= PyPDFLoader('L5.pdf')

docs = loader.load()

print(docs[0].page_content)