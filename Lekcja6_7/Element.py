import pygame

class Image(pygame.sprite.Sprite):
    def __init__(self, path) -> None:
        super().__init__()
        self.image = pygame.image.load(path)

class Element():
    def __init__(self, type) -> None:
        self.choice = 0
        self.image_list = []

        for i in range(1,4):
            path = f"images/{type}{i}.png"
            loaded_image = Image(path)
            self.image_list.append(loaded_image)
        pass

    def chooseNext(self):
        self.choice += 1
        if self.choice > 2:
            self.choice = 0

    def choosenImage(self):
        return self.image_list[self.choice].image

class HeadWear(Element):
    def __init__(self) -> None:
        super().__init__('head')

class Eyes(Element):
    def __init__(self) -> None:
        super().__init__('eye')

class BodyWear(Element):
    def __init__(self) -> None:
        super().__init__('body')

class Weapon(Element):
    def __init__(self) -> None:
        super().__init__('weapon')
