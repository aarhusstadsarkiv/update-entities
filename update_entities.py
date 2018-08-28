import json
import requests
import csv
import logging


DOMAIN = 'address'
ENTITIES_POST_URL = 'https://openaws.appspot.com/entity_tools'
TOKEN = ''


def main():

    def post_request():


    def update_values(json_encoded_string):
        values = json.loads(json_encoded_string)
        try:
            altas_idx = values.get('sources', []).index('Kommuneatlas')
            values['sources'][altas_idx] = '''
            '''
        except:
            print('"Kommuneatlas" not in sources-key')
        
        return values


    def create_entities_dict(csv_file):
        # convert to dict with eID's as keys and valuedicts as values
        with open(csv_file) as ifile:
            reader = csv.reader(ifile)
            reader.next()
            for line in reader:
                _id = line[0][2:]  # remove 'e#' from start of id-column
                
                try:
                    values = update_values(line[1])
                except Exception:
                    print("Unable to load string from id: " + _id)
                    continue

                schema = values.get('schema', '')
               
                return post_request(schema, 'update', _id, values)

    def post_request(schema, operation, _id, data):

        data["oaws_meta"] = {"id": _id, "schema_name": schema}

        oawsPostCall = {}
        oawsPostCall["token"] = TOKEN
        oawsPostCall["operation"] = operation
        oawsPostCall["data"] = json.dumps(data)

        try:
            response = oaws.oawsSimpleRequest(oawsEndPoint, oawsPostCall, "POST")
        except ValueError as err:
            print("oaws not updated")

if __name__ == '__main__':
    main()
