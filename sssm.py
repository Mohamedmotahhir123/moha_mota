from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ObjectProperty
from kivy.clock import Clock
import random


class Player(Widget):
    score = NumericProperty(0)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class Enemy(Widget):
    def reset_position(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(300, 550)


class GameWidget(Widget):
    player = ObjectProperty(None)
    enemy = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1 / 60)

    def update(self, dt):
        if self.enemy.collide_widget(self.player):
            self.enemy.reset_position()
            self.player.score += 1

    def move_player(self, direction):
        if direction == "up":
            self.player.move(0, 10)
        elif direction == "down":
            self.player.move(0, -10)
        elif direction == "left":
            self.player.move(-10, 0)
        elif direction == "right":
            self.player.move(10, 0)


class SmileyApp(App):
    def build(self):
        game = GameWidget()

        # Add control buttons
        controls = Widget(size=(800, 200))

        btn_up = Button(text="Up", size_hint=(0.2, 0.2), pos=(300, 0))
        btn_up.bind(on_press=lambda x: game.move_player("up"))

        btn_down = Button(text="Down", size_hint=(0.2, 0.2), pos=(300, 100))
        btn_down.bind(on_press=lambda x: game.move_player("down"))

        btn_left = Button(text="Left", size_hint=(0.2, 0.2), pos=(200, 50))
        btn_left.bind(on_press=lambda x: game.move_player("left"))

        btn_right = Button(text="Right", size_hint=(0.2, 0.2), pos=(400, 50))
        btn_right.bind(on_press=lambda x: game.move_player("right"))

        controls.add_widget(btn_up)
        controls.add_widget(btn_down)
        controls.add_widget(btn_left)
        controls.add_widget(btn_right)

        root = Widget()
        root.add_widget(game)
        root.add_widget(controls)

        return root


if __name__ == "__main__":
    SmileyApp().run()
