from ruamel import yaml
import traceback
import logging

class Roles:
    def __init__(self, filePath):
        self.file = filePath
        self.roleNames = []
        self.roleIds = []

        self.load()

    def load(self):
        try:
            with open(self.file, 'r') as f:
                self.doc = yaml.load(f)
        except Exception as e:
            logging.error(traceback.format_exc())

        for role in self.doc['roles']:
            self.roleNames.append(role['name'])

            _ = {'name': role['name'],
                 'id':   role['id']}
            self.roleIds.append(_)

    def getRoleNames(self):
        return self.roleNames

    def getRoleIds(self):
        return self.roleIds

    def deleteRole(self, name):
        with open(self.file, 'r') as f:
            lines = f.readlines()
            f.close()

        with open(self.file, 'w') as f:
            for line in lines:
                if name not in line:
                    f.write(line)

    def addRole(self, name, id):
        try:
            with open(self.file, 'w') as f:
                template = """    {name}:
                        name: {name}
                        id: {id}"""

                info = {
                    'name': name,
                    'id': id
                }

                f.write(template.format(**info))
                self.load()
                return {'status': 'success', 'value': 'null'}

        except Exception as e:
            return {'status': 'fail',
                    'value': e}