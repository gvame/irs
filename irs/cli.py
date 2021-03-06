# Arguments
import argparse

# System
import sys
import os

# Powered by:
from .ripper import Ripper
from .utils import console, parse_default_flags
from .config import CONFIG

def main():
    parser = argparse.ArgumentParser()

    # Single Song
    parser.add_argument("-a", "--artist", dest="artist", help="Specify artist name. Must be used with -s/--song")
    parser.add_argument("-s", "--song",   dest="song",   help="Specify song name. Must be used with -a/--artist")

    # Album
    parser.add_argument("-A", "--album",    dest="album", help="Specify album name")

    # Playlist
    parser.add_argument("-u", "--username", dest="username", help="Specify username. Must be used with -p/--playlist")
    parser.add_argument("-p", "--playlist", dest="playlist", help="Specify playlist name. Must be used with -u/--username")

    # Post-Processors
    parser.add_argument("-l", "--location", dest="location", help="Specify a directory to place files in.")
    parser.add_argument("-o", "--organize", dest="organize", action="store_true", help="Organize downloaded files.")

    # Config
    parser.add_argument("-c", "--config", dest="config", action="store_true", help="Display path to config file.")


    args = parser.parse_args(parse_default_flags())

    if args.config:
        import irs
        print (os.path.dirname(irs.__file__) + "/config.py")
        sys.exit()


    ripper_args = {
        "post_processors": {
            "custom_directory": args.location,
            "organize": args.organize,
        }
    }

    ripper = Ripper(ripper_args)

    if args.artist and args.song:
        ripper.song(args.song, args.artist)
    elif args.album:
        ripper.spotify_list("album", args.album)
    elif args.username and args.playlist:
        ripper.spotify_list("playlist", args.playlist, args.username)
    else:
        console(ripper)

if __name__ == "__main__":
    main()