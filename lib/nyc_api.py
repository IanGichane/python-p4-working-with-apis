
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content
  
  def program_school(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
    programs_list = []
    programs = json.loads(self.get_programs())
    if isinstance(programs, list) and all(isinstance(program, str) for program in programs):
            programs_list = programs
    else:
            # Assume it's a list of dictionaries and extract the "agency" field
      programs_list = [program.get("agency", "") for program in programs]

    return programs_list
# programs = GetPrograms().get_programs()
# print(programs)

programs = GetPrograms()
programs_schools = programs_instance.program_school()
for school in set(programs_schools):
    print(school)