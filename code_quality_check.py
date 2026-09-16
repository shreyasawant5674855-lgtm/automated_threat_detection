import ast
import os

files_to_check = [
    "backend.py",
    "threat_detector.py",
    "save_model.py",
    "automated_detection.py",
    "database.py"
]

print("Code Quality Check Started")
print("--------------------------")

all_passed = True

for filename in files_to_check:

    if not os.path.exists(filename):
        print(filename, "-> File not found")
        all_passed = False
        continue

    try:
        with open(filename, "r", encoding="utf-8") as file:
            code = file.read()

        ast.parse(code)

        print(filename, "-> Syntax OK")

    except SyntaxError as error:
        print(filename, "-> Syntax Error")
        print("Error:", error)
        all_passed = False

if all_passed:
    print("\nCode quality check completed successfully!")
else:
    print("\nCode quality check found issues.")