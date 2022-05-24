import numpy as np

calorie_stats = np.genfromtxt("cereal.csv", delimiter = ',')

average_calories = np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

count = 0

nth_percentile = np.percentile(calorie_stats_sorted, count)

while nth_percentile < 60:
  count += 1
  nth_percentile = np.percentile(calorie_stats_sorted, count)

print(nth_percentile)
print(count)

more_calories = np.mean(calorie_stats > 60)
print(more_calories)

calorie_std = np.std(calorie_stats)
print(calorie_std)

