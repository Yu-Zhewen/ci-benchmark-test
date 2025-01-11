import json

# Load the combined results history
with open("results_history.json", "r") as f:
    results_history = json.load(f)

# Collect data for graphs
graph_data = {}
for entry in results_history["results"]:
    commit_hash = entry["commit_hash"]
    truncated_commit_hash = str(commit_hash)[:7]  # Truncate commit hash to first 7 characters
    for test in entry["tests"]:
        test_name = test["test_name"]
        status = test["status"]
        duration = test["duration"]

        if test_name not in graph_data:
            graph_data[test_name] = {"commit_hashes": [], "durations": [], "statuses": []}

        graph_data[test_name]["commit_hashes"].append(truncated_commit_hash)  # Use truncated commit hash
        graph_data[test_name]["durations"].append(duration)
        graph_data[test_name]["statuses"].append(status)

# Start building the HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Test Results Visualization</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
        .chart-container { width: 80%; margin: 30px auto; }
        canvas { width: 100%; height: auto; }
    </style>
</head>
<body>
    <h1>Test Results Visualization</h1>
    <p>Overview of test results for the most recent commits:</p>
"""

# Add a graph for each test
for test_name, data in graph_data.items():
    html_content += f"""
    <div class="chart-container">
        <h2>Performance for {test_name}</h2>
        <canvas id="chart-{test_name.replace(' ', '-')}"></canvas>
    </div>
    <script>
        const ctx_{test_name.replace(' ', '_')} = document.getElementById('chart-{test_name.replace(' ', '-')}')
        const chart_{test_name.replace(' ', '_')} = new Chart(ctx_{test_name.replace(' ', '_')}, {{
            type: 'line',
            data: {{
                labels: {data["commit_hashes"]},  // Truncated commit hashes as X-axis labels
                datasets: [{{
                    label: 'Duration (s)',
                    data: {data["durations"]},   // Test durations as Y-axis
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderWidth: 2
                }}]
            }},
            options: {{
                responsive: true,
                scales: {{
                    x: {{
                        title: {{
                            display: true,
                            text: 'Commit Hash'
                        }}
                    }},
                    y: {{
                        title: {{
                            display: true,
                            text: 'Duration (s)'
                        }}
                    }}
                }}
            }}
        }});
    </script>
    """

# Close the HTML content
html_content += """
</body>
</html>
"""

# Save the HTML file
with open("results_history.html", "w") as f:
    f.write(html_content)

print("Visualization with graphs generated and saved to results_history.html.")
