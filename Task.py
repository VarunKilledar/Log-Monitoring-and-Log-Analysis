import time
import re
import sys
import signal

#Function to  read and Monitor the new log in log files
def Monitor_log(log_file,keywords):
    try:
        print("Monitering Log file:",log_file)
        with open(log_file,'r') as file:
            file(0,2) #Moving file pointer towards end
            while True:
                new_line = file.readline()
                if new_line:
                    print(new_line.strip())
                    Analyze_Log(new_line,keywords)# Calling the function to Analyze the Error
                time.sleep(0.1) # Adjust the time as per need 
    except KeyboardInterrupt:
        print("\nMonitering Stopped by the user.")
        sys.exit()
    except Exception as e:
        print("Error Occurred:",e)
#Function for Analyze the log for searcing for error
def Analyze_Log(log_entry,keywords):
    keywords_Occurance = 0
    for keywords,pattern in keywords.items():
        if re.search(pattern, log_entry,re.IGNORECASE): #Serardching for the spesific keywords in the log file
            print("KeyWords '{}' matched  in log Entry: '{}'".format(keywords,log_entry.strip()))
            keywords_Occurance +=1
    print("Keywords Count:",keywords_Occurance)

if __name__ == "__main__":
    log_file = "/var/log/testLog.log"  # Change this to your log file path
    keywords = {
        "Error": r"error",
        "HTTP Status Code 404": r"HTTP/1\.1\" 404",
        # Add more keywords and patterns as needed
    }

    def signal_handler(signal, frame):
        print("\nReceived SIGINT, stopping monitoring.")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    Monitor_log(log_file, keywords)

