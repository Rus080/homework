Task_completion_rate = 3
Number_of_hours_spent = 2.5
Course_title = 'Python'
Time_per_task = Number_of_hours_spent / Task_completion_rate
Time_per_task = round(Time_per_task, 2)
print('Курс:', Course_title, ', всего задач:', Task_completion_rate, ', затрачено часов:', Number_of_hours_spent,
      ', среднее время выполнения', Time_per_task, 'часа.')
