import sys

from challenge_factory import get_challenge

challenge_name = sys.argv[1]
challenge = get_challenge(challenge_name)
challenge.test_challenge()

