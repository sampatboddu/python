import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        dest="input",
        default="gs://dataflow-samples/shakespeare/kinglear.txt",
        help="takes input file")
    parser.add_argument(
        "--output",
        dest="output",
        default="gs://test-bucket-spn/output.txt",
        help="takes input file")

    # parsing all the args from command line
    args = parser.parse_args()
    print("Input file is ", args.input)
    print("Output file is ", args.output)

    # parsing and extracting only known args andignore other unknown args
    known_args, unknown = parser.parse_known_args()
    print("Input file is ", known_args.input)
    print("Output file is ", known_args.output)
