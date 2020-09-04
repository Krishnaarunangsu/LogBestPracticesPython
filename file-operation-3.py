# file reading
class FileReaderDetails():
    def __init__(self):
        self.file = None

    def file_reader(self):
        """
        Read the complete file
        :return:
        """
        try:
            with open('data/dog_breeds.txt') as reader:
                try:
                    print(reader.read())
                except IOError as ie:
                    pr
                reader.close()
        except FileNotFoundError as fe:
            print(fe)

    def file_reader_part(self):
        """
        Read the some part of the file
        :return:
        """
        with open('data/dog_breeds.txt') as reader:
            print(reader.read(25))

    def file_reader_line(self):
        """
        Read the each line of the file character-wise
        :return:
        """
        with open('data/dog_breeds.txt') as reader:
            print(reader.readline(5))
            # Notice that line is greater than the 5 chars and continues
            # down the line, reading 5 chars each time until the end of the
            # line and then "wraps" around
            print(reader.readline(5))
            print(reader.readline(5))

    def file_reader_lines_list(self):
        """
        Read the entire file as a list
        :return:
        """
        with open('data/dog_breeds.txt') as reader:
            print(reader.readlines())

    def file_reader_lines_as_list(self):
        """
        Read the entire file as a list
        :return:
        """
        self.file = open('data/dog_breeds.txt', 'r')
        file_As_list = list(self.file)
        print(file_As_list)





file_reader_details = FileReaderDetails()
file_reader_details.file_reader()
print('***********************************')
file_reader_details.file_reader_part()
print('***********************************')
file_reader_details.file_reader_line()
print('***********************************')
file_reader_details.file_reader_lines_list()
print('***********************************')
file_reader_details.file_reader_lines_as_list()
