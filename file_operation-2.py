class FileHandling:
    """
    file operations
    """
    def __init__(self):
        """
        Initialization of file variable
        """
        self.file = None

    def file_read(self):
        """
        read the file in 'r' mode
        :return:
        """
        try:
            # file=None
            try:
                # self.file = open('data/data1.txt', 'r', encoding='utf-8')
                self.file = open('D:/Arunangsu/resources/test1.txt', 'r', encoding='utf-8')
                print(self.file)
            except FileNotFoundError as fe:
                print('{}'.format(fe))
            # Perform File Operations
            print(self.file.read())
        except IOError as ie:
            print('There is some issue with the file :{}'.format(ie))
        except:
            print('Some Unexpected Error has happened')
        finally:
            if self.file !=None:
                self.file.close()


file_handling = FileHandling()
file_handling.file_read()

