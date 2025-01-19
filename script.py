import random

# Greeting
print("Hi, Good to see you again!")
print("Follow me on GitHub https://github.com/1kalina\n")

# Input prompts
try:
    members = int(input("How many people are you? "))
    groups = int(input("How many groups do you want to make? "))

    if groups <= 0 or members < groups:
        print("Invalid input: groups must be positive and less than or equal to members.")
    else:
        memb_per_group = members // groups
        remainder = members % groups


        def randomizer(members, groups, memb_per_group, remainder):
            booked = []
            for i in range(1, groups + 1):
                group = []
                for _ in range(memb_per_group):
                    while True:
                        member = random.randint(1, members)
                        if member not in booked:
                            booked.append(member)
                            group.append(member)
                            break
                # Distribute remaining members among groups
                if remainder > 0:
                    while True:
                        member = random.randint(1, members)
                        if member not in booked:
                            booked.append(member)
                            group.append(member)
                            remainder -= 1
                            break

                print(f"Group {i} includes members with numbers: {sorted(group)}")


        randomizer(members, groups, memb_per_group, remainder)

except ValueError:
    print("Please enter valid integers for members and groups.")

