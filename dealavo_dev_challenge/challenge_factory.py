import os
from utils import get_input_to_output_filenames_map

from dealavo_dev_challenge.challenge_1.solution import Challenge_1
from dealavo_dev_challenge.challenge_2.challenge_2_sol import Challenge_2
from dealavo_dev_challenge.challenge_3.solution import Challenge_3
from dealavo_dev_challenge.challenge_4.solution import Challenge_4
from dealavo_dev_challenge.challenge_5.solution import Challenge_5
from dealavo_dev_challenge.challenge_6.solution import Challenge_6
from dealavo_dev_challenge.challenge_7.solution import Challenge_7
from dealavo_dev_challenge.challenge_8.solution import Challenge_8
from dealavo_dev_challenge.challenge_9.solution import Challenge_9
from dealavo_dev_challenge.challenge_10.solution import Challenge_10


def get_challenge(challenge_name):
    dirpath_in = os.path.join(os.path.curdir, challenge_name, 'in')
    dirpath_out = os.path.join(os.path.curdir, challenge_name, 'out')
    input_filenames = [os.path.join(dirpath_in, filename) for filename in os.listdir(dirpath_in)]
    output_filenames = [os.path.join(dirpath_out, filename) for filename in os.listdir(dirpath_out)]
    return names_to_objects[challenge_name](get_input_to_output_filenames_map(input_filenames, output_filenames))


names_to_objects = {
    'challenge_1': Challenge_1,
    'challenge_2': Challenge_2,
    'challenge_3': Challenge_3,
    'challenge_4': Challenge_4,
    'challenge_5': Challenge_5,
    'challenge_6': Challenge_6,
    'challenge_7': Challenge_7,
    'challenge_8': Challenge_8,
    'challenge_9': Challenge_9,
    'challenge_10': Challenge_10,
}