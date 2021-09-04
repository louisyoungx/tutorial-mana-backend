from django.core.files.storage import Storage
from webdav4.client import Client
from Django_Admin.settings import IMAGE_URL, IMAGE_FILE_PATH, IMAGE_WEBDAV_UPLOAD


class ImageStorage(Storage):
    '''Image文件存储类'''
    def __init__(self, client_conf=None, base_url=None):
        '''初始化'''
        self.client = Client(base_url=IMAGE_WEBDAV_UPLOAD, auth=('PhotoService', 'ImageHostingService'))
        # self.client.ls(path='/', detail=False)

    def _open(self, name, mode='rb'):
        '''打开文件'''
        pass

    def _save(self, name, content):
        '''保存文件'''
        # name:选择上传文件的名字
        # content:包含你上传文件内容的File对象

        # http://www.louisyoung.site:8089/photo/share/scUP9PKA#!List
        name = name.split('/')[1]
        to_path = IMAGE_FILE_PATH + name
        # save_path = BASE_DIR + '/media/' + name
        # file = open(save_path, "wb")  # 打开文件
        # file.write(content.read())
        # file.close()
        self.client.upload_fileobj(file_obj=content, to_path=to_path, overwrite=True)
        # self.client.upload_file(from_path=save_path, to_path=to_path, overwrite=True)
        return name

    def exists(self, name):
        '''Django判断文件名是否可用'''
        return False

    def url(self, name):
        path = IMAGE_URL + name
        return path