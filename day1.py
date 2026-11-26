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