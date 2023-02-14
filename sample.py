text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker."

with open("lorem_ipsum.txt", "w") as file:
    file.write(text)

with open("lorem_ipsum.txt", "r") as file:
    text = file.read()

reversed_text = text[::-1]

with open("reversed_lorem_ipsum.txt", "w") as file:
    file.write(reversed_text)
