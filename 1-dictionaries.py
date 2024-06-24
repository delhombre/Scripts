#!/usr/bin/python3
# Assign values to a dictionary
flight_data = {
    "Flight": "FR6556",
    "Company": "SERKANAIR",
    "Destination": "ISTANBUL",
    "Status": "Bording",
}

# Print values from dictionary
print(flight_data, end="\n\n")
print(flight_data.keys())
print(flight_data.values(), end="\n\n")

flight_data["Status"] = "Departed"
print("Flight " + flight_data["Flight"] + " status : " + flight_data["Status"])
