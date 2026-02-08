import numpy as np
import re

# no guarantees this works as its supposed to
# should exclusively change the specified number
# regardless, input's only read, output separate to make sure no nonsense happens.

def main():
    with open('input.txt', 'r') as f:
        content = f.read()
    
    #define which number to replace
    try:
        target_number = float(input("Enter the number to replace: "))
    except ValueError:
        print("INVALID input. Enter a VALID number.")
        return
    
    #define max decimal places
    try:
        max_decimal_places = int(input("maximum decimal places? (for example 2 for 200.22): "))
        if max_decimal_places < 0:
            print("decimal places must be positive")
            return
    except ValueError:
        print("WRONG")
        return
    
    #create regex pattern to match the exact number (including decimals)
    pattern = r'(?<=\s)' + re.escape(str(target_number)) + r'(?=\s|$)'
    
    #find all occurrences of the target number
    matches = list(re.finditer(pattern, content))
    
    if not matches:
        print(f"Can't find {target_number} in the input.txt")
        return
    
    print(f"found {len(matches)} occurrence(s) of {target_number}")
    
    def replace_with_variance(match):
        original = float(match.group())
        lower_bound = original * 0.75
        upper_bound = original * 1.25
        
        new_value = np.random.uniform(lower_bound, upper_bound)
        
        formatted_value = f"{new_value:.{max_decimal_places}f}"
        
        if '.' in formatted_value:
            formatted_value = formatted_value.rstrip('0').rstrip('.')
        
        return formatted_value
    
    new_content = re.sub(pattern, replace_with_variance, content)
    
    with open('output.txt', 'w') as f:
        f.write(new_content)
    
    print("Finished. Results stored in output.txt.")

if __name__ == "__main__":
    main()