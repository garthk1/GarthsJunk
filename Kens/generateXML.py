# Author: DaJuggernaut
import string
import sys

# print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

kens_file = str(sys.argv)
print(kens_file)
name_of_file = kens_file.find("Li")
end_of_file = kens_file.find(".zip") +4
entire_file = kens_file[name_of_file:end_of_file]
short_version_text = entire_file[6:9]
revision_version_exist = entire_file.find("_")
revision_version_start = entire_file.find("_") +1
revision_version_end = entire_file.find(".zip")
revision_version = entire_file[revision_version_start:revision_version_end]

print("Revision: ") + revision_version
version = "Version " + short_version_text
file_name = "File name: " + entire_file
print(version)
print(file_name)

