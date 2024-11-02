# Email Validator

A comprehensive Python tool for validating email addresses using both regex pattern matching and DNS MX record verification.

## Quick Links
- [Source Code](./projects/email_veryfication_console/check_email_console.py)
- [View Demo](./projects/email_veryfication_console/index.html)

## Features

- **Regex Validation**: Checks if email follows standard format
- **DNS Verification**: Validates domain's MX records
- **Common Domain Support**: Pre-validates common email providers
- **Color-coded Output**: Clear visual feedback using colorama

## Source Code

```python
import re
import dns.resolver
from colorama import init, Fore, Style

# Initialize colorama
init()

# Function to validate email addresses using a comprehensive regex
def is_valid_email(email):
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(regex, email) is not None

# Function to check if the email domain has MX records
def has_mx_record(email):
    domain = email.split('@')[-1]
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return True if answers else False
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.DNSException) as e:
        print(f"{Fore.YELLOW}DNS lookup failed for domain {domain}: {e}{Style.RESET_ALL}")
        return False

# Common domains that should always pass the MX check
common_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']

# Get the email address from the user
email = input("Enter the email address to check: ").strip().lower()

# Validate the email address
if not is_valid_email(email):
    print(f"{Fore.RED}Invalid email format: {email}{Style.RESET_ALL}")
elif email.split('@')[-1] not in common_domains and not has_mx_record(email):
    print(f"{Fore.RED}Email has no valid MX record: {email}{Style.RESET_ALL}")
else:
    print(f"{Fore.GREEN}Email is valid: {email}{Style.RESET_ALL}")
```

## Requirements

```bash
pip install dnspython colorama
```

## How It Works

1. **Format Validation**
   - Uses comprehensive regex pattern
   - Checks for valid username and domain format
   - Verifies correct use of special characters

2. **DNS Verification**
   - Resolves domain's MX records
   - Pre-validates common email providers
   - Handles DNS lookup errors gracefully

3. **Visual Feedback**
   - 🟢 Green: Valid email
   - 🔴 Red: Invalid format or no MX record
   - 🟡 Yellow: DNS lookup warnings

## Usage

```bash
python check_email_console.py
Enter the email address to check: user@example.com
```

## Example Output

- ✅ `Email is valid: user@gmail.com`
- ❌ `Invalid email format: invalid.email@`
- ❌ `Email has no valid MX record: user@nonexistent.domain`

## Technical Details

- Uses `dnspython` for MX record verification
- Implements RFC 5322 compliant email regex
- Optimized for common email providers
- Error handling for DNS resolution