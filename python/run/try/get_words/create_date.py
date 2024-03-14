import datetime
import os

current_folder = os.getcwd()
# Start date
start_date = datetime.date(2018, 1, 1)

# End date (today's date)
end_date = datetime.date.today()

# Open file to write dates
with open(current_folder+'/lists/raw/date.txt', 'w') as f:
    # Current date starts from start date
    current_date = start_date
    while current_date <= end_date:
        # Write date to file in DDMMYYYY format
        f.write(current_date.strftime('%d%m%Y') + '\n')
        # Increment current date
        current_date += datetime.timedelta(days=1)