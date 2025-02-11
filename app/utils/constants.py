import tempfile


class Constants:

    TEMP_DIR = tempfile.gettempdir()
    ROOT_FOLDER = 'resources/'
    LOG = f'{ROOT_FOLDER}logs/'
    DOWNLOAD_SP = '/documentos_gcpj/'

    def folder_list(self) -> tuple:
        return (self.LOG,)
