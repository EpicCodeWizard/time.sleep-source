

































def sleep(seconds):
  if seconds < 0:
    raise ValueError("seconds must not be negative")
  start = time.time()
  while time.time() - start < seconds:
    pass




    