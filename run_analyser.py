import csv

def count_runs(file_path):
    # Initialize counters for each distance
    run_counts = {
        "1k": 0,
        "2k": 0,
        "5k": 0,
        "7k": 0,
        "10k": 0
    }

    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if present
            
            for row in reader:
                if len(row) < 2:
                    continue  # Skip rows with insufficient data
                try:
                    meters = float(row[1])
                    
                    # Ignore invalid or "no workout" entries
                    if meters <= 0:
                        continue
                    
                    # Determine the nearest kilometer
                    nearest_k = round(meters / 1000)
                    
                    # Update the corresponding run count if it's a key
                    key = f"{nearest_k}k"
                    if key in run_counts:
                        run_counts[key] += 1
                        if key =='7k' :
                            print(f'{key} on {row[0]}')
                        if key =='5k' :
                            print(f'5k on {row[0]}')
                        if key =='10k' :
                            print(f'10k on {row[0]}')
                
                except ValueError:
                    continue  # Skip rows with invalid numbers
        
        return run_counts

    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

# Use your file path
file_path = "/home/amohmad/Documents/ashik/workout/Nov_2024_running.csv"

result = count_runs(file_path)
if result:
    print("Run counts:")
    for run_type, count in result.items():
        print(f"{run_type}: {count}")
