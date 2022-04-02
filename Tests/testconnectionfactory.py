from ConnectionFactory import PersonEventFactory
from Enums import TableNamesEnum

print(TableNamesEnum.PERSON_EVENT_VIEW)
pef = PersonEventFactory()
data = pef.get_all()
for k, v in data.items():
    print(k, v.person.first_name, v.role.short_description, v.relationship_type.short_description, v.event.short_description)
