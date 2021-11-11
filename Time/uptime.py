import ctypes

lib = ctypes.windll.kernel32
a = lib.GetTickCount64()

b = int(str(a)[:-3])

mins, sec = divmod(b, 60)
hour, mins = divmod(mins, 60)
days, hour = divmod(hour, 24)

print(f"Uptime OS: {days} days, {hour:02}:{mins:02}:{sec:02}")
