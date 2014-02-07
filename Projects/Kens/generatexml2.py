import sys
from xml.etree.ElementTree import Element, SubElement, tostring
import os
import os.path
import time
from xml.etree import ElementTree


# print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
# from lxml import etree




kens_file = str(sys.argv)
print(kens_file)
name_of_file = kens_file.find("Li")
end_of_file = kens_file.find(".zip") +4
end_of_file_noext = kens_file.find(".zip")
entire_file = kens_file[name_of_file:end_of_file]
short_version_text = entire_file[6:9]
revision_version_exist = entire_file.find("_")
revision_version_start = entire_file.find("_") +1
revision_version_end = entire_file.find(".zip")
file_without_extension = kens_file[name_of_file:end_of_file_noext]
revision_version = entire_file[revision_version_start:revision_version_end]

file_size = os.path.getsize(entire_file)
print(file_size)
# testing different time formats

print "last modified: %s" % time.ctime(os.path.getmtime(entire_file))
print "created: %s" % time.ctime(os.path.getctime(entire_file))

# Need to tweak this one but it gives me proper GMT Time!
# The date is funky though, I kinda like it.
created_time = time.strftime("%m/%d/%Y %I:%M:%S %p",time.gmtime(os.path.getmtime(entire_file)))

#statinfo = os.stat(entire_file)
stat_info = os.stat(entire_file).st_ctime
print(stat_info)

# end time testing zone


print("Revision: ") + revision_version
version = "Version " + short_version_text
file_name = "File name: " + entire_file
print(version)
print(file_name)
print(file_without_extension)
print(entire_file)

# XML Testing down below
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

#root = ElementTree.parse('/tmp/xmlfile').getroot()


'''
root = Element('Item')
title = SubElement(root, "Title")
title.text = version
sparkle = SubElement(root,"sparkle:releaseNotesLink")
sparkle.text = "http://li228-23.members.linode.com/app/" + file_without_extension + ".html"
pub_date = SubElement(root,"pubDate")
pub_date.text = created_time
indent(root)
ElementTree.dump(root)
'''

enclosure_begining = "<enclosure url=\"http://li228-23.members.linode.com/app/" +  entire_file + "\""
sparkle_shortver = "sparkle:shortVersionString=\"" +  short_version_text + "\""
sparkle_revision = "sparkle:version=\"" + revision_version + "\""
sparkle_file_size = "sparkle:dsaSignature=\"\""
file_length = "length=" + str(file_size)
enclosure_end = "type=\"application/octet-stream\"/>"


print("<item>")

print(enclosure_begining)
print(sparkle_shortver)
print(sparkle_revision)
print(sparkle_file_size)
print(file_length)
print(enclosure_end)

print("</item>")
#xml = xml.dom.minidom.parse(root)
#pretty_xml_as_string = xml.toprettyxml()
# print tostring(root)

