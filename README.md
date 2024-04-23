# Log Monitoring and Analysis Script
This script is designed to monitor a specified log file for new entries and analyze them for specific keywords or patterns. It continuously reads new lines from the log file, searches for predefined keywords, and prints matching entries along with their occurrence count.

## Functionality:
- Monitors a specified log file for new entries in real-time.
- Analyzes log entries for specific keywords or patterns.
- Prints matching log entries and their occurrence count.

## Requirements:
- Python 3.x installed on your system.
- No additional Python libraries required.

## Usage:
1. Save the provided script (log_monitor.py) to your desired location.
2. Modify the log_file variable to specify the path of the log file you want to monitor.
3. Define keywords and corresponding regular expression patterns in the keywords dictionary as needed.
4. Open a terminal or command prompt.
5. Navigate to the directory where the script is saved.
6. Run the script using the following command:
    ```
    python log_monitor.py
    ```

## Additional Notes:
- Adjust the time.sleep() value in the Monitor_log() function to control the frequency of log file checks.
- Customize the keywords dictionary to include keywords and patterns relevant to your log analysis requirements.
- The script handles KeyboardInterrupt (Ctrl+C) to gracefully stop monitoring.

### Feedback:
For any issues, suggestions, or feedback, please feel free to contact the script author.