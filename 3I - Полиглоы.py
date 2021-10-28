n = int(input())
children = []
languages = set()
for _ in range(n):
    m = int(input())
    child = set()
    for _ in range(m):
        language = input()
        child.add(language)
        languages.add(language)
    children.append(child)

all_known_languages = None
for child in children:
    if all_known_languages is None:
        all_known_languages = child

    all_known_languages = set([language for language in all_known_languages
                              if language in child])

print(len(all_known_languages))
for language in all_known_languages:
    print(language)
print(len(languages))
for language in languages:
    print(language)
