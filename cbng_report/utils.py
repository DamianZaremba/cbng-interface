from random import random

from cbng_report.models import ClusterNode, Reports
import socket
import logging

logger = logging.getLogger(__name__)

def get_node(type):
    '''
    Returns the node for a cluster type
    :param type: (String) type of node to get
    :return: (String) value of node
    '''
    try:
        return ClusterNode.objects.get(type=type).node
    except ClusterNode.DoesNotExist:
        return None


def send_msg_to_relay(message):
    '''
    Send a message to the relay node
    :param message: (String) message to send
    :return: None
    '''
    if len(message) > 400:
        message = '%s [...]' % message[0:394]

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.sendto(message, (get_node('relay'), 3333))
    except Exception, e:
        logger.exception('Failed to send message to relay', e)
    finally:
        s.close()


def get_next_report(user):
    '''
    Generate the next report ID for a user
    :param user: User to generate a report ID for
    :return: (Integer) id or None
    '''
    try:
        reports = Reports.objects.filter(status=0).order_by('-timestamp')[0:50]
        r = random(0, len(reports))
        return reports[r]
    except Exception, e:
        logger.exception('Failed to get the next report for user %d' % user.id, e)
    return None