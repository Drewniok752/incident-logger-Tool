import pandas as pd
from datetime import datetime

# Define the file name for storing incidents
FILE_NAME = 'incidents.csv'

def log_incident(description, priority, status='Open'):
    """
    Logs an incident to the CSV file.

    :param description: Description of the incident
    :param priority: Priority of the incident (e.g., High, Medium, Low)
    :param status: Status of the incident (default is 'Open')
    """
    # Create a new DataFrame for the incident
    incident = pd.DataFrame([{
        'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Description': description,
        'Priority': priority,
        'Status': status
    }])

    try:
        # Check if the CSV file already exists
        if pd.io.common.file_exists(FILE_NAME):
            # Append the new incident to the existing CSV file
            incident.to_csv(FILE_NAME, mode='a', header=False, index=False)
        else:
            # Write the new incident to a new CSV file
            incident.to_csv(FILE_NAME, mode='w', header=True, index=False)
        print(f"Incident logged successfully: {description}")
    except Exception as e:
        print(f"Failed to log incident: {e}")

# Main function to execute the script
if __name__ == '__main__':
    # Get input from the user
    description = input("Enter the incident description: ")
    priority = input("Enter the incident priority (High/Medium/Low): ")
    
    # Log the incident
    log_incident(description, priority)

