import events

class EventHandler(object):

    def __init__(self):

        self.events = dict()
        self.default = None

    def add_default(self, callback):
        self.default = callback

    def add_callback(self, event_type, callback):

        if event_type in self.events:
            self.events[event_type].append(callback)
        else:
            self.events[event_type] = [callback]

class CollisionHandler(EventHandler):
    """
    Callbacks must have as input : sprite1, sprite2, map
    Event types are tuple(collision_type1, collision_type2)
    """

    def trigger(self, sprite1, sprite2, map):

        sprites = sorted((sprite1, sprite2), key=lambda x: x.collision_type)

        key = (sprites[0].collision_type, sprites[1].collision_type)

        if key not in self.events:
            self.default(sprites[0], sprites[1], map)
            return

        for callback in self.events[key]:
            callback(sprites[0], sprites[1], map)

class TeleportationHandler(EventHandler):
    """
    Callback msut have as input : sprite, from_map, to_map, portal
    Event types are just "map_change"
    """

    def trigger(self, event_type, sprite, portal):

        for callback in self.events[event_type]:
            callback(sprite, portal)

# Build Teleportation handler
teleportation_handler = TeleportationHandler()
for event in dir(events):
    if event == "default_teleportation_callback":
        teleportation_handler.add_default(getattr(events, "default_teleportation_callback"))
    elif event.endswith("_teleportation_callback"):
        event_type = event.replace("_teleportation_callback", "")
        teleportation_handler.add_callback(event_type, getattr(events, event))

# Build collision handler
collision_handler = CollisionHandler()
for event in dir(events):
    if event == "default_collision_callback":
        collision_handler.add_default(getattr(events, "default_collision_callback"))
    elif event.endswith("_collision_callback"):
        event_type = event.replace("_collision_callback", "")
        event_type = tuple(event_type.split("_"))
        collision_handler.add_callback(event_type, getattr(events, event))
