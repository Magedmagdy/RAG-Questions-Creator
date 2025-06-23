import os
from pathlib import Path



list_of_files = [
     "src/__init__.py",
     "src/helper.py",
     "NoteBooks/notebook.ipynb",
     "Images",
     "DataSets",
     ".env",
     ".env.example",
     "frontend.py",
     "backend.py"
]


for filepath in list_of_files:
     filepath = Path(filepath)
     filedir, filename = os.path.split(filepath)
     if filedir != "":
          os.makedirs(name=filedir, exist_ok=True)
          
     if (not os.path.exists(filepath)):
          if filename in  ["Images", "DataSets"]:
               os.makedirs(name=filename, exist_ok=True)
          else:
               with open(file=filepath, mode="w") as f:
                    pass
     else:
          print(f"{filepath} is already exists")
               