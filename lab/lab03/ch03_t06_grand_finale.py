from datetime import datetime

now = datetime.now()

print('%02d:%02%d:%04d' % (now.hour, now.minute, now.second))
