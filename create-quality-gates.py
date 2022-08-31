from sonarqube import SonarQubeClient
import yaml

dict_quality_gates_already = {}
list_quality_created = []
sonar = SonarQubeClient(sonarqube_url="http://localhost:9001", username='admin', password='admin123')
def open_file_config ():
    with open('quality-gates.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

def update_condition_to_quality_gate():
    data = open_file_config()
    separator = ' '
    for quality_gates in (data['list-quality-gates']):
        name_quality_gates = separator.join(quality_gates.keys())
        id_conditions = search_id_conditions(name_quality_gates)
        value = quality_gates[name_quality_gates][0]['metric'][0]['value']
        operator = quality_gates[name_quality_gates][0]['metric'][1]['op']
        try:
            result = sonar.qualitygates.update_condition_to_quality_gate(id=id_conditions, metric="new_coverage", error=value, op=operator)
            print (result)
        except:
            print (name_quality_gates+" don't update !!")

def search_id_conditions(gatename):
    id_conditions = sonar.qualitygates.show_quality_gate(name=gatename)['conditions'][0]['id']
    return id_conditions

def search_id(gatename):
    id_gates = get_quality_gates_already()[gatename]
    return id_gates

def get_quality_gates_already():
    list_quality_gates_already = sonar.qualitygates.get_quality_gates()
    for quality_gates_already in list_quality_gates_already['qualitygates']:
        name_gates_already = quality_gates_already['name']
        id_gates_already = quality_gates_already['id']
        dict_quality_gates_already[name_gates_already] = id_gates_already
    return (dict_quality_gates_already)

def create_quality_gates():
    data = open_file_config()
    separator = ' '
    for quality_gates in data['list-quality-gates']:
        name_quality_gates = separator.join(quality_gates.keys())
        if name_quality_gates not in get_quality_gates_already():
            result = sonar.qualitygates.create_quality_gate(name=name_quality_gates)
            id = search_id(name_quality_gates)
            sonar.qualitygates.create_condition_to_quality_gate(gateId=id, metric="new_coverage", error="80", op="LT")

def update_quality_gates_created():
    data = open_file_config()
    separator = ' '
    list_quality_gates = data['list-quality-gates']
    for quality_gates_created in data['list-quality-gates']:
        name_quality_gates_created = separator.join(quality_gates_created.keys())
        list_quality_created.append(name_quality_gates_created)
    return list_quality_created

def delete_quality_gates():
    for quality_gates in get_quality_gates_already():
        if quality_gates not in update_quality_gates_created():
            result = sonar.qualitygates.delete_quality_gate(dict_quality_gates_already[quality_gates])
            print (result)
    
if __name__ == "__main__":
#    print (search_id_conditions())
#    print (search_id("qlg1"))

#    print (get_quality_gates_already())
    print (create_quality_gates())
    print (delete_quality_gates())
    print (update_condition_to_quality_gate())
