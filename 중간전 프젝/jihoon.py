# Example: Creating a list of 300 people with names and IDs
volunteers = []

for i in range(1, 301):  # Loop from 1 to 300
    volunteer = {
        "id": f"ID{i:03}",  # Generate ID like ID001, ID002, ..., ID300
        "name": f"Volunteer{i}"  # Generate names like Volunteer1, Volunteer2, ..., Volunteer300
    }
    volunteers.append(volunteer)

# Print the list of volunteers
for v in volunteers:
    print(v)