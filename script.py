import random
from typing import List

def display_greeting():
    """Display welcome message and GitHub link"""
    print("Good to see you again!")
    print("Follow me on GitHub https://github.com/1kalina\n")

def get_valid_input(prompt: str) -> int:
    """Get and validate user input as positive integer"""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

def validate_group_size(members: int, groups: int) -> bool:
    """Validate that group count is reasonable"""
    if groups > members:
        print(f"Cannot create {groups} groups from {members} members.")
        return False
    return True

def generate_member_list(member_count: int) -> List[int]:
    """Generate a shuffled list of member identifiers"""
    members = list(range(1, member_count + 1))
    random.shuffle(members)
    return members

def distribute_members(members: List[int], group_count: int) -> List[List[int]]:
    """Distribute members into groups as evenly as possible"""
    groups = [[] for _ in range(group_count)]
    for i, member in enumerate(members):
        groups[i % group_count].append(member)
    return groups

def display_groups(groups: List[List[int]]):
    """Display the formed groups"""
    for i, group in enumerate(groups, start=1):
        print(f"Group {i} includes members with numbers: {sorted(group)}")

def main():
    display_greeting()

    members = get_valid_input("How many people are you? ")
    groups = get_valid_input("How many groups do you want to make? ")

    if not validate_group_size(members, groups):
        return

    member_list = generate_member_list(members)
    grouped_members = distribute_members(member_list, groups)
    display_groups(grouped_members)

if __name__ == "__main__":
    main()
