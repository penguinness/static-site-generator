def block_to_block_type(block):
    block = block.strip()

    lines = block.splitlines()

    if (
        lines[0].lstrip().startswith("#")
        and lines[0].count("#") <= 6
        and lines[0][lines[0].find(" ") :].strip()
    ):
        return "heading"
    elif lines[0].lstrip().startswith("```") and lines[-1].lstrip().startswith("```"):
        return "code"
    elif all(line.lstrip().startswith(">") for line in lines):
        return "quote"
    elif all(
        line.lstrip().startswith("* ") or line.lstrip().startswith("- ")
        for line in lines
    ):
        return "unordered_list"
    elif lines[0].lstrip().startswith("1. "):
        numbers = []
        for line in lines:
            line = line.lstrip()
            if line[0].isdigit() and line[1] == "." and line[2] == " ":
                num = int(line[0])
                numbers.append(num)
        if numbers == list(range(1, len(numbers) + 1)):
            return "ordered_list"
    else:
        return "paragraph"
