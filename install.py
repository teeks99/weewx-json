from setup import ExtensionInstaller

def loader():
    return JSON_Installer()

class JSON_Installer(ExtensionInstaller):
    def __init__(self):
        super(JSON_Installer, self).__init__(
            version="1.0",
            name='JSON',
            description='Add JSON output',
            author="Thomas Kent",
            author_email="https://github.com/teeks99/weewx-json",
            config={
                'StdReport': {
                    'JSONReport': {
                        'skin': 'JSON',
                        'enable': True
                    }
                }
            },
            files=[('skins/JSON', [
                'skins/JSON/current_minimal.json.tmpl',
                'skins/JSON/skin.conf',
                'skins/JSON/weewx.json.tmpl'
            ])]
        )
