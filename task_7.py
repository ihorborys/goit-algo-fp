import random
import matplotlib.pyplot as plt


def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)


def simulate_rolls(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        die1, die2 = roll_dice()
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1
    return sum_counts


def calculate_probabilities(sum_counts, num_rolls):
    probabilities = {k: v / num_rolls for k, v in sum_counts.items()}
    return probabilities


def plot_probabilities(probabilities, analytical_probs):
    sums = list(probabilities.keys())
    monte_carlo_probs = list(probabilities.values())
    analytical_probs = [analytical_probs[i] for i in sums]

    x = range(len(sums))

    plt.figure(figsize=(10, 6))
    plt.bar(x, monte_carlo_probs, width=0.4, label='Monte Carlo', color='blue', align='center')
    plt.bar(x, analytical_probs, width=0.4, label='Analytical', color='red', align='edge')

    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.xticks(x, sums)
    plt.legend()
    plt.show()


# Аналітичні ймовірності
analytical_probs = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}

# Параметри симуляції
num_rolls = 100000

# Симуляція кидків
sum_counts = simulate_rolls(num_rolls)

# Обчислення ймовірностей за результатами симуляції
monte_carlo_probs = calculate_probabilities(sum_counts, num_rolls)

# Відображення результатів
plot_probabilities(monte_carlo_probs, analytical_probs)

# Виведення ймовірностей для кожної суми
print("Ймовірності (Метод Монте-Карло):")
for sum_, prob in monte_carlo_probs.items():
    print(f"Сума {sum_}: {prob:.4f}")

print("\nАналітичні ймовірності:")
for sum_, prob in analytical_probs.items():
    print(f"Сума {sum_}: {prob:.4f}")
