# This is a medium severity, medium confidence issue
# Use of possibly insecure function - consider using safer ast.literal_eval.
def execute_code(code):
    eval(code)  # Medium confidence

user_input = "print('Executing untrusted code')"
execute_code(user_input)
