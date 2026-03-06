```python
import re
from urllib.parse import urlparse, parse_qs

def validate_redirect_url(redirect_url):
    """
    Validates a redirect URL to ensure it is safe and does not lead to external sites.
    
    Args:
        redirect_url (str): The URL to validate.
    
    Returns:
        bool: True if the URL is safe, False otherwise.
    """
    # Define a regular expression pattern to match allowed domains
    allowed_domains = ['example.com', 'example.org']
    pattern = re.compile(r'^https?://(?:www\.)?({})$'.format('|'.join(map(re.escape, allowed_domains))))
    
    # Check if the URL matches the allowed domains
    if pattern.match(redirect_url):
        return True
    
    # Parse the URL to check for any potentially dangerous query parameters
    parsed_url = urlparse(redirect_url)
    if parsed_url.netloc not in allowed_domains:
        return False
    
    query_params = parse_qs(parsed_url.query)
    dangerous_params = ['redirect','redirect_to', 'url']
    for param in dangerous_params:
        if param in query_params:
            return False
    
    return True
```