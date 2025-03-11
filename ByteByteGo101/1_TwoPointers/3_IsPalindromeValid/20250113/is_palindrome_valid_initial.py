# Time: O(n)
# Space: O(n)
def is_palindrome_valid(s: str) -> bool:
    s_alphanumeric = "".join(c for c in s if c.isalnum())
    return s_alphanumeric == s_alphanumeric[::-1]
