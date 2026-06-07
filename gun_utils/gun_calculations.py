def gun_pct(made, attempted):
    if attempted == 0:
        return 0.0
    return made / attempted


def gun_pct_display(made, attempted):
    if attempted == 0:
        return "0.0%"
    return f"{gun_pct(made, attempted) * 100:.1f}%"


def gun_total_made(workout):
    return int(workout.get("three_made", 0)) + int(workout.get("two_made", 0)) + int(workout.get("free_throw_made", 0))


def gun_total_attempted(workout):
    return int(workout.get("three_attempted", 0)) + int(workout.get("two_attempted", 0)) + int(workout.get("free_throw_attempted", 0))


def gun_fg_made(workout):
    return int(workout.get("three_made", 0)) + int(workout.get("two_made", 0))


def gun_fg_attempted(workout):
    return int(workout.get("three_attempted", 0)) + int(workout.get("two_attempted", 0))
