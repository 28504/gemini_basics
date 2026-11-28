messages = [
    {"role" : "python", "content" : "hii"},
    {"role" : "user" , "content" : "Learning rag"}
]

messages.append({"role" : "assistant", "content" : "New"})

for m in messages:
    print(m["role"] + ":" + m["content"])


def word_count(text):
    return len(text.split())

print(word_count("retrieval augmented generation"))

text = "abcdefgh"
print(text[0:3])
print(text[3:6])
print(text[6:9])

for i in range(0, len(text), 3):
    print(i)

def chunk_size(text, size):
    chunks = []
    for i in range(0, len(text), size):
        piece = text[i:i+size]
        chunks.append(piece)
    return chunks 

print(chunk_size("abcdefgh", 3))
print(chunk_size("abcdefgh",5))

