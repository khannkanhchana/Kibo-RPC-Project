import random
battery = 100.0
for waypoint in range(1, 11):
    battery -= random.uniform(1.5, 3.5)
    print(f"Waypoint {waypoint}: Battery = {battery:.2f}%")
    if battery < 75:
        print("[EMERGENCY RETURN TRIGGERED]")
        break
    if battery < 80:
        print("[CAUTION] Battery below 80%!")