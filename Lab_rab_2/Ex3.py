import os

for root, dirl, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.py'):
            print(os.path.join(root, file))