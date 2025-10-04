import re

def format_receipt(items, prices, quantities):
    '''
    Create a formatted receipt using string methods.
    Args:
    items: List of item names
    prices: List of prices (floats)
    quantities: List of quantities (integers)
    Returns:
    str: Formatted receipt with aligned columns
    Format Requirements:
    - Item name: left-aligned, 20 characters
    - Quantity: center-aligned, 5 characters
    - Price: right-aligned, 8 characters with 2 decimal places
    - Total: right-aligned at bottom
    - Use dashes for separator lines
    Example:
    items = ["Coffee", "Sandwich", "Cookie"]
    rices = [3.50, 8.99, 2.00]
    quantities = [2, 1, 3]
    print(format_receipt(items, prices, quantities))
    ========================================
    Item                    Qty    Price
    ========================================
    Coffee                  2      $ 7.00
    Sandwich                1      $ 8.99
    Cookie                  3      $ 6.00
    ========================================
    TOTAL $ 21.99
    ========================================
    '''
    recepit = ("========================================\n" \
        "Item                    Qty     Price\n" \
        "========================================\n")
    cost = 0
    for item in items(range):
        recepit = recepit + f"{items[item]}                  {quantities[item]}     {prices[item]}\n"
        cost = cost + prices*quantities
    recepit = (recepit + "========================================\n" \
        f"TOTAL $ {cost}\n" \
        "========================================\n")
    return recepit
'''
items = ["Coffee", "Sandwich", "Cookie"]
prices = [3.50, 8.99, 2.00]
quantities = [2, 1, 3]
print(format_receipt(items, prices, quantities))
'''
def process_user_data(raw_data):
    '''
    Clean and process user input data using string methods.
    Args:
        raw_data: Dictionary with messy user input
            - 'name': May have extra spaces, wrong capitalization
            - 'email': May have spaces, uppercase letters
            - 'phone': May have various formats
            - 'address': May have inconsistent formatting
    Returns:
        dict: Cleaned data with:
            - 'name': Properly capitalized, trimmed
            - 'email': Lowercase, no spaces
            - 'phone': Digits only
            - 'address': Title case, single spaces
            - 'username': Generated from name (first_last)
            - 'validation': Dict of validation results
    Example:
    >>> data = {
        ... 'name': ' john DOE ',
        ... 'email': ' JOHN.DOE @EXAMPLE.COM ',
        ... 'phone': '(555) 123-4567',
        ... 'address': '123 main street, apt 5'
    ... }
    >>> result = process_user_data(data)
    >>> result['name']
    'John Doe'
    >>> result['email']
    'john.doe@example.com'
    >>> result['phone']
    '5551234567'
    >>> result['username']
    'john_doe'
    '''
    fixed_name = raw_data[0].lower()
    fixed_name = fixed_name.strip()
    fixed_name = fixed_name.capitalize()
    fixed_email = raw_data[1].lower()
    fixed_email = re.sub(r'[ ]', '', fixed_email)
    fixed_num = re.sub(r'[^0-9]', '', raw_data[2])
    fixed_add = raw_data[3].lower()
    fixed_add = fixed_add.capitalize()
    fixed_add = re.sub(r'\s+', ' ', fixed_add)
    username = re.sub(r'\s+', '_', fixed_name)
    fixed_data = {"name": fixed_name, "email": fixed_email, "phone": fixed_num, "address": fixed_add, "username": username}
    return fixed_data

def analyze_text(text):
    """
    Perform comprehensive text analysis using string methods.
    Args:
    text: Multi-line string of text
    Returns:
    dict: Analysis results containing:
    - 'total_chars': Total character count
    - 'total_words': Total word count
    - 'total_lines': Number of lines
    - 'avg_word_length': Average word length (rounded to 2 decimal)
    - 'most_common_word': Most frequently used word (case-insensitive)
    - 'longest_line': The longest line in the text
    - 'words_per_line': List of word counts per line
    - 'capitalized_sentences': Number of sentences starting with capital
    - 'questions': Number of sentences ending with '?'
    - 'exclamations': Number of sentences ending with '!'
    Example:
    >>> text = '''Hello world! How are you?
    ... This is a test. Another line here!'''
    >>> result = analyze_text(text)
    >>> result['total_words']
    11
    >>> result['questions']
    1
    """
    textSplit = text.split()
    text_Dict = {}
    text_Dict['total_chars'] = len(text.strip())
    text_Dict['total_words'] = len(textSplit)
    text_Dict['total_lines'] = text.count('\n') + 1
    text_Dict['avg_word_length'] = sum(map(len, textSplit))/ text_Dict['total_words']
    counter = {}
    for word in textSplit.lower():
        if word in counter.keys():
            counter[word] = counter[word] + 1
        else:
            counter[word] = 1
    pass