DEBUG = True
SERVICE_NAME = 'TenyksLol'
SERVICE_VERSION = '0.1.0'
SERVICE_UUID = '419e9fce-a75d-4954-b652-00931cd8e97a'
SERVICE_DESCRIPTION = 'A celebration of what it means to truly laugh'

##############################################################################
# The following setting defines a dictionary containing Redis connection
# information used when connecting to the Redis server.
#
# This setting is required.

REDIS_CONNECTION = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'password': None,
}
##############################################################################


##############################################################################
# The following channel settings are for when you need to change the default
# Redis channel key for each pipe respectively. BROADCAST_SERVICE_CHANNEL
# is used for messages going from Tenyks to Redis for the clients.
# BROADCAST_ROBOT_CHANNEL is used for messages going from clients to Tenyks
# for IRC.
#
# These are namespaced, so you shouldn't need to change them.
#
# These settings are optional

BROADCAST_SERVICE_CHANNEL = 'tenyks.service.broadcast'
BROADCAST_ROBOT_CHANNEL = 'tenyks.robot.broadcast'
##############################################################################