#!/usr/bin/python

api = 'https://api.github.com'

import argparse
import json
import logging
import os
from github import Github
import sys
from git import Repo
from tqdm import tqdm

LOG = logging.getLogger('repolist')


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--username', '-u')
    p.add_argument('--token', '-t')
    p.add_argument('--debug', '-d',
                   action='store_const',
                   const=logging.DEBUG,
                   dest='loglevel')

    p.set_defaults(loglevel=logging.INFO)
    return p.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(
        level=args.loglevel)
    reqlog = logging.getLogger('requests')
    reqlog.setLevel(logging.WARN)

    g = Github(args.token)

    user = g.get_user()
    repos = [repo for repo in user.get_repos(type='private') if args.username
in repo.full_name]

    for repo in tqdm(repos):
        name = repo.name
        full_name = repo.full_name
        path = os.path.abspath(os.path.join(os.path.join(os.getcwd(), os.pardir),
name))
        print(f"Cloning {name} from {full_name} to {path}")
        dir = os.listdir(path)
        if len(dir) == 0: 
            Repo.clone_from(f"https://{args.token}@github.com/{full_name}.git",
path)

if __name__ == '__main__':
    main()

