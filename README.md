# RedditReincarnator 👻

[![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/github/license/itsnotashley/RedditReincarnator)](LICENSE)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Status](https://img.shields.io/badge/status-alpha-orange)

**Rise again on Reddit.**

RedditReincarnator helps you migrate your Reddit presence from one account to another. Whether you've been shadowbanned or you're just starting fresh - this tool brings your subs and saved content back to life.

## Features

✅ Transfer all subreddit subscriptions  
✅ Transfer saved posts and comments  
✅ Progress bars and detailed logs  
✅ Works cross-platform (Windows, macOS, Linux)

## Install

```bash
pip install -r requirements.txt
```

## Setup

Edit `RedditReincarnator.py` and insert your Reddit API credentials under:

```python
OLD_ACCOUNT = { ... }
NEW_ACCOUNT = { ... }
```

Create Reddit API apps at: https://www.reddit.com/prefs/apps (type = "script")

## Usage

```bash
python RedditReincarnator.py
```

## License

MIT - spooky stuff, do what you want.
