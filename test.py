# generate_results.py
import json

# Example test results (without commit hash)
test_results = {
    "tests": [
        {"test_name": "Test 1", "status": "passed", "duration": 1.2},
        {"test_name": "Test 2", "status": "failed", "duration": 2.4},
        {"test_name": "Test 3", "status": "passed", "duration": 0.8},
    ]
}

# Write the test results to results.json
with open("results.json", "w") as outfile:
    json.dump(test_results, outfile, indent=4)

print("Test results saved in results.json")