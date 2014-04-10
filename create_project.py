#! /usr/bin/env python

import argparse, os
from string import Template

git_root_dir = '/home/git'

cmd_tmpl = Template(
'''
pushd $home
mkdir $name
cd $name
git --bare init
popd
echo git@cris:$home/$name
'''
)


def get_cmd(home, name):
    return cmd_tmpl.substitute(home=home, name=name)


def execute_cmd(cmd_str):
    cmds = cmd_str.split('\n')
    for cmd in cmds:
        if cmd:
            # print cmd
            os.popen2(cmd)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creating a git project')
    parser.add_argument('name', help='project name')
    parser.add_argument('-dir', help='project root dir', default=git_root_dir)
    args = parser.parse_args()
    cmd_str = get_cmd(args.dir, args.name + '.git')
    execute_cmd(cmd_str)