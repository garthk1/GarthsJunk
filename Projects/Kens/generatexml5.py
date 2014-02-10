import sys
import os
import os.path
import time

line2_ver = sys.argv[1]
str(line2_ver)
is_zipfile = line2_ver.endswith("zip")

#slight error checking.
if is_zipfile is False:
    print("This is not a zip file! Dude! What's wrong with you!")
    exit()
else:
    print "\n\n"

    file_size = os.path.getsize(line2_ver)

# Time to cut the file name up
line2_no_zip = line2_ver.rsplit(".", 1)[0]
line2_dic_v = line2_no_zip.split('v')
line2_versions = line2_dic_v[1]
line2_revision_cut = line2_versions.split('_')
line2_revision_number = line2_revision_cut[1]
line2_version_cut = line2_revision_cut[0]

# Get the create time of the file
created_time = time.strftime("%a, %d %b %Y %I:%M:%S %z", time.gmtime(os.path.getmtime(line2_ver)))

# Printing everything!
print "<item>"
print "\t<title>Version{0}</title>".format(line2_version_cut)
print "\t<sparkle:releaseNotesLink>http://li228-23.members.linode.com/releaseNotes/{0}.html\
</sparkle:releaseNotesLink>" .format(line2_versions)
print "\t<pubDate>{0}</pubDate>".format(created_time)
print "\t<enclosure url=\"http://li228-23.members.linode.com/app/{0}\"".format(line2_ver)
print "\t\tsparkle:shortVersionString=\"{0}\"".format(line2_version_cut)
print "\t\tsparkle:version=\"{0}\"".format(line2_revision_number)
print "\t\tsparkle:dsaSignature=\"\""
print "\t\tlength=\"{0}\"".format(str(file_size))
print "\t\ttype=\"application/octet-stream\"/>"
print "</item>"
print "\n\n" #added some new lines so its easier to cut and paste

# Release notes wraps funny. Not sure how make it go to a new line without breaking it.



