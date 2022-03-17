# First way
"""
def EditFile(file_name):
    reader = open('file_name')
    try:
        # further file processing goes there
    finally:
        reader.close()
"""
# Second way(The preferred one)
"""
def EditFile2(file_name):
    with open('file_name') as reader:
        # further file processing goes there
"""