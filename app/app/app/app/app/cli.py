import argparse
from .manager import TaskManager

def run():
    parser = argparse.ArgumentParser(description="To-Do CLI App")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title", type=str)

    # list
    subparsers.add_parser("list")

    # done
    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int)

    # delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add":
        manager.add(args.title)
    elif args.command == "list":
        manager.list()
    elif args.command == "done":
        manager.done(args.id)
    elif args.command == "delete":
        manager.delete(args.id)
    else:
        parser.print_help()
