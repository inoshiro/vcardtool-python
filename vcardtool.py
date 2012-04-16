# vim:fileencoding=utf-8
import sys
import os
import argparse
import vobject

def main():
    parser = make_parser()
    args = parser.parse_args()
    args.func(args)

def make_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_split = subparsers.add_parser('split', help='split vCard file')
    parser_split.add_argument('--file', required=True, help='vCard file')
    parser_split.add_argument('--dir', required=True, help='output directory')
    parser_split.set_defaults(func=sub_split)

    parser_list = subparsers.add_parser('list', help='list datas in vCard file')
    parser_list.add_argument('--file', required=True, help='vCard file')
    parser_list.set_defaults(func=sub_list)

    return parser

def sub_split(args):
    print "exec split"
    fname = args.file
    output = args.dir
    f = open(fname)
    for item in vobject.readComponents(f):
        write_file(item, output)
    f.close()

def sub_list(args):
    print 'exec list'
    fname = args.file
    f = open(fname)
    for item in vobject.readComponents(f):
        print_info(item)
    f.close()

def write_file(v, dirname):
    path = get_path(v, dirname)
    f = open(path, 'w')
    f.write(v.serialize())
    f.close()

def print_info(v):
    name = v.fn.value
    mail = v.email.value if hasattr(v, 'email') else ''
    print name + ' | ' + mail

def get_path(v, dirname):
    fname = v.fn.value.replace(' ', '_')
    return os.path.join(dirname, fname) + '.vcf'

def encode_name(v):
    if hasattr(v, 'CHARSET_param'):
        name = v.fn.value
    else:
        name = v.fn.value
    return name

if __name__ == '__main__':
    main()
