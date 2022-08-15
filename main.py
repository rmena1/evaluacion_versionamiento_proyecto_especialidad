import json

def main():
    print('Top 10 retweeted tweets:')
    top_10_retweeted = top_retweeted_tweets()
    for item in top_10_retweeted:
        print(item['content'])
        print(item['retweetCount'])
        print()
        
    print()
    print('Top 10 users with most tweets:')
    top_10_users = top_user_tweets()
    for item in top_10_users:
        print(item['user'])
        print(item['tweets'])
        print()


def import_json():
    contents = open('farmers-protest-tweets-2021-03-5.json', "r").read() 
    data = [json.loads(str(item)) for item in contents.strip().split('\n')]
    return data

def top_retweeted_tweets():
    json = import_json()
    top_retweeted = []
    for item in json:
        if len(top_retweeted) < 10:
            top_retweeted.append(item)
        else:
            for tweet in top_retweeted:
                if item['retweetCount'] > tweet['retweetCount']:
                    top_retweeted.remove(tweet)
                    top_retweeted.append(item)
                    top_retweeted.sort(key=lambda x: x['retweetCount'], reverse=False)
                    break
    top_retweeted.sort(key=lambda x: x['retweetCount'], reverse=True)
    return top_retweeted

def top_user_tweets():
    # return list with top 10 users with most tweets
    json = import_json()
    top_users = []
    for item in json:
        found = False
        for user in top_users:
            if item['user']['username'] == user['user']:
                user['tweets'] += 1
                found = True
                break
        if not found:
            top_users.append({'user': item['user']['username'], 'tweets': 1})
    top_users.sort(key=lambda x: x['tweets'], reverse=True)
    #return first 10 users with most tweets
    return top_users[:10]

def top_tweeted_days():
    pass

def top_used_hashtags():
    pass

if __name__ == '__main__':
    main()
