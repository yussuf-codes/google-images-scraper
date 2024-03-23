from argparse import ArgumentParser
from google_images_scraper import ScrapeImages


def main():
    parser = ArgumentParser()

    parser.add_argument("-q", "--qry", type=str)
    parser.add_argument("-n", "--num", type=int)
    parser.add_argument("-d", "--dir", type=str)

    args = parser.parse_args()

    ScrapeImages(args.qry, args.num, args.dir)


if __name__ == "__main__":
    main()
