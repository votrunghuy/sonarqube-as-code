from sonarqube import SonarQubeClient
List_Quality_Gates = ['qlg1', 'qlg2', 'qlg3', 'Sonar way', 'qlg4', 'qlg5', 'qlg6', 'qlg7']
sonar = SonarQubeClient(sonarqube_url="http://localhost:9001", username='admin', password='admin123')
Dict_Quality_Gates_Already = {}
def Get_Quality_Gates_Already():
    List_Quality_Gates_Already = sonar.qualitygates.get_quality_gates()
    for Quality_Gates_Already in List_Quality_Gates_Already['qualitygates']:
        Name_Gates_Already = Quality_Gates_Already['name']
        ID_Gates_Already = Quality_Gates_Already['id']
        Dict_Quality_Gates_Already[Name_Gates_Already] = ID_Gates_Already
    return (Dict_Quality_Gates_Already)
def Create_Quality_Gates():
    for Quality_Gates in List_Quality_Gates:
        if Quality_Gates not in Get_Quality_Gates_Already():
            Result = sonar.qualitygates.create_quality_gate(name=Quality_Gates)
            print (Result)
def Delete_Quality_Gates():
    for Quality_Gates in Get_Quality_Gates_Already():
#        print (Quality_Gates)
        if Quality_Gates not in List_Quality_Gates:
            Result = sonar.qualitygates.delete_quality_gate(Dict_Quality_Gates_Already[Quality_Gates])
            print (Result)
if __name__ == "__main__":
    print (Create_Quality_Gates())
    print (Delete_Quality_Gates())
    

#    for Quality_Gates in List_Quality_Gates:
#        if Quality_Gates in Quality_Gates_Already['name']:
#            print ("Quality Gates"+ Quality_Gates + "Exits")
#        else:
#            sonar.qualitygates.create_quality_gate(name=Quality_Gates)
#     Quality_Gates_Already['name']
#print (List_Quality_Gates_Already['qualitygates']['name'])
#for quality_gate in List_Quality_gates:
#    sonar.qualitygates.create_quality_gate(name=quality_gate)
#quality_gates = sonar.qualitygates.get_quality_gates()
#print (quality_gates['qualitygates'])

