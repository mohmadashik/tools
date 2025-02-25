def pace_to_kph(pace):
    """
    Convert pace in mm:ss per kilometer to kilometers per hour (kph).

    Parameters:
        pace (str): The pace in the format "mm:ss per kilometer".

    Returns:
        float: Speed in kilometers per hour (kph).
    """
    try:
        # Split the input into minutes and seconds
        minutes, seconds = map(int, pace.split(':'))

        # Convert the total time per kilometer into hours
        total_hours_per_km = (minutes * 60 + seconds) / 3600

        # Calculate speed in kph
        kph = 1 / total_hours_per_km

        return round(kph, 2)
    except (ValueError, ZeroDivisionError):
        return "Invalid input. Please provide pace in the format 'mm:ss'."

# Input pace from the user
pace_input = input("Enter your average pace (mm:ss per kilometer): ")

# Convert pace to kph
speed_kph = pace_to_kph(pace_input)

print(f"Your speed is: {speed_kph} kph")
