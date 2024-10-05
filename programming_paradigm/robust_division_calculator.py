def safe_divide(numerator, denominator):
    """
    Perform division, handling errors such as division by zero and non-numeric inputs.
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Perform the division and handle division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        else:
            result = num / denom
            return f"The result of the division is {result}"
    
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."