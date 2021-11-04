import pytz
from datetime import datetime

take_tokyo = datetime.now(
    pytz.timezone("Asia/Tokyo")
)  # https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
tokyo = take_tokyo.strftime("%H:%M:%S")
print("Tokyo Time is", tokyo)
