# Lambda with if but without else in Python

# 1. Lambda with if but without else, None if condition is False
f1 = lambda x: x**2 if x > 0 else None

# 2. Lambda with if and else, True/False
f2 = lambda x: x**2 if x > 0 else -1

# 3. Lambda with only else, not possible directly
f3 = lambda x: None if x > 0 else x**2

# 4. Lambda without if or else, returns the value
f4 = lambda x: x**2

print(f"f1(5): {f1(5)}")    # 25
print(f"f1(-3): {f1(-3)}")  # None

print(f"f2(5): {f2(5)}")    # 25
print(f"f2(-3): {f2(-3)}")  # -1

print(f"f3(5): {f3(5)}")    # None
print(f"f3(-3): {f3(-3)}")  # 9

print(f"f4(5): {f4(5)}")    # 25
print(f"f4(-3): {f4(-3)}")  # 9

# Code by Harshit