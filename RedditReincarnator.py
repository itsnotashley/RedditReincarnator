# RedditReincarnator - Transfer Reddit subs and saved items between accounts

import praw
import logging
from tqdm import tqdm
import time

OLD_ACCOUNT = {
    'client_id': 'your_old_client_id',
    'client_secret': 'your_old_secret',
    'username': 'your_old_username',
    'password': 'your_old_password',
    'user_agent': 'OldAccountScript'
}

NEW_ACCOUNT = {
    'client_id': 'your_new_client_id',
    'client_secret': 'your_new_secret',
    'username': 'your_new_username',
    'password': 'your_new_password',
    'user_agent': 'NewAccountScript'
}

LOG_FILE = 'reddit_transfer.log'

logging.basicConfig(
    filename=LOG_FILE,
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def login(account_info):
    return praw.Reddit(
        client_id=account_info['client_id'],
        client_secret=account_info['client_secret'],
        username=account_info['username'],
        password=account_info['password'],
        user_agent=account_info['user_agent']
    )

def transfer_subs(old_reddit, new_reddit):
    logging.info("Fetching subscribed subreddits...")
    subs = list(old_reddit.user.subreddits(limit=None))
    logging.info(f"Found {len(subs)} subreddits.")

    for sub in tqdm(subs, desc="Subscribing to subreddits"):
        try:
            new_reddit.subreddit(sub.display_name).subscribe()
            logging.info(f"Subscribed to r/{sub.display_name}")
        except Exception as e:
            logging.error(f"Failed to subscribe to r/{sub.display_name}: {e}")
        time.sleep(1)

def transfer_saved(old_reddit, new_reddit):
    logging.info("Fetching saved items...")
    saved_items = list(old_reddit.user.me().saved(limit=None))
    logging.info(f"Found {len(saved_items)} saved items.")

    for item in tqdm(saved_items, desc="Saving posts/comments"):
        try:
            if isinstance(item, praw.models.Comment):
                new_reddit.comment(item.id).save()
                logging.info(f"Saved comment: {item.id}")
            elif isinstance(item, praw.models.Submission):
                new_reddit.submission(item.id).save()
                logging.info(f"Saved post: {item.id}")
        except Exception as e:
            logging.error(f"Failed to save item {item.id}: {e}")
        time.sleep(1)

def main():
    print("🔑 Logging into old account...")
    old_reddit = login(OLD_ACCOUNT)
    print("✅ Old account logged in.")

    print("🔑 Logging into new account...")
    new_reddit = login(NEW_ACCOUNT)
    print("✅ New account logged in.")

    print("📦 Transferring subscriptions...")
    transfer_subs(old_reddit, new_reddit)

    print("📚 Transferring saved posts/comments...")
    transfer_saved(old_reddit, new_reddit)

    print(f"🎉 All done! Logs saved to {LOG_FILE}")

if __name__ == "__main__":
    main()
