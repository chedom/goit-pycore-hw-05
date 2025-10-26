import sys
import log_processor

def main():
    if len(sys.argv) <= 1:
        print("Path to logs must be specified")
        return

    log_path = sys.argv[1]
    logs = []

    try:
        logs = log_processor.load_logs(log_path)
        log_processor.display_log_counts(log_processor.count_logs_by_level(logs))
    except FileNotFoundError:
        print(f"File {log_path} not found, check if the file exists and the path is correct")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    if len(sys.argv) <= 2:
        return # early return, no reason to display filtered logs

    log_level = sys.argv[2].strip().upper() # allows to accept `info`/`INFO`
    print('\n') # separate stats output from logs
    log_processor.display_log(log_processor.filter_logs_by_level(logs, log_level), log_level)


if __name__ == "__main__":
    main()