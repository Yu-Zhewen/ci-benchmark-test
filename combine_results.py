import json
import os
import subprocess

# Get the commit hash from the environment variable (the current commit triggering the workflow)
commit_hash = os.getenv("GITHUB_SHA")

# Load the current results (generated in the current commit)
with open("results.json", "r") as f:
    current_results = json.load(f)

# Fetch the previous results from the `gh-pages` branch
with open("results_history.json", "r") as f:
    results_history = json.load(f)

# Add the current commit results to the list
new_result = {
    "commit_hash": commit_hash,  # Add the current commit hash
    "tests": current_results["tests"]
}

# Append the new result to the end of the results list
results_history["results"].append(new_result)

# Limit the history to the most recent 100 results
max_commits = 100
results_history["results"] = results_history["results"][-max_commits:] if len(results_history["results"]) > max_commits else results_history["results"]

# Save the combined and truncated results to the results_history.json
with open("results_history.json", "w") as f:
    json.dump(results_history, f, indent=4)

print(f"Combined results saved with commit hash {commit_hash}. Kept only the most recent 100 commits.")

