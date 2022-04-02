from DataFactory import PersonFactory, PlaceFactory, ThingFactory, RoleFactory
from DataFactory import TagsList, RelationshipTypeFactory

pf = PersonFactory()
# data = pf.get_all()
# print(data)

# data = pf.get_where_like(first_name='Mrs.')
# for k, v in data.items():
#     print(k, v.first_name)

data = pf.get_all()
for k, v in data.items():
    print(k, v.first_name)

print("*********************************************")
place_factory = PlaceFactory()
data = place_factory.get_all()
for k, v in data.items():
    print(k, v.short_description)

print("*********************************************")
thing_factory = ThingFactory()
data = thing_factory.get_all()
for k, v in data.items():
    print(k, v.short_description)

print("*********************************************")
role_factory = RoleFactory()
data = role_factory.get_all()
for k, v in data.items():
    print(k, v.short_description)
print("*********************************************")
#data = role_factory.get_person_roles("aae5e380-351b-4448-b3c1-9c2ca6e49869")
#print(data)
# for k, v in data.items():
#     print(k, v.short_description)
# role_factory = RoleFactory()
#
data = role_factory.get_by_tags(["family", "crime", "social"])
for k, v in data.items():
    print(k, v.short_description, v.tags)
print("*********************************************")

tags = TagsList().get_tags_list()
print(tags)

print("*********************************************")

rel_type_factory = RelationshipTypeFactory()
data = rel_type_factory.get_all()
for k, v in data.items():
    print(k, v.short_description)
print("*********************************************")
data = rel_type_factory.get_by_tags("family", "crime")
for k, v in data.items():
    print(k, v.short_description, v.tags)
print("*********************************************")