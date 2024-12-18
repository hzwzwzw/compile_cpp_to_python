import os
import subprocess

# List of test C++ files
test_files = [
    "example/test0.cpp",
    "example/test1.cpp",
    "example/test2.cpp",
    "example/test3.cpp",
    "example/test4.cpp"
]

def run_translator(test_file):
    # Run the translator and capture the output
    result = subprocess.run(
        ["python3", "-m", "translator.translator", test_file],
        capture_output=True,
        text=True
    )
    
    # Print the output and error (if any)
    print(f"Running translator on {test_file}...")
    print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")

def main():
    for test_file in test_files:
        if os.path.exists(test_file):
            run_translator(test_file)
        else:
            print(f"Test file {test_file} does not exist.")

if __name__ == "__main__":
    main()