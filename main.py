import pandas as pd
import xml.etree.ElementTree as ET


def excel_to_xml(input_excel_file, output_xml_file):
    # Read Excel file into a DataFrame
    df = pd.read_excel(input_excel_file)

    # Create XML root element
    root = ET.Element("data")

    # Convert each row in the DataFrame to XML
    for _, row in df.iterrows():
        item_element = ET.SubElement(root, "item")
        for col_name, cell_value in row.items():
            col_element = ET.SubElement(item_element, col_name)
            col_element.text = str(cell_value)

    # Create an ElementTree object and write to the XML file
    tree = ET.ElementTree(root)
    tree.write(output_xml_file, xml_declaration=True, encoding="utf-8")


if __name__ == "__main__":
    excel_file_path = "path/to/your/excel/file.xlsx"
    xml_output_path = "path/to/your/output/file.xml"

    excel_to_xml(excel_file_path, xml_output_path)
