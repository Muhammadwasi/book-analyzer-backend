

def get_first_prompt_with_text(text: str) -> str:
    return """
    Given the following book content, identify characters and summarize their interactions with each other in JSON format like:
    {
        "character_interactions" : [
            {
                "character_name": "Romeo",
                "interacted_with": [
                    {
                        "name" : "Juliet",
                        "count": 23
                    },
                    {
                        "name" : "Mercutio",
                        "count": 23
                    },
                    {
                        "name" : "Friar",
                        "count": 23
                    }
                ],
                "total_interactions": 45
            },
            {
                "character_name": "Juliet",
                "interacted_with": [
                    {
                        "name" : "Romeo",
                        "count": 23
                    },
                    {
                        "name" : "Nurse",
                        "count": 23
                    },
                    {
                        "name" : "Lady Capulet",
                        "count": 23
                    }
                ],
                "total_interactions": 45
            },
            {
                "character_name": "Mercutio",
                "interacted_with": [
                    {
                        "name" : "Juliet",
                        "count": 23
                    },
                    {
                        "name" : "Mercutio",
                        "count": 23
                    },
                    {
                        "name" : "Friar",
                        "count": 23
                    }
                ]
                "total_interactions": 45
            }
        ]
    }
    Please note that the result will be ingested to the function which will take only json as input. Please don't input any content other than the specified JSON above.
    Here's the first chunk of the book:
    """ + text


def get_subsequent_prompt_with_text(text: str) -> str:
    return """
    Given the following book content, identify characters and summarize their interactions with each other in JSON format like:
    {
        "character_interactions" : [
            {
                "character_name": "Romeo",
                "interacted_with": [
                    {
                        "name" : "Juliet",
                        "count": 23
                    },
                    {
                        "name" : "Mercutio",
                        "count": 23
                    },
                    {
                        "name" : "Friar",
                        "count": 23
                    }
                ],
                "total_interactions": 45
            },
            {
                "character_name": "Juliet",
                "interacted_with": [
                    {
                        "name" : "Romeo",
                        "count": 23
                    },
                    {
                        "name" : "Nurse",
                        "count": 23
                    },
                    {
                        "name" : "Lady Capulet",
                        "count": 23
                    }
                ],
                "total_interactions": 45
            },
            {
                "character_name": "Mercutio",
                "interacted_with": [
                    {
                        "name" : "Juliet",
                        "count": 23
                    },
                    {
                        "name" : "Mercutio",
                        "count": 23
                    },
                    {
                        "name" : "Friar",
                        "count": 23
                    }
                ]
                "total_interactions": 45
            }
        ]
    }
    Please note that the result will be ingested to the function which will take only json as input. Please don't input any content other than the specified JSON above.
    Here's the remaining chunk of the book:
    """ + text
