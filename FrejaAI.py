import random
import openai
import brain2
from colorama import Fore, Back, Style
import time


# Your OpenAI API key
openai.api_key = "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"

# Array of tweets to feed to GPT-3.5
tweets = brain2.brain

for x in range(10):
    # Prevent rate limiting
    time.sleep(1)

    # Randomly select 20% of the tweets
    num_tweets_to_select = round(len(tweets) * 0.08)
    selected_tweets = random.sample(tweets, num_tweets_to_select)

    # Concatenate selected tweets into a single string
    tweet_text = "\n".join(selected_tweets)

    # Generate new tweet with GPT-3.5
    prompt = f"Generate a new short sentence based on these sentences: {tweet_text}\n\nNew sentence:"
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated tweet from the response
    generated_tweet = response.choices[0].text.strip()

    # Print the generated tweet
    print((Style.BRIGHT + Fore.GREEN + "FrejaAI: " +
           Style.RESET_ALL + generated_tweet))
    print(" ")
