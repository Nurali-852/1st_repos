import math
import time

def calculate_sqrt_after_delay(number, delay_ms):
    time.sleep(delay_ms / 1000)

    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

number = 25100
delay_ms = 2123

calculate_sqrt_after_delay(number, delay_ms)
