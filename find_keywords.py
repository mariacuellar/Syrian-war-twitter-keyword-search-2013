import sys,json,re,csv
from collections import defaultdict as dd

# Create the .csv file that will include the observations containing key words. Only 'text', 'coordinates', and 'created_at' are included for now.
with open('00positives.csv', 'a') as csvfile:
    awriter = csv.writer(csvfile, delimiter='\t',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    awriter.writerow(['text'] + ['coordinates'] + ['created_at'])


def count_terms(all_tweets,terms):
  term_counts = dd(int) # Dictionary object containing word counts
	pattern = re.compile('[^ 0-9a-zA-Z@]+#') # Only keep these characters

	for line in all_tweets.readlines(): # Loop through tweets
		a_tweet = json.loads(line)
		if a_tweet.has_key('text'): # Make sure the tweet has text values
			tweet_text = pattern.sub('', a_tweet['text'].encode('utf-8').lower()) # Encode to utf-8 and remove special characters
			for word in terms:
				result = re.findall(word,tweet_text)
				if result:
					term_counts[word] += len(result) # Increment dictionary object
					with open('00positives.csv', 'a') as csvfile: # Include observation in .csv file if it contains terms
                                            awriter = csv.writer(csvfile, delimiter='\t',
                                                                 quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                            awriter.writerow([tweet_text] + [a_tweet['coordinates']] + [a_tweet['created_at']])
	for key in terms:
		print key,term_counts[key] # Prints the number of times the term is included in the Twitter sample


def main():
    tweet_file = open(sys.argv[1])
    terms = ['syria','assad','damascus','homs','aleppo']
    count_terms(tweet_file,terms)

if __name__ == '__main__':
    main()
