# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew text2.")

# Relative file paths
with open("../my_file.txt") as file:
    contents = file.read()
    print(contents)