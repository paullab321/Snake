import random
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, SPEED, MAX_SPEED, SPACE_SIZE, BODY_PARTS, SNAKE_BODY_COLOR, FOOD_COLOR

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            # starting coordinates top left
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            # noinspection PyArgumentList
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_BODY_COLOR,
                                             outline=SNAKE_BODY_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        x_spawn = random.randint(0, int((WINDOW_WIDTH / SPACE_SIZE)) - 1) * SPACE_SIZE
        y_spawn = random.randint(0, int((WINDOW_HEIGHT / SPACE_SIZE)) - 1) * SPACE_SIZE

        self.coordinates = [x_spawn, y_spawn]

        # noinspection PyArgumentList
        canvas.create_oval(x_spawn, y_spawn, x_spawn + SPACE_SIZE, y_spawn + SPACE_SIZE, fill=FOOD_COLOR,
                           outline=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    global SPEED

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    # noinspection PyArgumentList
    square = (canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_BODY_COLOR, tag="snake"))

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label_score.config(text="Score: " + str(score))

        canvas.delete("food")

        if SPEED > MAX_SPEED:
            SPEED = SPEED - 5

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collision(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)
        return False


def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= WINDOW_WIDTH:
        return True

    elif y < 0 or y >= WINDOW_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    canvas.delete(ALL)
    # noinspection PyArgumentList
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 70), text="Game Over", fill="red", tag="gameover")

    # button = Button(window, text="Retry", command= run_game)
    # button.pack()
    # window.update()


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'right'

label_score = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label_score.pack()

# New label
label_info = Label(window, text="Welcome to Snake Game", font=('consolas', 20))
label_info.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


def run_game():
    snake = Snake()
    food = Food()
    next_turn(snake, food)
    window.mainloop()


def main():
    run_game()


main()
