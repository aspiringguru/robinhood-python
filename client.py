from pathlib import Path
import configparser

from robinhood.RobinhoodClient import RobinhoodClient

# Set up the client
client = RobinhoodClient()

# Get an auth token
config = configparser.ConfigParser()
config.read([str(Path.home() / '.robinhood' / 'credentials')])
client.set_auth_token_with_credentials(
  config['account']['RobinhoodUsername'],
  config['account']['RobinhoodPassword']
)

try:
  client.get_watchlist_instruments('Default')
finally:
  client.clear_auth_token()
