from chideraIbeh.assignment5.graph import Graph


class FamilyTree:
    def __init__(self):
        self.graph = Graph()
        self.family_members = {}  # Mapping of person name to their details

    def add_family_member(self, name, gender, age):
        if name not in self.family_members:
            self.family_members[name] = {'gender': gender, 'age': age}
            self.graph.add_node(name)
        else:
            print("Person with this name already exists.")

    def add_relationship(self, person1, person2, relationship):
        if person1 in self.family_members and person2 in self.family_members:
            self.graph.add_edge(person1, person2, relationship)
        else:
            print("One or both persons do not exist in the family tree.")

    def edit_family_member(self, name, attribute, value):
        if name in self.family_members:
            if attribute in self.family_members[name]:
                self.family_members[name][attribute] = value
            else:
                print("Invalid attribute.")
        else:
            print("Person does not exist.")

    # Data assertions
    def enforce_rules(self):
        for person in self.graph.adjacency_list:
            relationships = self.graph.adjacency_list[person]
            for relative, relation in relationships:
                if person == relative:
                    raise ValueError("A person cannot have a relationship with themselves.")
                # Implement more rules as required

    # CLI methods for user interaction
    def cli_add_family_member(self):
        name = input("Enter name: ")
        gender = input("Enter gender: ")
        age = input("Enter age: ")
        self.add_family_member(name, gender, age)

    def cli_add_relationship(self):
        person1 = input("Enter name of person 1: ")
        person2 = input("Enter name of person 2: ")
        relationship = input("Enter relationship: ")
        self.add_relationship(person1, person2, relationship)

    def cli_edit_family_member(self):
        name = input("Enter name of person to edit: ")
        attribute = input("Enter attribute to edit: ")
        value = input("Enter new value: ")
        self.edit_family_member(name, attribute, value)
