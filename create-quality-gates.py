from sonarqube import SonarQubeClient
import yaml

Dict_Quality_Gates_Already = {}
List_Quality_Created = []
sonar = SonarQubeClient(sonarqube_url="http://localhost:9001", username='admin', password='admin123')
def Open_File_Config ():
    with open('quality-gates.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

def Get_Quality_Gates_Already():
    List_Quality_Gates_Already = sonar.qualitygates.get_quality_gates()
    for Quality_Gates_Already in List_Quality_Gates_Already['qualitygates']:
        Name_Gates_Already = Quality_Gates_Already['name']
        ID_Gates_Already = Quality_Gates_Already['id']
        Dict_Quality_Gates_Already[Name_Gates_Already] = ID_Gates_Already
    return (Dict_Quality_Gates_Already)

def Create_Quality_Gates():
    data = Open_File_Config()
    separator = ' '
    for Quality_Gates in data['list-quality-gates']:
        Name_Quality_Gates = separator.join(Quality_Gates.keys())
        if Name_Quality_Gates not in Get_Quality_Gates_Already():
            Result = sonar.qualitygates.create_quality_gate(name=Name_Quality_Gates)
    
def Delete_Quality_Gates():
    data = Open_File_Config()
    separator = ' '
    List_Quality_Gates = data['list-quality-gates']
    for Quality_Gates_Created in data['list-quality-gates']:
        Name_Quality_Gates_Created = separator.join(Quality_Gates_Created.keys())
        List_Quality_Created.append(Name_Quality_Gates_Created)
    for Quality_Gates in Get_Quality_Gates_Already():
        if Quality_Gates not in List_Quality_Created:
            Result = sonar.qualitygates.delete_quality_gate(Dict_Quality_Gates_Already[Quality_Gates])
            print (Result)
if __name__ == "__main__":
    print (Create_Quality_Gates())
    print (Delete_Quality_Gates())
