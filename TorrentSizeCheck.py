import os
import libtorrent as lt
import sys

def get_torrent_info(torrent_path):
    info = lt.torrent_info(torrent_path)
    size_mb = info.total_size() / (1024 * 1024)  # convert bytes to MB
    size_gb = size_mb / 1024  # convert MB to GB
    return size_mb, size_gb

def main(path):
    total_size_mb = 0
    total_size_gb = 0

    if os.path.isfile(path) and path.endswith(".torrent"):
        paths = [path]
    elif os.path.isdir(path):
        paths = [os.path.join(path, filename) for filename in os.listdir(path) if filename.endswith(".torrent")]
    else:
        print("Path is neither a .torrent file nor a directory")
        sys.exit(1)

    for torrent_path in paths:
        try:
            size_mb, size_gb = get_torrent_info(torrent_path)
            total_size_mb += size_mb
            total_size_gb += size_gb
            print(f"Torrent size ({os.path.basename(torrent_path)}): {size_mb:.2f} MB ~ {size_gb:.2f} GB")
        except:
            print(f"Error reading file: {os.path.basename(torrent_path)}")
    
    print(f"Total size of all torrents: {total_size_mb:.2f} MB ~ {total_size_gb:.2f} GB")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path>")
        sys.exit(1)
    main(sys.argv[1])
