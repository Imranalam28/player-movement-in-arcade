import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 5

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.WHITE)
        self.player = None
        self.enemy_list = None

    def setup(self):
        self.player = Player("player.png", 0.04)
        self.player.center_x = SCREEN_WIDTH / 2
        self.player.center_y = SCREEN_HEIGHT / 2
        self.enemy_list = arcade.SpriteList()
        for i in range(10):
            enemy = arcade.Sprite("enemy.png", 0.04)
            enemy.center_x = i * 60 + 30
            enemy.center_y = SCREEN_HEIGHT - 30
            self.enemy_list.append(enemy)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.enemy_list.draw()

    def on_update(self, delta_time):
        self.player.update()
        collisions = arcade.check_for_collision_with_list(self.player, self.enemy_list)
        for collision in collisions:
            collision.kill()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.player.center_x = x
        self.player.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Player Movement Example")
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
