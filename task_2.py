#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for X in [True, False]:
    for Y in [True, False]:
        for Z in [True, False]:
            print(f"X = {X}, Y = {Y}, Z = {Z}")
            print("not(X or Y or Z):", not(X or Y or Z))
            print("not X and not Y and not Z", not X and not Y and not Z)
            print("result: ", not (X or Y or Z) == (not X and not Y and not Z))
            print('')