import os
import xml.etree.ElementTree as ET

# Input and output folders
input_folder = "source_data/xml"
output_folder = "modified_version"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through all XML files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".xml"):
        # Construct the full path for the input file
        input_file_path = os.path.join(input_folder, filename)

        # Load the source_data XML file
        tree = ET.parse(input_file_path)
        root = tree.getroot()

        # Create a new XML tree
        new_tree = ET.ElementTree(ET.Element('quran'))
        new_root = new_tree.getroot()

        # Initialize the current index for the entire document
        current_index = 1

        # Iterate through sura elements
        for sura in root.findall('.//sura'):
            sura_number = sura.get('index')

            # Create a new sura element in the new XML structure
            new_sura = ET.SubElement(new_root, 'sura', number=sura_number)

            # Iterate through aya elements within each sura
            for aya in sura.findall('.//aya'):
                aya_number = aya.get('index')
                aya_text = aya.get('text')

                # Create a new aya element in the new XML structure
                new_aya = ET.SubElement(new_sura, 'aya', index=str(current_index), aya_number=aya_number, text=aya_text, footnotes='')

                # Increment the current index
                current_index += 1

        # Construct the full path for the output file
        output_file_path = os.path.join(output_folder, filename)

        # Save the new XML file
        new_tree.write(output_file_path, encoding='utf-8', xml_declaration=True)
