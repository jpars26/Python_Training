def get_bonus(salary, percentage):
    percentage = percentage / 100
    if salary > 200:
        return  int(salary * (0.35 + percentage)) 
    return int(salary * 0.35)


print(get_bonus(200, 3))
