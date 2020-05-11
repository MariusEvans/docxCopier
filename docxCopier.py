import docx
import pyperclip
import sys

print("\ndocxCopier by Marius Evans")
print("--------------------------")

if len(sys.argv) < 2:
    print("Usage: python docxCopier.py \"PATH_TO_MY_FILE.docx\"")
    sys.exit()

filename = sys.argv[1]

doc = docx.Document(filename)

fullText = []
for para in doc.paragraphs:
    fullText.append(para.text)
pyperclip.copy('\n'.join(fullText))
print("All text has been copied.\n")