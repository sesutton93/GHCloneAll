#!/usr/bin/python

api = 'https://api.github.com'

import argparse
import json
import logging
import os
from github import Github
import sys



LOG = logging.getLogger('repolist')


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--username', '-u')
    p.add_argument('--password', '-p')
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
    if args.token:
        g = Github(args.token)
    else:
        g = Github(args.username, args.password)
    user = g.get_user()
    repos = [repo for repo in user.get_repos(type='private')]

    for repo in repos:
        print(repo.clone_url)



if __name__ == '__main__':
    main()

