import sys
import os
import os.path
import time

# Was playing with XML but had a hard time with the enclosure. I will figure it out at some point im sure.
# Will need these guys again for that.
# from xml.etree import ElementTree
# from xml.etree.ElementTree import Element, SubElement, tostring



# Gather the file name from the input so I can manupulate it.
# Once I figure out lists I am sure it will be easier.
kens_file = str(sys.argv)


program_name = sys.argv[0]
arguments = sys.argv[1]
count = len(arguments)
print(arguments)


# All this text manipulation. I am sure there is a much easier way to do it.
# This is just how I could make it work with my limited knowledge.
name_of_file = kens_file.find("Li")
end_of_file = kens_file.find(".zip") +4
end_of_file_noext = kens_file.find(".zip")
entire_file = kens_file[name_of_file:end_of_file]
short_version_text = entire_file[6:9]
revision_version_exist = entire_file.find("_")
revision_version_start = entire_file.find("_") +1
minor_version_end = entire_file.find("_") -1
revision_version_end = entire_file.find(".zip")
file_without_extension = kens_file[name_of_file:end_of_file_noext]
revision_version = entire_file[revision_version_start:revision_version_end]
minor_version_exists = entire_file[9]
'''
if minor_version_exists == ".":
    minor_version_start = entire_file[]
    str(minor_version_end)
    minor_version =  minor_version_start + str(minor_version_end)
    print(minor_version)
'''

#file_name = "File name: " + entire_file
# Get the file size of the input file..hopefully
file_size = os.path.getsize(entire_file)

# Get the create time of the file
created_time = time.strftime("%a, %d %b %Y %I:%M:%S %z",time.gmtime(os.path.getmtime(entire_file)))

# Printing everything!
print("<item>")
print("\t<title>Version{0}</title>" .format(short_version_text))
print("\t<sparkle:releaseNotesLink>http://li228-23.members.linode.com/releaseNotes/{0}_{1}.html</sparkle:releaseNotesLink>" .format(short_version_text,revision_version))
print("\t<pubDate>{0}</pubDate>" .format(created_time))
print("\t<enclosure url=\"http://li228-23.members.linode.com/app/{0}\"" .format(entire_file))
print("\t\tsparkle:shortVersionString=\"{0}\"" .format(short_version_text))
print("\t\tsparkle:version=\"{0}\"" .format(revision_version))
print("\t\tsparkle:dsaSignature=\"\"")
print("\t\tlength=\"{0}\"" .format(str(file_size)))
print("\t\ttype=\"application/octet-stream\"/>")
print("</item>")

# Release notes wraps funny. Not sure how make it go to a new line without breaking it.