# Import arcpy package
import arcpy

#Setting the default workspace
arcpy.env.workspace = r"D:\1_BVIEER\3rd_sem\Programming for GIS- III Mr. Ronit Jadhav\Practical_1\P1_Running_Python_Scripts\Practical_1_ProProject\01_Running_Python_Scripts.gdb"

arcpy.analysis.Buffer("Wilson_Schools","Wilson_School_Buffer_600m", "600 meters")
print("Process Cmpleted")