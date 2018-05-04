from functools import partial, update_wrapper
from decimal import Decimal

from bounties import settings
from std_bounties.bounty_client import BountyClient
from std_bounties.client_helpers import bounty_url_for, apply_and_notify, apply_and_notify_test, formatted_fulfillment_amount, token_price, format_deadline, usd_price, token_lock_price
from std_bounties.models import Bounty
from utils.functional_tools import merge, narrower, wrapped_partial

from slackclient import SlackClient


bounty_client = BountyClient()
sc = SlackClient(settings.SLACK_TOKEN)


class SlackMessageClient:

    def __init__(self):
        pass

    def bounty_issued(bounty_id, **kwargs):

    def bounty_activated(bounty_id, **kwargs):

    def bounty_fulfilled(bounty_id, **kwargs):

    def fulfillment_updated(bounty_id, **kwargs):

    def fulfillment_accepted(bounty_id, **kwargs):

    def bounty_killed(bounty_id, **kwargs):

    def contribution_added(bounty_id, **kwargs):

    def deadline_extended(bounty_id, **kwargs):

    def bounty_changed(bounty_id, **kwargs):

    def issuer_transferred(bounty_id, **kwargs):

    def payout_increased(bounty_id, **kwargs):

