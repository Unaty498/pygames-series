import pygame

from src.animation import AnimateSprite


class Entity(AnimateSprite):

    def __init__(self, name, x, y):
        super().__init__(name)
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2(x, y)
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = pygame.Vector2(self.position.x, self.position.y)

    def save_location(self): self.old_position = pygame.Vector2(self.position.x, self.position.y)

    def move(self, inputs: pygame.Vector2):
        if inputs.magnitude() == 0:
            self.image = self.images['down'][1]
            self.image.set_colorkey(0, 0)
        else:
            direction = inputs.normalize()
            movement = pygame.Vector2(round(direction.x), round(direction.y))
            self.change_animation('down' if movement.y > 0 and movement.y > abs(movement.x) else ('up' if movement.y < 0 and movement.y < -abs(movement.x) else ('left' if movement.x < 0 else 'right')))
            self.position += movement

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.update()

    def objective_to_direction(self, objective: pygame.math.Vector2):
        return pygame.math.Vector2(0, 0) if objective == self.position else pygame.math.Vector2(
            objective.x - self.position.x, objective.y - self.position.y
        ).normalize()


class Player(Entity):

    def __init__(self):
        super().__init__('player', 0, 0)


class NPC(Entity):
    def __init__(self, name, pathPointsCount, dialog):
        super().__init__(name, 0, 0)
        self.pathPointsCount = pathPointsCount
        self.dialog = dialog
        self.points: list[pygame.Vector2] = []
        self.name = name
        self.speed = 0.50
        self.current_point = 0

    def target_point(self):
        target_point = self.current_point + 1

        if target_point >= self.pathPointsCount:
            target_point = 0

        point_pos = self.points[target_point]
        if(self.position - point_pos).magnitude() < 3:
            self.current_point = target_point
            return
        self.move(self.objective_to_direction(point_pos))

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def load_points(self, tmx_data):
        for num in range(1, self.pathPointsCount + 1):
            point = tmx_data.get_object_by_name(f'{self.name}_path{num}')
            position = pygame.Vector2(point.x, point.y)
            self.points.append(position)
