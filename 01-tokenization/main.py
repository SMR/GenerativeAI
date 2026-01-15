import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")
text = "Hello, I am Samarjeet!"
tokens = enc.encode(text)
print(tokens)
tokens =[9906, 11, 358, 1097, 86356, 3841, 295, 0]
decoded = enc.decode(tokens)
print(decoded)

