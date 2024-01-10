import re
def single_line_parentheses_converter(code):
    def clean_parentheses(match):
        # Replace newlines and multiple spaces with a single space
        inner_content = match.group(0)
        cleaned_content = re.sub(r'\s+', ' ', inner_content)
        return cleaned_content

    # Match parentheses, including nested ones
    pattern = r'\((?:[^()]|\([^()]*\))*\)'
    single_line_code = re.sub(pattern, clean_parentheses, code)

    return single_line_code 