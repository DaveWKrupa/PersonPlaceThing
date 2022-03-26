from TableConnector import TableConnector
from Enums import TableNamesEnum


class ActionActionConnector(TableConnector):
    def __init__(self, record_id=None,
                 action_id_a=None, action_id_b=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().ACTION_ACTION, record_id,
                         action_id_a, action_id_b,
                         relationship_type_id, role_id, description)

    @property
    def action_id_a(self):
        return super()._record_id_left

    @action_id_a.setter
    def action_id_a(self, value):
        super()._record_id_left = value

    @property
    def action_id_b(self):
        return super()._record_id_right

    @action_id_b.setter
    def action_id_b(self, value):
        super()._record_id_right = value


class ActionEventConnector(TableConnector):
    def __init__(self, record_id=None,
                 action_id=None, event_id=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().ACTION_EVENT, record_id,
                         action_id, event_id,
                         relationship_type_id, role_id, description)

    @property
    def action_id(self):
        return super()._record_id_left

    @action_id.setter
    def action_id(self, value):
        super()._record_id_left = value

    @property
    def event_id(self):
        return super()._record_id_right

    @event_id.setter
    def event_id(self, value):
        super()._record_id_right = value


class ActionPlaceConnector(TableConnector):
    def __init__(self, record_id=None,
                 action_id=None, place_id=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().ACTION_PLACE, record_id,
                         action_id, place_id,
                         relationship_type_id, role_id, description)

    @property
    def action_id(self):
        return super()._record_id_left

    @action_id.setter
    def action_id(self, value):
        super()._record_id_left = value

    @property
    def place_id(self):
        return super()._record_id_right

    @place_id.setter
    def place_id(self, value):
        super()._record_id_right = value


class EventEventConnector(TableConnector):
    def __init__(self, record_id=None,
                 event_id_a=None, event_id_b=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().EVENT_EVENT, record_id,
                         event_id_a, event_id_b,
                         relationship_type_id, role_id, description)

    @property
    def event_id_a(self):
        return super()._record_id_left

    @event_id_a.setter
    def event_id_a(self, value):
        super()._record_id_left = value

    @property
    def event_id_b(self):
        return super()._record_id_right

    @event_id_b.setter
    def event_id_b(self, value):
        super()._record_id_right = value


class EventPlaceConnector(TableConnector):
    def __init__(self, record_id=None,
                 event_id=None, place_id=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().EVENT_PLACE, record_id,
                         event_id, place_id,
                         relationship_type_id, role_id, description)

    @property
    def event_id(self):
        return super()._record_id_left

    @event_id.setter
    def event_id(self, value):
        super()._record_id_left = value

    @property
    def place_id(self):
        return super()._record_id_right

    @place_id.setter
    def place_id(self, value):
        super()._record_id_right = value


class PersonActionConnector(TableConnector):
    def __init__(self, record_id=None,
                 person_id=None, action_id=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().PERSON_ACTION, record_id,
                         person_id, action_id,
                         relationship_type_id, role_id, description)

    @property
    def person_id(self):
        return super()._record_id_left

    @person_id.setter
    def person_id(self, value):
        super()._record_id_left = value

    @property
    def action_id(self):
        return super()._record_id_right

    @action_id.setter
    def action_id(self, value):
        super()._record_id_right = value


class PersonEventConnector(TableConnector):
    def __init__(self, record_id=None,
                 person_id=None, event_id=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().PERSON_EVENT, record_id,
                         person_id, event_id,
                         relationship_type_id, role_id, description)

    @property
    def person_id(self):
        return super()._record_id_left

    @person_id.setter
    def person_id(self, value):
        super()._record_id_left = value

    @property
    def event_id(self):
        return super()._record_id_right

    @event_id.setter
    def event_id(self, value):
        super()._record_id_right = value


class PersonPersonConnector(TableConnector):
    def __init__(self, record_id=None,
                 person_id_a=None, person_id_b=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().PERSON_PERSON, record_id,
                         person_id_a, person_id_b,
                         relationship_type_id, role_id, description)

    @property
    def person_id_a(self):
        return super()._record_id_left

    @person_id_a.setter
    def person_id_a(self, value):
        super()._record_id_left = value

    @property
    def person_id_b(self):
        return super()._record_id_right

    @person_id_b.setter
    def person_id_b(self, value):
        super()._record_id_right = value


class PersonPlaceConnector(TableConnector):
    def __init__(self, record_id=None,
                 person_id=None, place_id=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().PERSON_PLACE, record_id,
                         person_id, place_id,
                         relationship_type_id, role_id, description)

    @property
    def person_id(self):
        return super()._record_id_left

    @person_id.setter
    def person_id(self, value):
        super()._record_id_left = value

    @property
    def place_id(self):
        return super()._record_id_right

    @place_id.setter
    def place_id(self, value):
        super()._record_id_right = value


class PersonThingConnector(TableConnector):
    def __init__(self, record_id=None,
                 person_id=None, thing_id=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().PERSON_THING, record_id,
                         person_id, thing_id,
                         relationship_type_id, role_id, description)

    @property
    def person_id(self):
        return super()._record_id_left

    @person_id.setter
    def person_id(self, value):
        super()._record_id_left = value

    @property
    def thing_id(self):
        return super()._record_id_right

    @thing_id.setter
    def thing_id(self, value):
        super()._record_id_right = value


class PersonRoleConnector(TableConnector):
    def __init__(self, record_id=None,
                 person_id=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().PERSON_ROLE, record_id,
                         person_id, None,
                         relationship_type_id, role_id, description)

    @property
    def person_id(self):
        return super()._record_id_left

    @person_id.setter
    def person_id(self, value):
        super()._record_id_left = value


class PlacePlaceConnector(TableConnector):
    def __init__(self, record_id=None,
                 place_id_a=None, place_id_b=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().PLACE_PLACE, record_id,
                         place_id_a, place_id_b,
                         relationship_type_id, role_id, description)

    @property
    def place_id_a(self):
        return super()._record_id_left

    @place_id_a.setter
    def place_id_a(self, value):
        super()._record_id_left = value

    @property
    def place_id_b(self):
        return super()._record_id_right

    @place_id_b.setter
    def place_id_b(self, value):
        super()._record_id_right = value


class ThingThingConnector(TableConnector):
    def __init__(self, record_id=None,
                 thing_id_a=None, thing_id_b=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().THING_THING, record_id,
                         thing_id_a, thing_id_b,
                         relationship_type_id, role_id, description)

    @property
    def thing_id_a(self):
        return super()._record_id_left

    @thing_id_a.setter
    def thing_id_a(self, value):
        super()._record_id_left = value

    @property
    def thing_id_b(self):
        return super()._record_id_right

    @thing_id_b.setter
    def thing_id_b(self, value):
        super()._record_id_right = value


class ThingPlaceConnector(TableConnector):
    def __init__(self, record_id=None,
                 thing_id=None, place_id=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().THING_PLACE, record_id,
                         thing_id, place_id,
                         relationship_type_id, role_id, description)

    @property
    def thing_id(self):
        return super()._record_id_left

    @thing_id.setter
    def thing_id(self, value):
        super()._record_id_left = value

    @property
    def place_id(self):
        return super()._record_id_right

    @place_id.setter
    def place_id(self, value):
        super()._record_id_right = value


class ThingActionConnector(TableConnector):
    def __init__(self, record_id=None,
                 thing_id=None, action_id=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().THING_ACTION, record_id,
                         thing_id, action_id,
                         relationship_type_id, role_id, description)

    @property
    def thing_id(self):
        return super()._record_id_left

    @thing_id.setter
    def thing_id(self, value):
        super()._record_id_left = value

    @property
    def action_id(self):
        return super()._record_id_right

    @action_id.setter
    def action_id(self, value):
        super()._record_id_right = value


class ThingEventConnector(TableConnector):
    def __init__(self, record_id=None,
                 thing_id=None, event_id=None,
                 relationship_type_id=None, role_id=None, description=None):
        super().__init__(TableNamesEnum().THING_EVENT, record_id,
                         thing_id, event_id,
                         relationship_type_id, role_id, description)

    @property
    def thing_id(self):
        return super()._record_id_left

    @thing_id.setter
    def thing_id(self, value):
        super()._record_id_left = value

    @property
    def event_id(self):
        return super()._record_id_right

    @event_id.setter
    def event_id(self, value):
        super()._record_id_right = value
