# 07_python_advanced/standard_library_datetime.py

import datetime

# Current date and time
now = datetime.datetime.now()
print("Now:", now)                  # 2025-06-08 15:30:00.123456

# Today's date
today = datetime.date.today()
print("Today:", today)              # 2025-06-08

# Create date, time, and datetime objects
d = datetime.date(2025, 1, 1)
t = datetime.time(12, 30, 15)
dt = datetime.datetime(2025, 1, 1, 12, 30, 15)

# Access fields
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

# Timedelta: duration or difference
delta = datetime.timedelta(days=3, hours=5)
print("Delta:", delta)

future = dt + delta
past = dt - delta
print("Future:", future)
print("Past:", past)

# Datetime difference
d1 = datetime.datetime(2025, 6, 1)
d2 = datetime.datetime(2025, 6, 8)

diff = d2 - d1
print("Diff days:", diff.days)
print("Diff total seconds:", diff.total_seconds())

# Parsing strings to datetime
s = "2025-06-08 14:45"
parsed = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M")
print("Parsed:", parsed)

# Formatting datetime to string
formatted = parsed.strftime("%d/%m/%Y %I:%M %p")
print("Formatted:", formatted)  # 08/06/2025 02:45 PM

# Replace components
changed = dt.replace(year=2030, hour=8)
print("Modified datetime:", changed)

# Comparisons
if d1 < d2:
    print("d1 is earlier")

# Rounding to nearest minute or hour
rounded_min = dt.replace(second=0, microsecond=0)
rounded_hour = dt.replace(minute=0, second=0, microsecond=0)

# ISO formatting
print("ISO date:", dt.date().isoformat())      # '2025-01-01'
print("ISO datetime:", dt.isoformat())         # '2025-01-01T12:30:15'

# From timestamp (UNIX time)
ts = 1728123456
from_ts = datetime.datetime.fromtimestamp(ts)
print("From timestamp:", from_ts)

# To timestamp
print("To timestamp:", dt.timestamp())         # seconds since epoch

# Combine and split date and time
combined = datetime.datetime.combine(d, t)
print("Combined:", combined)

print("Date part:", dt.date())
print("Time part:", dt.time())

# UTC vs local time
utc_now = datetime.datetime.utcnow()
print("UTC Now:", utc_now)

# For full timezone support: use `pytz` or `zoneinfo` (Python 3.9+)

# Practical examples

# Expiration check
expires = datetime.datetime(2025, 6, 15)
if datetime.datetime.now() > expires:
    print("Expired")

# Scheduling 7 days from now
print("One week later:", datetime.datetime.now() + datetime.timedelta(days=7))

# Log timestamp
print("Log:", datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"))

# Tips

# - Always be explicit with timezones in real apps (use zoneinfo / pytz)
# - Avoid string comparison of dates — use objects
# - Use ISO 8601 formats for API exchange: `datetime.isoformat()`
