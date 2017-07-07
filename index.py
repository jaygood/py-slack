import os
import time
from slackclient import SlackClient

AT_BOT = '<@' + os.environ['BOT_ID'] + '>'
EXAMPLE_COMMAND = 'do'

slack_client = SlackClient(os.environ['SLACK_BOT_TOKEN'])

def handle_command(command, channel):
  response = 'Use the *' + EXAMPLE_COMMAND + '* command'
  if command.startswith(EXAMPLE_COMMAND):
    response = 'give me a sec'
  slack_client.api_call('chat.postMessage', channel=channel, text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
  output_list = slack_rtm_output
  if output_list and len(output_list) > 0:
    for output in output_list:
      if output and 'text' in output and AT_BOT in output['text']:
        return output['text'].split(AT_BOT)[1].strip().lower(), output['channel']

  return None, None


if __name__ == '__main__':
  READ_WEBSOCKET_DELAY = 10
  if slack_client.rtm_connect():
    print('connectd and runnin')
    while True:
      command, channel = parse_slack_output(slack_client.rtm_read())
      if command and channel:
        handle_command(command, channel)
      time.sleep(READ_WEBSOCKET_DELAY)
  else:
    print('connect failed')
