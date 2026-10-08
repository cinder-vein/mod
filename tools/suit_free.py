"""Ring abilities work whenever the ring is worn, suit or no suit.

In A New Corps, each ring's power has a suit toggle (a dummy ability toggled on its bar, usually named after the
power) and most of its abilities only unlock or run while that toggle is on. free_from_suit() rewrites a ring power so
the toggle only controls how you look: the suit and mask layers, hidden skin layers, the transformation animation, the
name change, the screen tint, the suit-up sound and the armor swap still follow it; everything else (beams,
constructs, the skill tree, flight, armor and health upgrades, immunities...) works while the ring is worn.

The rewrite treats "the suit is on" as always true inside the power and simplifies each condition with Palladium's
own logic (not: none true, or: any true, and: all true).
"""
import json

COSMETIC = {"palladium:render_layer", "palladium:render_layer_by_accessory_slot", "palladium:hide_body_part",
            "palladium:animation_timer", "palladium:repeating_animation_timer", "palladium:name_change",
            "palladium:shader_effect", "palladium:restrict_slots", "palladium:trail"}
COSMETIC_COMMANDS = ("playsound ", "pocket ")  # the suit-up sound; storing and restoring your armor
TRUE, FALSE = True, False
NEVER = {"type": "palladium:false"}


def suit_toggles(power):
    """The power's suit toggle(s): dummy abilities switched by a toggle key (Phasing is an ability, not the suit)."""
    out = []
    for key, ab in power.get("abilities", {}).items():
        enabling = ab.get("conditions", {}).get("enabling", [])
        enabling = enabling if isinstance(enabling, list) else [enabling]
        if (ab.get("type") == "palladium:dummy" and key != "phasing"
                and any(c.get("type") == "palladium:toggle" for c in enabling if isinstance(c, dict))):
            out.append(key)
    return out


def cosmetic(ab):
    if ab.get("type") in COSMETIC:
        return True
    if ab.get("type") == "palladium:command":
        cmds = [c for k in ("first_tick_commands", "commands", "last_tick_commands") for c in ab.get(k, [])]
        return bool(cmds) and all(c.startswith(COSMETIC_COMMANDS) for c in cmds)
    return False


def simplify(cond, toggles, power_id):
    """TRUE, FALSE or a condition, with the suit toggle(s) taken as on."""
    if not isinstance(cond, dict):
        return cond
    t = cond.get("type")
    # "the suit is on" is always true now; "the suit node is unlocked" was always true anyway (it only needs the bar)
    # and stays, so the tree keeps its lines from the suit node
    if (t == "palladium:ability_enabled" and cond.get("ability") in toggles
            and cond.get("power") in (None, "null", power_id)):
        return TRUE
    if t in ("palladium:not", "palladium:or", "palladium:and"):
        inner = [simplify(c, toggles, power_id) for c in cond.get("conditions", [])]
        rest = [c for c in inner if c is not TRUE and c is not FALSE]
        if t == "palladium:not":
            if any(c is TRUE for c in inner):
                return FALSE
            return {**cond, "conditions": rest} if rest else TRUE
        if t == "palladium:or":
            if any(c is TRUE for c in inner):
                return TRUE
            return (rest[0] if len(rest) == 1 else {**cond, "conditions": rest}) if rest else FALSE
        if any(c is FALSE for c in inner):
            return FALSE
        return (rest[0] if len(rest) == 1 else {**cond, "conditions": rest}) if rest else TRUE
    return cond


def free_from_suit(power, power_id):
    """Rewrites the power in place; returns how many abilities changed."""
    toggles = set(suit_toggles(power))
    changed = 0
    if not toggles:
        return changed
    for key, ab in power.get("abilities", {}).items():
        if key in toggles or cosmetic(ab) or "conditions" not in ab:
            continue
        before = json.dumps(ab["conditions"], sort_keys=True)
        new = {}
        for kind, value in ab["conditions"].items():
            items = value if isinstance(value, list) else [value]
            out = [simplify(c, toggles, power_id) for c in items]
            if any(c is FALSE for c in out):
                new[kind] = [NEVER]
            else:
                kept = [c for c in out if c is not TRUE]
                if kept:
                    new[kind] = kept
        ab["conditions"] = new
        if json.dumps(new, sort_keys=True) != before:
            changed += 1
    return changed
