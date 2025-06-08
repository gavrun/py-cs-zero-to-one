# 07_python_advanced/exceptions_hierarchy.py

# Defining custom exception classes in a clear hierarchy

# Helps organize complex systems with specific types of errors

class ApplicationError(Exception):
    """Base class for all application-specific errors."""
    pass

class AuthError(ApplicationError):
    """Raised when authentication fails."""
    pass

class PermissionError(ApplicationError):
    """Raised when a user is authenticated but not authorized."""
    pass

def authenticate(user):
    # Simulate a basic authentication check
    if user != "admin":
        raise AuthError("User not recognized")

try:
    authenticate("guest")
except ApplicationError as e:
    # Catch any application-related error in one place
    print("Application error:", type(e).__name__, "-", e)

