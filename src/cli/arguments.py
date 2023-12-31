import argparse
import uuid

from logger.logger import logger


def get_arguments():
    # Use the argparse module to handle command line arguments.
    parser = argparse.ArgumentParser(description='Process some integers.')

    # Add arguments with defaults.
    parser.add_argument('--user_id', type=str, default=str(uuid.uuid4()), help='User ID')
    parser.add_argument('--app_id', type=str, default=str(uuid.uuid4()), help='App ID')
    parser.add_argument(
        '--step', '-s',
        choices=['clarify', 'specification', 'development', 'execution'],
        type=str,
        default=None,
        help='Step'
    )

    # Parse the arguments.
    args = parser.parse_args()

    logger.info(f"If you wish to continue with this project in future run 'python main.py --app_id {args.app_id}'")
    return vars(args)
