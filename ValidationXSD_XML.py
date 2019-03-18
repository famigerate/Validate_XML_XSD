from lxml import etree
from io import StringIO
import os
import json


class Validation:

    def __init__(self, xsd_path, xml_path):
        self.xsd_path = xsd_path
        self.xml_path = xml_path

    def validate(self):

        # open and read schema file
        with open(self.xsd_path, 'r') as schema_file:
            schema_to_check = schema_file.read()

        parser = etree.XMLParser(encoding='cp1251')
        xmlschema_doc = etree.parse(StringIO(schema_to_check[3:]), parser)
        xmlschema = etree.XMLSchema(xmlschema_doc)

        # parse xml
        try:
            doc = etree.parse(self.xml_path, parser)
        # check for file IO error
        except IOError:
            return 'Could not read file'

        # check for XML syntax errors
        except etree.XMLSyntaxError as err:
            with open('error_syntax.log', 'w') as error_log_file:
                error_log_file.write(str(err.error_log))
        except:
            return 'Could not read file'

        # validate against schema
        try:
            xmlschema.assertValid(doc)
            return ''
        except etree.DocumentInvalid as xsd_err:
            count = 0
            jsonarr = []
            for error in xmlschema.error_log:
                text = 'Filename: {} Error: {} Nubmer line : {}'.format(os.path.basename(self.xml_path),
                                                                              error.message,
                                                                              error.line)
                count += 1
                jsonObj = [
                    {'count': count, 'text': text, 'line': error.line, 'filename': os.path.basename(self.xml_path)}
                ]
                res = json.dumps(jsonObj, sort_keys=True, ensure_ascii=False)
                jsonarr.append(res)
            return jsonarr
        except:
            return 'Could not read file'
