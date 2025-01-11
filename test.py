import random
import json

# Example test results (without commit hash)
test_results = {
    "tests": [
        {"test_name": "Test 1", "status": "passed", "duration": random.uniform(1, 10)},
        {"test_name": "Test 2", "status": "passed", "duration": random.uniform(1, 10)},
        {"test_name": "Test 3", "status": "passed", "duration": random.uniform(1, 10)},
    ]
}

# Write the test results to results.json
with open("results.json", "w") as outfile:
    json.dump(test_results, outfile, indent=4)

print("Test results saved in results.json")