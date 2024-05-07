# gunicorn.conf.py

bind = "0.0.0.0:8000"  # Change the port if necessary
workers = 3  # Adjust the number of workers based on your system resources
timeout = 120  # Set the timeout to a value suitable for your application