class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:
    if not people:
        return []
    for person_data in people:
        Person(name=person_data["name"], age=person_data["age"])
    person_instances = []
    for person_data in people:
        name = person_data["name"]
        current_instance = Person.people[name]
        partner_key = "wife" if "wife" in person_data else \
            ("husband" if "husband" in person_data else None)
        if partner_key and person_data.get(partner_key) is not None:
            partner_name = person_data[partner_key]
            partner_instance = Person.people.get(partner_name)
            if partner_key == "wife":
                current_instance.wife = partner_instance
            elif partner_key == "husband":
                current_instance.husband = partner_instance
        person_instances.append(current_instance)
    return person_instances
