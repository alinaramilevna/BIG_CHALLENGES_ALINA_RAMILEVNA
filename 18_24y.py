import os


def get_new_s(text: str) -> str:
    return text.replace(',', '').replace(')', '').replace('(', '').lower()


files = os.listdir('elements')
d = {}

for file in files:

    with open(f'elements/{file}', 'r', encoding='utf8') as f:
        text = f.read()

    s = get_new_s(text)
    words = s.split()

    for word in words:
        d[word] = d.get(word, 0) + 1

# print(max(d, key=lambda x: d[x]))
print(sorted(d, key=lambda x: d[x], reverse=True))
