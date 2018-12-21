from xml.etree import ElementTree as ET
import os

# Alter XML File and Save Changes to the same file.
def alterXML(tagsToChange, valuesForTags, xml):
  # Dictionary to store all the tags (in case there are many)
  tags = {}
  # Verify the list of tags and values are the same length
  if (len(tagsToChange) != len(valuesForTags)):
    raise NameError('Number of tags does not match number of values')
  # Add values to the dictionary created above.
  for i in range(0, len(tagsToChange)):
    tags[tagsToChange[i]] = valuesForTags[i]
  # Use ElementTree to parse the xml file and create the tree for you.
  tree = ET.parse(xml)
  # Loop through the dictionary, and set each tag to its new value
  for tag in tags:
    tree.find(tag).text = tags[tag]
  # Write the text to the new XML
  tree.write(xml)
  print('Completed Altering ' + xml)


# Using the existing function 'alterXML' to alter all .xml files in a given folder.
def changeAllXMLFiles(folder, tags, values):
  for file in os.listdir(folder):
    if(file.endswith('.xml')):
      alterXML(tags, values, os.path.join(folder, file))


tags = ['state_cd', 'fac_id']
values = ['NV', 'NVS597S']

changeAllXMLFiles('/home/runner/xmls', tags, values)
