import base64
import os

from app.utils.constants import Constants


class Files:
    """
        Classe utilitária para trasformação de arquivos.
    """

    @staticmethod
    def create_folder_structure():
        """
            Cria a estrutura de pastas necessárias.

            Esta função cria as pastas especificadas na lista retornada pelo método `lista_pasta` da classe `Constantes`. Se a pasta não existir, ela será criada.
        """
        for constante in Constants().folder_list():
            if not os.path.exists(constante):
                os.makedirs(constante)

    @staticmethod
    def base64_to_file(base64_string, file_name):
        try:
            temp_file_path = os.path.join(Constants.TEMP_DIR_SELENIUM, file_name)
            file_bytes = base64.b64decode(base64_string)
            with open(temp_file_path, "wb") as file:
                file.write(file_bytes)
            return temp_file_path

        except Exception as e:
            print("Ocorreu um erro ao gerar o arquivo:", str(e))
            return None
