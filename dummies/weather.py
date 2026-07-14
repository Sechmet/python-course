# weather.py - Dummies Section
# A beginner-friendly script to get started with weather data


TEMPERATURE = 5
WATER_TEMPERATURE = 24
WIND_SPEED = 8


GO_SWIM = TEMPERATURE > 25 and WATER_TEMPERATURE > 20 and WIND_SPEED < 10
GO_WALK = TEMPERATURE > 20 and WIND_SPEED < 10

print(f"go swim: {GO_SWIM}")
print(f"go walk: {GO_WALK}")

if TEMPERATURE >= 20 and WIND_SPEED <= 10:
    weather = "good"
elif TEMPERATURE >= 25:
    weather = "still good"
else:
    weather = "bad"

print(f"{weather}")