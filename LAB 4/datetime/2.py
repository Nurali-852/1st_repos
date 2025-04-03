from datetime import datetime, timedelta

today = datetime.now()
yester = today - timedelta(days=1)
tomor = today + timedelta(days=1)
print("Today: ", today)
print("Yesterday: ", yester)
print("Tomorrow: ", tomor)