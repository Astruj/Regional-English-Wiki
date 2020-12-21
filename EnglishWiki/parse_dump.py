import wiki_dump_parser as parser


# this function reads the XML dump of wikipedia and outputs the processed data in a CSV file
def parse_dump(file_path):
    parser.xml_to_csv(file_path)
