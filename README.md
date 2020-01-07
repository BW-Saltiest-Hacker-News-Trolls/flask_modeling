Flask app currently deployed at: https://flask-modeling.herokuapp.com/item?id=10340094

Wraps https://hacker-news.firebaseio.com/v0/item/10340094.json, removing html escape sequences & tags 
and adding prob_offensive (rating from [profanity-check](https://pypi.org/project/profanity-check/)) 
and custom_pred (a homebrew neural network rating of probable comment toxicity) to the returned fields.

Takes a Hacker News item id as input. Returns a server error if the item text is missing or the id is 
invalid.
