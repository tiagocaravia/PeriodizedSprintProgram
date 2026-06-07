standards = {
    "10m":     [("<12.0/<24.0", 2.00), ("<11.5/<23.0", 1.92), ("<11.0/<22.0", 1.84), ("<10.5/<21.0", 1.76)],
    "30m":     [("<12.0/<24.0", 4.60), ("<11.5/<23.0", 4.30), ("<11.0/<22.0", 4.00), ("<10.5/<21.0", 3.70)],
    "10m fly": [("<12.0/<24.0", 1.10), ("<11.5/<23.0", 1.05), ("<11.0/<22.0", 1.00), ("<10.5/<21.0", 0.95)],
    "60m":     [("<12.0/<24.0", 7.60), ("<11.5/<23.0", 7.30), ("<11.0/<22.0", 7.00), ("<10.5/<21.0", 6.70)],
    "120m":    [("<12.0/<24.0", 14.25), ("<11.5/<23.0", 13.65), ("<11.0/<22.0", 13.10), ("<10.5/<21.0", 12.50)],
}

bounds = {
    "10m":     (1.60, 3.20),
    "30m":     (3.50, 7.00),
    "10m fly": (0.85, 1.80),
    "60m":     (6.30, 13.00),
    "120m":    (11.50, 22.00),
}


def get_current_tier(event, pr):
    tier = None
    for label, cutoff in standards[event]:
        if pr < cutoff:
            tier = label
    return tier


def get_next_tier(event, pr):
    for label, cutoff in standards[event]:
        if pr >= cutoff:
            return label, cutoff
    return None, None


def get_pr(event):
    low, high = bounds[event]
    while True:
        try:
            pr = float(input(f"Enter your {event} PR in seconds (or 0 to skip): "))
        except ValueError:
            print("  Please enter a valid number.\n")
            continue
        if pr == 0:
            return None
        elif pr < low or pr > high:
            print(f"  Invalid — enter a value between {low}s and {high}s\n")
        else:
            return pr


print("--- Sprint Threshold & Standards Calculator ---\n")

for event in standards:
    pr = get_pr(event)
    if pr is None:
        print()
        continue

    threshold = round(pr / 0.95, 2)
    current_tier = get_current_tier(event, pr)
    next_tier, next_cutoff = get_next_tier(event, pr)

    print(f"\n  PR: {pr}s")
    print(f"  Minimum threshold: {threshold}s")
    print(f"  Current tier: {current_tier if current_tier else 'Below standards'}")
    if next_cutoff:
        diff = round(pr - next_cutoff, 2)
        print(f"  Next tier ({next_tier}): need to hit {next_cutoff}s — {diff}s away")
    else:
        print("  You are at the highest tier!")
    print()