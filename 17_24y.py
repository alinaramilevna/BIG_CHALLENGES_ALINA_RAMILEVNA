import os


def get_letter_count(text: str) -> int:
    cnt = 0

    for char in text:
        if char.isalpha():
            cnt += 1

    return cnt


files = os.listdir('elements')
total = 0

for file in files:
    with open(f'elements/{file}', 'r', encoding='utf8') as f:
        text = f.read()
        total += get_letter_count(text)

print(total)
