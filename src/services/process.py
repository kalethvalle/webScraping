import json
import os

class ServiceProcess:
    def listProcess(self):
        path_to_json = os.path.join(os.path.dirname(__file__), '../collections/actors')
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

        data = []
        for index, js in enumerate(json_files):
            with open(os.path.join(path_to_json, js)) as json_file:
                json_text = json.load(json_file)
                data.append({
                    "id": js.split('.')[0],
                    "process": json_text
                })

        return data