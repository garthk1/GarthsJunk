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
# kens_file = str(sys.argv)

line2_ver = sys.argv[1]
str(line2_ver)
is_zipfile = line2_ver.endswith("zip")

if is_zipfile is False:
    print("This is not a zip file! Dude! What's wrong with you!")
    exit()
else:
    print("Lets do this!")

line2_no_zip = line2_ver.rsplit(".", 1)[0]
print(line2_no_zip)
line2_dic_v = line2_no_zip.split('v')
line2_versions = line2_dic_v[1]
line2_revision_cut = line2_versions.split('_')
line2_revision_number = line2_revision_cut[1]
line2_version_cut = line2_revision_cut[0]
# line2_major_cut = line2_version_cut.rsplit('.', 1)
# line2_major = line2_major_cut[0]
# line2_minor = line2_major_cut[1]

#hmmm gotta get a . between those.
# print(line2_version_nozip)
#print(line2_version_only)
#print(line2_versions)
print(line2_versions)
# print(line2_dic_v)
# print(line2_revision_cut)
print(line2_revision_number)
print(line2_version_cut)
# print(line2_major_cut)
#print(line2_major)
#print(line2_minor)


file_size = os.path.getsize(entire_file)

# Get the create time of the file
created_time = time.strftime("%a, %d %b %Y %I:%M:%S %z", time.gmtime(os.path.getmtime(line2_ver)))

# Printing everything!
print("<item>")
print("\t<title>Version{0}</title>".format(line2_version_cut)
#print("\t<sparkle:releaseNotesLink>http://li228-23.members.linode.com/releaseNotes/{0}.html\
#  </sparkle:releaseNotesLink>" .format(line2_versions))
print("\t<pubDate>{0}</pubDate>".format(created_time))
print "\t<enclosure url=\"http://li228-23.members.linode.com/app/{0}\"".format(line2_no_zip)
print("\t\tsparkle:shortVersionString=\"{0}\"".format(line2_version_cut))
print("\t\tsparkle:version=\"{0}\"".format(line2_revision_number))
print("\t\tsparkle:dsaSignature=\"\"")
print("\t\tlength=\"{0}\"".format(str(file_size)))
print("\t\ttype=\"application/octet-stream\"/>")
print("</item>")

# Release notes wraps funny. Not sure how make it go to a new line without breaking it.



'''
filename = '/home/user/somefile.txt'
print( filename.rsplit( ".", 1 )[ 0 ] )
# '/home/user/somefile'
The rsplit tells Python to perform the string splits starting from the right of the string, and the 1 says to perform at most one split (so that e.g.
'foo.bar.baz' -> [ 'foo.bar', 'baz' ]).
Since rsplit will always return a non-empty array, we may safely index 0 into it to get the filename minus the extension.
'''