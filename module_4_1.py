from fake_math import divide as div_fake
from true_math import divide as div_true

result1 = div_fake(26,4)
print(result1)
result2 = div_fake(15, 0)
print(result2)
result3 = div_true(36, 6)
print(result3)
result4 = div_true(14, 0)
print(result4)