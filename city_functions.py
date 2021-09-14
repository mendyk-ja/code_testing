def get_city_country(city, country, population=''):
    """Generate elegantly formatted city and country name"""
    formatted_text = f"{city}, {country}"
    if population:
        return f"{formatted_text.title()} - population {population}"
    else:
        return formatted_text.title()
