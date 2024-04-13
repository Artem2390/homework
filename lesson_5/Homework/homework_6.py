triggers = (
    "меню",
    "спортзал",
    "обслуговування"
)

discount = 0
feedback = input("Введіть ваш фідбек: ")
feedback_lower = feedback.lower()

for trigger_word in triggers:
    discount_per_word = feedback_lower.count(trigger_word) * 5
    discount += discount_per_word

if len(feedback) > 60:
    discount += 15

# Limit the discount to a maximum of 100%
discount = min(discount, 100)

print(f"Ви отримуєте {discount}% знижки на наступне відвідування.")


