import os
print(*[file for file in os.listdir('E:\graduate\Korea_MIUD') if file.endswith('.inc')],sep='\n')
