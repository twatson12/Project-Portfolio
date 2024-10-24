import re

def check_password_strength(password):
    """
    Check password strength and return a detailed analysis
    Returns: Dictionary containing strength score and detailed feedback
    """
    analysis = {
        'score': 0,
        'length': 0,
        'has_upper': False,
        'has_lower': False,
        'has_digit': False,
        'has_special': False,
        'feedback': []
    }
    
    # Check length
    if len(password) >= 12:
        analysis['score'] += 2
        analysis['feedback'].append("Good length")
    elif len(password) >= 8:
        analysis['score'] += 1
        analysis['feedback'].append("Acceptable length")
    else:
        analysis['feedback'].append("Password is too short - should be at least 8 characters")
    analysis['length'] = len(password)
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        analysis['score'] += 1
        analysis['has_upper'] = True
    else:
        analysis['feedback'].append("Add uppercase letters")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        analysis['score'] += 1
        analysis['has_lower'] = True
    else:
        analysis['feedback'].append("Add lowercase letters")
    
    # Check for digits
    if re.search(r'\d', password):
        analysis['score'] += 1
        analysis['has_digit'] = True
    else:
        analysis['feedback'].append("Add numbers")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        analysis['score'] += 1
        analysis['has_special'] = True
    else:
        analysis['feedback'].append("Add special characters")
    
    # Check for common patterns
    common_patterns = [
        r'12345',
        r'qwerty',
        r'password',
        r'admin',
        r'abc123'
    ]
    
    for pattern in common_patterns:
        if pattern.lower() in password.lower():
            analysis['score'] -= 1
            analysis['feedback'].append(f"Contains common pattern: {pattern}")
    
    # Calculate strength category
    if analysis['score'] <= 1:
        analysis['strength'] = 'Very Weak'
    elif analysis['score'] == 2:
        analysis['strength'] = 'Weak'
    elif analysis['score'] == 3:
        analysis['strength'] = 'Moderate'
    elif analysis['score'] == 4:
        analysis['strength'] = 'Strong'
    else:
        analysis['strength'] = 'Very Strong'
    
    return analysis

def print_password_analysis(analysis):
    """Print a formatted analysis of the password strength"""
    print("\nPassword Strength Analysis")
    print("-" * 25)
    print(f"Strength: {analysis['strength']}")
    print(f"Score: {analysis['score']}/6")
    print(f"Length: {analysis['length']} characters")
    print("\nCriteria Met:")
    print("✓ Uppercase letters" if analysis['has_upper'] else "✗ Missing uppercase letters")
    print("✓ Lowercase letters" if analysis['has_lower'] else "✗ Missing lowercase letters")
    print("✓ Numbers" if analysis['has_digit'] else "✗ Missing numbers")
    print("✓ Special characters" if analysis['has_special'] else "✗ Missing special characters")
    
    if analysis['feedback']:
        print("\nSuggestions for improvement:")
        for feedback in analysis['feedback']:
            print(f"- {feedback}")

            # Define some test passwords
passwords = [
    "password123",
    "jeffreydahmer",
    "mickeymouse123",
    "jamesbrown321",
    "despicableandmoana",
    "ricky-ann",
]

# Test each password
for pwd in passwords:
    print(f"Testing password: {pwd}")
    analysis = check_password_strength(pwd)
    print_password_analysis(analysis)
    print("\n" + "="*30 + "\n")
