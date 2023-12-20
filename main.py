import xml.etree.ElementTree as ET

# Load the original XML file
xml_file_path = "ta.tamil.xml"
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Create a new XML tree
new_tree = ET.ElementTree(ET.Element('quran'))
new_root = new_tree.getroot()

# Iterate through sura elements
for sura in root.findall('.//sura'):
    sura_number = sura.get('index')

    # Create a new sura element in the new XML structure
    new_sura = ET.SubElement(new_root, 'sura', number=sura_number)

    # Iterate through aya elements within each sura
    for aya in sura.findall('.//aya'):
        aya_number = aya.get('index')
        aya_index = aya.get('index')
        aya_text = aya.get('text')

        # Create a new aya element in the new XML structure
        new_aya = ET.SubElement(new_sura, 'aya', index=aya_index, aya_number=aya_index, text=aya_text, footnotes='')

# Save the new XML file
new_xml_file_path = "new_tamil.xml"
new_tree.write(new_xml_file_path, encoding='utf-8', xml_declaration=True)
