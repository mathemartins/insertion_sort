from chideraIbeh.assignment5.familyTree import FamilyTree

if __name__ == '__main__':
    # Example usage:
    family = FamilyTree()

    # Adding family members
    family.add_family_member("John", "Male", 35)
    family.add_family_member("Jane", "Female", 32)
    family.add_family_member("Alice", "Female", 12)

    # Adding relationships
    family.add_relationship("John", "Jane", "Married")
    family.add_relationship("John", "Alice", "Child")

    # CLI interaction (assuming calling these methods in a loop for interaction)
    family.cli_add_family_member()
    family.cli_add_relationship()
    family.cli_edit_family_member()

    # Enforcing data assertions
    family.enforce_rules()