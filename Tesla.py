"""
  Let’s say we need to integrate yet another electric vehicle API to our backend and we have decided that to be Tesla (all hail to Elon). The end goal is to optimise vehicle’s charging schedules and when it is the right time, either start or stop charging in order to ensure that each morning we can provide the owner a fully charged vehicle. 


Please investigate the possibilities of integrating Tesla, familiarise yourself with available data and access methods. 
"""


# Describe the technologies the OEM has used
# 1) If I understand the question correctly, using the tesla Api, one can easily achieve
# the much need integration by providing an avenue for users to input their client keys
# Another approach would be using already existing libraries for the tesla integration.

# 2) With the tesla with api available one can build their own library to consume the api that way.
# ) Yes, existing libraries can be reused but one can only do as much as the library permits.

# (Honestly this is a wild guess)My approach to writing the integration service would be
# first - to use OAuth2Service to securely authenticate the Tesla user
# second - use RabbitMQ to transfer power between the tesla and the power source


# the hard parts will be the transfer of energy between the connected tesla and the power source

# One major risk would be security loop holes maybe as power is being transferrrd.

# I have no idea how long It would take. a couple of months maybe.
