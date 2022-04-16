# PersonPlaceThing
This database application tracks people, places, things, events and actions, and the relationships between them.

The inspiration for this application is the game Clue. 
The use case for this application with the game Clue is to describe who killed who with what, where and when.

Using the game Clue to describe the tables:
Person table has Professor Plum and Colonel Mustard etc.
Place table has the Tudor Manor, along with the rooms such as the library and lounge.
Thing table contains the murder weapons, rope, wrench, knife etc.
Event table holds the overall event which is the party to which everyone is invited by Mr. Boddy.
Other events are the murder or murders that took place.
Actions are such things as the use of the murder weapon to commit the murder. Or actions taken to hide one's guilt.
Roles can describe a Person. For example Wadsworth's role is the Butler. 
Roles can also be used to describe connections between other classes beyond the RelationshipType.
RelationshipTypes should be generic connection words between other classes that can be used to make a sentence.

For example RelationshipType = 'is a'
Person = Betty
Role = lawyer
Person -> RelationshipType -> Role

Betty is a lawyer

Another example using both RelationshipType and Role
Thing1 = steering wheel
Thing2 = Dodge truck
RelationshipType = 'is a component of'
Role = 'directional control mechanism'
Thing1 -> RelationshipType -> Thing2 -> Role

The steering wheel is a component of the Dodge truck and is the directional control mechanism.

Each of the basic class types can be connected to any other basic type.
For example, Person can be connected to Place, Thing, Event, Action or another Person.
Thing can be connected to Person, Place, Event, Action or another Thing.
This is done using the connector classes like PersonPlaceConnector.

Factory classes are available for loading collections of objects of the various types.

There are two function addresses that must be passed into the classes, 
the data_saved_callback_func and invalid_data_callback_func handles.
These can be used by the caller to handle program events.
The most basic implementation of these two functions are:

    def data_saved_callback_func(**kwargs):
        for k, v in kwargs.items():
            print(k, v)
    
    
    def invalid_data_callback_func(**kwargs):
        for k, v in kwargs.items():
            print(k, v)

An example keys in kwargs is passed into these are table_name, record_id and message.
This code snippet shows how the function is called internally.

    def _fire_data_saved_callback_func(self, message):
        if self._data_saved_callback_func:
            self._data_saved_callback_func(table_name=self._table_name,
                                            record_id=self.record_id,
                                            message=message)