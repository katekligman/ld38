def default_collision_callback(sprite1, sprite2, map):
    if sprite1.map is None:
        map.add_sprite(sprite1)
    elif sprite2.map is None:
        map.add_sprite(sprite2)

def creature_hero_collision_callback(creature, hero, map):

    raise Exception("hero collided")

def hero_portal_collision_callback(hero, portal, map):

    raise Exception("hero at portal")
