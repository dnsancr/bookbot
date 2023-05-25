path_to_file = 'books/frankenstein.txt'

with open(path_to_file) as f:
    file_content = f.read()

lowered_file_content = file_content.lower()
words = file_content.split()
characters = {}
characters_found = []

for character in lowered_file_content:
    if character.isalpha():
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
            characters_found.append(character)

print(f"--- Begin report of {path_to_file} ---")
print(f"\n{len(words)} words found in the document\n")

characters_found.sort()
for character in characters_found:
    print(f"The '{character}' character was found {characters[character]} times")

print("\n--- End report ---")
