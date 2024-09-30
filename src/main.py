from argparse import ArgumentParser
from google_images_scraper import scrape_images


def main() -> None:
    parser = ArgumentParser()

    parser.add_argument("-q", "--qry", type=str)
    parser.add_argument("-n", "--num", type=int)
    parser.add_argument("-d", "--dir", type=str)

    args = parser.parse_args()

    scrape_images(args.qry, args.num, args.dir)


if __name__ == "__main__":
    main()
