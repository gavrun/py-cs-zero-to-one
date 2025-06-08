# 07_python_advanced/stdlib/standard_library_locale.py

# Python 'locale' module
# Locale-aware formatting of numbers, currency, strings, etc.

import locale

# Get/set current locale
default_locale = locale.getdefaultlocale()
print("System default locale:", default_locale)

# Set locale for all categories (LC_ALL)
locale.setlocale(locale.LC_ALL, '')  # system default (e.g., "en_US.UTF-8")

# OR explicitly:
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
# locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
# locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

# Format numbers according to locale
value = 1234567.89
formatted = locale.format_string("%.2f", value, grouping=True)
print("Formatted number:", formatted)

# Format currency
# (Note: not supported in all locales)
try:
    print("Currency:", locale.currency(value))
except Exception as e:
    print("Currency formatting failed:", e)

# Locale-aware sorting
names = ["Zoe", "Émile", "Åsa", "Anna"]

# Default sort (Unicode order)
print("Default sorted:", sorted(names))

# Locale-aware sort
sorted_locale = sorted(names, key=locale.strxfrm)
print("Locale-aware sorted:", sorted_locale)

# Locale categories
# LC_ALL        → affects all categories
# LC_NUMERIC    → number formatting
# LC_MONETARY   → currency formatting
# LC_TIME       → time/date formatting
# LC_COLLATE    → string comparison/sorting
# LC_CTYPE      → character classification

# Reset to default (C locale)
locale.setlocale(locale.LC_ALL, 'C')

# Useful functions
print("Decimal point symbol:", locale.localeconv()['decimal_point'])
print("Thousands separator:", locale.localeconv()['thousands_sep'])


# locale.getdefaultlocale()           → system's default
# locale.setlocale(LC_ALL, '...')     → change locale
# locale.format_string(fmt, val, grouping=True)
# locale.currency(val)                → currency string
# locale.strxfrm(s)                   → string key for locale-aware sorting
# locale.localeconv()                 → decimal and separator info
