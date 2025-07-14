def check_header_order(headers):
    """
    Analyze the sequence and content of HTML headers for semantic correctness and accessibility,
    following best practices (MDN, WCAG).

    - First heading must be <h1>.
    - Only one <h1> ideally.
    - No skipping heading levels upward.
    - No empty headings.
    - No <hN> before its immediate parent <h(N-1)>.
    """
    tips = []
    seen = set()

    def add_tip(msg):
        if msg not in seen:
            tips.append(msg)
            seen.add(msg)

    # Normalize and extract
    header_tags  = [tag.upper() for tag, _ in headers]
    header_texts = [text       for _, text in headers]
    header_levels = []
    for tag in header_tags:
        if len(tag) == 2 and tag[0] == "H" and tag[1].isdigit():
            header_levels.append(int(tag[1]))

    # 1. First heading must be <h1>
    if header_levels:
        if header_levels[0] != 1:
            add_tip("[SHOULD] The first heading should be <h1> (MDN, WCAG).")
    else:
        # No headings at all
        add_tip("[MUST] At least one <h1> should be present (MDN, WCAG).")

    # 2. Ideally only one <h1>
    h1_count = header_tags.count("H1")
    if h1_count > 1:
        add_tip(f"[COULD] Ideally, only one <h1> per page; found {h1_count} (MDN, WCAG).")

    # 3. Do not skip heading levels upward
    skips = set()
    for prev, curr in zip(header_levels, header_levels[1:]):
        if curr - prev > 1:
            skips.add(f"<h{curr}> after <h{prev}>")
    if skips:
        add_tip(f"[SHOULD] Do not skip heading levels upward: {', '.join(sorted(skips))} (MDN, WCAG).")

    # 4. Avoid empty headings
    empty = {f"<{tag}>" for tag, text in zip(header_tags, header_texts) if not text.strip()}
    if empty:
        add_tip(f"[MUST] Avoid empty headings: {', '.join(sorted(empty))} (MDN, WCAG).")

    # 5. Direct-parent hierarchy: <hN> should not precede any <h(N-1)>
    first_seen = {}
    for idx, lvl in enumerate(header_levels):
        first_seen.setdefault(lvl, idx)
    for lvl in range(2, 7):
        if lvl in first_seen and (lvl - 1) in first_seen:
            if first_seen[lvl] < first_seen[lvl - 1]:
                add_tip(
                    f"[COULD] <h{lvl}> appears before its parent <h{lvl-1}>; review outline hierarchy (MDN)."
                )

    return tips