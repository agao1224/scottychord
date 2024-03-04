import subprocess
import time
import signal

if __name__ == "__main__":
    # Start the process

    while True:
        try:
            subprocess.check_output(
                "python3 piano.py",
                stderr=subprocess.STDOUT,
                shell=True
            )
        except Exception as e:
            print()

    # Kill the process
    # p.send_signal(signal.SIGINT)  # Sends an interrupt signal, same as Ctrl+C

    # If the process does not terminate within the given sleep time, you can use p.terminate() or p.kill()
    # p.terminate()  # Politely ask the process to terminate
    # p.kill()  # Forcefully kill the process (if it doesn't terminate with terminate())