MIN_HEADING_LEVEL = 1
MAX_HEADING_LEVEL = 6


def heading(text, heading_level=1):
    if heading_level < MIN_HEADING_LEVEL:
        heading_level = MIN_HEADING_LEVEL
    if heading_level > MAX_HEADING_LEVEL:
        heading_level = MAX_HEADING_LEVEL
    heading_markdown = "#" * heading_level
    return f'{heading_markdown} {text}'
