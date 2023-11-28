def water_jug_problem(capacity_4, capacity_3, target):
    jug1 = 0
    jug2 = 0
    actions = []

    while jug1 != target and jug2 != target:
        if jug1 == 0:
            jug1 = capacity_4
            actions.append(f"Fill the 4-gallon jug ({jug1} gallons)")
        elif jug2 == capacity_3:
            jug2 = 0
            actions.append("Empty the 3-gallon jug (0 gallons)")
        else:
            transfer = min(jug1, capacity_3 - jug2)
            jug1 -= transfer
            jug2 += transfer
            actions.append(f"Pour {transfer} gallons from the 4-gallon jug to the 3-gallon jug")

    return actions
actions = water_jug_problem(4, 3, 2)
for step, action in enumerate(actions, start=1):
    print(f"Step {step}: {action}")
