from datetime import datetime

now = datetime.now()

formatted_date_time = now.strftime("%A, %d of %B on %H:%M:%S %p")

print(formatted_date_time)