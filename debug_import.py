import sys
import os

def print_project_structure(startpath):
    print("Project Structure:")
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

def check_imports():
    print("\nPython Path:")
    for path in sys.path:
        print(path)

    print("\nTrying to import backend modules:")
    try:
        from backend.wellness_suggestion import WellnessSuggestions
        print("Successfully imported WellnessSuggestions")
    except Exception as e:
        print(f"Import Error: {e}")

    print("\nCurrent Working Directory:", os.getcwd())

if __name__ == "__main__":
    print_project_structure('.')
    check_imports()