from langchain_text_splitters import RecursiveCharacterTextSplitter

text = "Hello, how are you? I am fine, thank you."

splitter = RecursiveCharacterTextSplitter(chunk_size=20, chunk_overlap=10)

chunks = splitter.split_text(text)

print(chunks)
