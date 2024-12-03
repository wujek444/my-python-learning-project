def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    return L[1] if len(L) > 1 else None


def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]


def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.

    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0], racers[-1] = racers[-1], racers[0]

def fashionably_late(arrivals: list, name: str):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    fashionably_late_after_idx = len(arrivals) / 2
    last_index = len(arrivals) - 1
    guest_index = arrivals.index(name)
    return guest_index >= fashionably_late_after_idx and guest_index != last_index