from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

clent = OpenAI()

text = "The quick brown fox jumps over the lazy dog"

response = clent.embeddings.create(
    model="text-embedding-3-small",
    input=text
)
print(response.data[0].embedding)