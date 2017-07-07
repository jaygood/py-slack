import os
from slackclient import SlackClient

BOT_NAME = 'something'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == '__main__':
  api_call = slack_client.api_call('users.list')
  if api_call.get('ok'):
    users = api_call.get('members')
    for user in users:
      if 'name' in user:
        print(user.get('name'))
      if 'name' in user and user.get('name') == BOT_NAME:
        print('found ' + user.get('id'))

  else:
    print('nada')