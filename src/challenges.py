"""Week 9 Homework: The Case of the Missing Festival Lanterns."""

EXPECTED_LANTERNS = {
    "river-dragon",
    "blue-crane",
    "moon-rabbit",
    "gold-tiger",
    "white-lotus",
    "red-kite",
}

LANTERN_LOG = [
    ("river-dragon", "North Gate"),
    ("blue-crane", "River Walk"),
    ("moon-rabbit", "River Walk"),
    ("river-dragon", "North Gate"),
    ("gold-tiger", "Market Street"),
    ("silver-fox", "Market Street"),
    ("red-kite", "South Bridge"),
]

CORRECT_SECTIONS = {
    "river-dragon": "North Gate",
    "blue-crane": "River Walk",
    "moon-rabbit": "River Walk",
    "gold-tiger": "Market Street",
    "white-lotus": "Temple Road",
    "red-kite": "Temple Road",
}


def analyze_lanterns(
    expected_lanterns: set[str],
    lantern_log: list[tuple[str, str]],
    correct_sections: dict[str, str],
) -> dict[str, object]:
    seen_lanterns = set()
    seen_once = set()
    duplicate_lanterns = set()
    count_by_section = {}
    wrong_section_lanterns = {}

    for lantern_name, actual_section in lantern_log:
        if lantern_name in seen_once:
            duplicate_lanterns.add(lantern_name)
        else:
            seen_once.add(lantern_name)
        seen_lanterns.add(lantern_name)

        count_by_section[actual_section] = count_by_section.get(actual_section, 0) + 1

        if lantern_name in expected_lanterns:
            expected_section = correct_sections.get(lantern_name)
            if expected_section and actual_section != expected_section:
                if lantern_name not in wrong_section_lanterns:
                    wrong_section_lanterns[lantern_name] = {
                        "expected": expected_section,
                        "actual": actual_section,
                    }

    missing_lanterns = expected_lanterns - seen_lanterns
    unexpected_lanterns = seen_lanterns - expected_lanterns

    return {
        "seen_lanterns": seen_lanterns,
        "missing_lanterns": missing_lanterns,
        "unexpected_lanterns": unexpected_lanterns,
        "duplicate_lanterns": duplicate_lanterns,
        "count_by_section": count_by_section,
        "wrong_section_lanterns": wrong_section_lanterns,
    }


if __name__ == "__main__":
    report = analyze_lanterns(EXPECTED_LANTERNS, LANTERN_LOG, CORRECT_SECTIONS)
    print(report)