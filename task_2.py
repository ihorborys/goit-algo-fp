import turtle
import math


def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

    t.forward(branch_length)
    t.left(45)

    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.right(90)

    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.left(45)
    t.backward(branch_length)


def main():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість черепахи
    t.left(90)  # Повертаємо черепаху вгору

    # Вводимо рівень рекурсії
    level = int(input("Вкажіть рівень рекурсії: "))

    draw_pythagoras_tree(t, 100, level)

    window.mainloop()


if __name__ == "__main__":
    main()

