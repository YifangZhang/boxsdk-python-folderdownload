from boxsdk import OAuth2, Client
from boxsdk import DevelopmentClient
import os

folder_id = "<folder_id>"

client = DevelopmentClient()
## still need to manually enter the developer token ##
me = client.user().get()

'''
download file & folder function
'''
def downloadFile(fp, client, file_path):
	print(f'working on file: {fp.name}')
	# Write the Box file contents to disk
	output_file = open(file_path+fp.name, 'wb')
	client.file(fp.id).download_to(output_file)
	output_file.close()


def downloadFolder(folder, client, file_path):
	## create a folder ##
	os.mkdir(file_path + folder.get().name)
	file_path_cur = file_path + folder.get().name + "/"
	for fp in folder.get_items():
		print(f'working on folder: {folder.get().name}')
		if(fp.type.capitalize() == "Folder"):
			downloadFolder(fp, client, file_path_cur)
		elif(fp.type.capitalize() == "File"):
			downloadFile(fp, client, file_path_cur)

folder = client.folder(folder_id)
downloadFolder(folder, client, "./")
