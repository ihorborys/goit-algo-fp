items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100


def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    chosen_items = []

    for item, values in sorted_items:
        if values['cost'] <= budget:
            budget -= values['cost']
            total_calories += values['calories']
            chosen_items.append(item)

    return chosen_items, total_calories


chosen_items, total_calories = greedy_algorithm(items, budget)
print(f"Greedy algorithm, chosen items: {chosen_items}")
print(f"Greedy algorithm, total calories: {total_calories}")




def dynamic_programming(items, budget):
    # Створюємо таблицю для зберігання максимальних калорій при кожному значенні бюджету
    dp = [0] * (budget + 1)

    # Заповнюємо таблицю динамічного програмування
    for item in items.values():
        cost = item['cost']
        calories = item['calories']
        for b in range(budget, cost - 1, -1):
            dp[b] = max(dp[b], dp[b - cost] + calories)

    # Знаходимо які предмети були обрані
    total_calories = dp[budget]
    chosen_items = []
    remaining_budget = budget
    for item, values in items.items():
        cost = values['cost']
        calories = values['calories']
        if remaining_budget >= cost and dp[remaining_budget] - dp[remaining_budget - cost] == calories:
            chosen_items.append(item)
            remaining_budget -= cost

    return chosen_items, total_calories


chosen_items, total_calories = dynamic_programming(items, budget)
print(f"Dynamic programming, chosen items: {chosen_items}")
print(f"Dynamic programming, total calories: {total_calories}")