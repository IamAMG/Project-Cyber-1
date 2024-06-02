import re

def check_password_complexity(password):

    #Defining criteria for determining the strength of the password
    
    length_criteria = len(password) >= 10
    uppercase_criteria = bool(re.search(r'[A-Z]',password))
    lowercase_criteria = bool(re.search(r'[a-z]',password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%&*(),.:{}<>]', password))


    # Assessment of  the strength of the password based on the criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong password! "

    else:
        feedback = "Weak password. Consider the following improvements:\n"
        if not length_criteria:
            feedback += "- Ensure the password is at least 10 characters long\n"
        if not uppercase_criteria:
            feedback += "- Include at least one uppercase letter\n"
        if not lowercase_criteria:
            feedback += "- Include at least one lowercase letter\n"
        if not digit_criteria:
            feedback += "- Include at least one digit\n"
        if not special_char_criteria:
            feedback += "- Include at least one special character (!@#$%&*(),.:{}<>)\n"

        return feedback


def main():
    print("Password Complexity Checker")

    # Get input from the user for Password
    password = input("Enter your password: ")

    # Checking and providing feedback after checking the complexity of the Password
    result = check_password_complexity(password)
    print(result)

if __name__ == "__main__":
    main()


        
        
      
