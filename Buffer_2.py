import arcpy

input_feature_class_path = r"D:\1_BVIEER\3rd_sem\Programming for GIS- III Mr. Ronit Jadhav\Practical_1\P1_Running_Python_Scripts\Practical_1_ProProject\01_Running_Python_Scripts.gdb\Wilson_Schools"

# Path to the output buffer feature class
output_buffer_path = r"D:\1_BVIEER\3rd_sem\Programming for GIS- III Mr. Ronit Jadhav\Practical_1\P1_Running_Python_Scripts\Practical_1_ProProject\output.gdb\buffer_500m"

# Buffer distance
distance = "500 Meters"

arcpy.analysis.Buffer(input_feature_class_path, output_buffer_path, distance)
print("Process completed")
