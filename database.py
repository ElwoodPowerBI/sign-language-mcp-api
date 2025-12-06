"""
Sign Language Database
Educational project demonstrating API concepts for MCP integration

This module contains sign language descriptions for basic words across multiple sign languages.
It serves as an in-memory database for the educational API.
"""

# Supported sign languages mapping
SUPPORTED_LANGUAGES = {
    "auslan": "Australian Sign Language",
    "jsl": "Japanese Sign Language",
    "is": "International Sign"
}

# Main sign language database
# Structure: word -> language_code -> sign details
SIGN_DATABASE = {
    "hello": {
        "auslan": {
            "language_full": "Australian Sign Language",
            "description": "Open hand, palm facing outward, placed near the side of the forehead. Move the hand outward in a small arc away from the head.",
            "handshape": "Open hand with fingers together",
            "movement": "Small arc outward from forehead",
            "facial_expression": "Friendly smile"
        },
        "jsl": {
            "language_full": "Japanese Sign Language",
            "description": "Bow slightly while bringing both open hands together in front of chest, palms facing each other, then move hands apart while bowing.",
            "handshape": "Both hands open, palms facing each other",
            "movement": "Hands come together then move apart during bow",
            "facial_expression": "Respectful expression with slight bow"
        },
        "is": {
            "language_full": "International Sign",
            "description": "Wave with open hand, palm facing outward, fingers spread slightly. Move hand side to side near shoulder level.",
            "handshape": "Open hand, fingers slightly spread",
            "movement": "Side to side waving motion at shoulder level",
            "facial_expression": "Warm, welcoming smile"
        }
    },
    "thank_you": {
        "auslan": {
            "language_full": "Australian Sign Language",
            "description": "Flat hand starts at chin, palm facing body. Move hand forward and slightly downward, as if blowing a kiss of gratitude.",
            "handshape": "Flat hand, fingers together",
            "movement": "Forward and downward from chin",
            "facial_expression": "Grateful smile"
        },
        "jsl": {
            "language_full": "Japanese Sign Language",
            "description": "One hand in a fist with thumb extended upward, bring it down in front of chest while slightly bowing head.",
            "handshape": "Fist with thumb up",
            "movement": "Downward motion in front of chest",
            "facial_expression": "Thankful expression with slight bow"
        },
        "is": {
            "language_full": "International Sign",
            "description": "Flat hand touches lips/chin, then moves forward and down toward the person being thanked.",
            "handshape": "Flat hand, fingers together",
            "movement": "From lips/chin forward and down",
            "facial_expression": "Sincere, grateful expression"
        }
    },
    "please": {
        "auslan": {
            "language_full": "Australian Sign Language",
            "description": "Open hand placed on chest, make a circular rubbing motion over the heart area.",
            "handshape": "Open hand, palm against chest",
            "movement": "Circular rubbing motion over heart",
            "facial_expression": "Polite, requesting expression"
        },
        "jsl": {
            "language_full": "Japanese Sign Language",
            "description": "Both hands together in prayer position in front of chest, slight bow of the head.",
            "handshape": "Both hands in prayer position",
            "movement": "Held steady with slight head bow",
            "facial_expression": "Respectful, requesting expression"
        },
        "is": {
            "language_full": "International Sign",
            "description": "Flat hand on chest, circular motion similar to many national sign languages.",
            "handshape": "Flat hand on chest",
            "movement": "Circular motion over chest area",
            "facial_expression": "Polite expression"
        }
    },
    "sorry": {
        "auslan": {
            "language_full": "Australian Sign Language",
            "description": "Closed fist placed on chest, make circular rubbing motion over the heart to show remorse.",
            "handshape": "Closed fist",
            "movement": "Circular rubbing motion over heart",
            "facial_expression": "Apologetic, remorseful expression"
        },
        "jsl": {
            "language_full": "Japanese Sign Language",
            "description": "Both hands together in prayer position, bow head more deeply than for 'please'.",
            "handshape": "Both hands in prayer position",
            "movement": "Held steady with deep head bow",
            "facial_expression": "Very apologetic expression with deeper bow"
        },
        "is": {
            "language_full": "International Sign",
            "description": "Fist or flat hand on chest with circular motion, combined with apologetic facial expression.",
            "handshape": "Fist or flat hand on chest",
            "movement": "Circular motion over chest/heart",
            "facial_expression": "Apologetic, regretful expression"
        }
    },
    "help": {
        "auslan": {
            "language_full": "Australian Sign Language",
            "description": "Dominant hand in thumbs-up position, place on open palm of non-dominant hand. Lift both hands upward together.",
            "handshape": "Thumbs-up on flat palm",
            "movement": "Both hands lift upward together",
            "facial_expression": "Concerned or seeking expression"
        },
        "jsl": {
            "language_full": "Japanese Sign Language",
            "description": "One flat hand supports the elbow of the other arm, which has an open hand reaching upward.",
            "handshape": "One flat support hand, one open reaching hand",
            "movement": "Reaching hand extends upward while supported",
            "facial_expression": "Seeking assistance expression"
        },
        "is": {
            "language_full": "International Sign",
            "description": "Thumbs-up hand placed on flat palm of other hand, both hands move upward together.",
            "handshape": "Thumbs-up on flat palm",
            "movement": "Both hands move upward in unison",
            "facial_expression": "Requesting help expression"
        }
    }
}


def get_all_words():
    """
    Returns a list of all words available in the database.
    
    Returns:
        list: Sorted list of word strings
    """
    return sorted(list(SIGN_DATABASE.keys()))


def get_all_languages():
    """
    Returns the dictionary of supported sign languages.
    
    Returns:
        dict: Dictionary mapping language codes to full names
    """
    return SUPPORTED_LANGUAGES


def get_sign(word, language=None):
    """
    Retrieve sign language data for a specific word.
    
    Args:
        word (str): The word to look up
        language (str, optional): Specific language code. If None, returns all languages.
    
    Returns:
        dict or None: Sign data if found, None otherwise
        
    Examples:
        >>> get_sign("hello")  # Returns all languages for "hello"
        >>> get_sign("hello", "auslan")  # Returns only Auslan for "hello"
    """
    # Check if word exists in database
    if word not in SIGN_DATABASE:
        return None
    
    # If no specific language requested, return all languages for this word
    if language is None:
        return SIGN_DATABASE[word]
    
    # Check if specific language exists for this word
    if language not in SIGN_DATABASE[word]:
        return None
    
    # Return specific language data
    return {language: SIGN_DATABASE[word][language]}
