# Domain Searcher

A simple Python script to check the availability of .com domains in bulk.

## How it works

This script takes a list of domain names (without the .com extension) and checks their availability using WHOIS lookups. It will tell you which domains are available and which are already taken.

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Create a `domains.txt` file in the project directory
2. Add your desired domain names, one per line (without the .com extension):
   ```
   myawesomesite
   cooldomain
   bestproject
   ```
3. Run the script:
   ```bash
   python domain_searcher.py
   ```

The script will check each domain and display:
- Real-time status as it checks each domain
- A summary of all available domains at the end (in uppercase)

## Example Output

```
myawesomesite.com is already taken.
cooldomain.com is available!
bestproject.com is already taken.

Available domains:
COOLDOMAIN.COM
```

## Requirements

- Python 3.6+
- Dependencies listed in `requirements.txt`

## Note

This script uses WHOIS lookups which can be rate-limited by some registrars. If you're checking a large number of domains, consider adding delays between requests.
