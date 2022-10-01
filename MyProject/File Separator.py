import os, shutil as sh

print("\tThese app is made to move all important files present in given path & in all subdirectories  inside the path to respective folders also present in that path.\n\tIf not present  then will be created if any file(s) is found & then all the files will be moved\n\n\t For Whole Phone Memory enter : 'ALL' \n\tOr give any valid path to separate all important files inside the path & all its subdirectories.")

whole_memory='/storage/emulated/0'
input_path=input("\tPath : \n\t")
if input_path=='ALL' :
	p=whole_memory
elif os.path.exists(input_path) :
	p=input_path
else :
	print('\tInvalid Input or No Such Directory ! \n\t')
	print('Program is being finished . . . . . .')
	exit()
print('\n\tPlease wait . . . . . . . .\n')
all_items=os.walk(p)
for paths,folders,files in all_items :
	os.chdir(paths)
	for f in files :
		f1=f.split('.')
		f2=f1[1].lower()
		file=f1[0]+'.'+f2
		
		if file.endswith('py') or file.endswith('cpp') or file.endswith('zava') :
			if  not os.path.exists(f'{p}/Programming Files') :
				os.mkdir(f'{p}/Programming Files')
			if not os.path.exists(f'{p}/Programming Files/{file}') :
						sh.move(f'{file}',f'{p}/Programming Files')
						
		elif file.endswith('mp3') or file.endswith('m4a') or file.endswith('wav') or file.endswith('flac'):
			if not os.path.exists(f'{p}/Music Files') :
				os.mkdir(f'{p}/Music Files')
			if not os.path.exists(f'{p}/Music Files/{file}') :
						sh.move(f'{file}',f'{p}/Music Files')
	
		elif file.endswith('pdf') or file.endswith('txt') or file.endswith('doc') or file.endswith('docx'):
			if not os.path.exists(f'{p}/Document Files') :
				os.mkdir(f'{p}/Document Files')
			if not os.path.exists(f'{p}/Document Files/{file}') :
						sh.move(f'{file}',f'{p}/Document Files')
	
		elif file.endswith('xlsx') or file.endswith('xls') :
			if not os.path.exists(f'{p}/Spreadsheet Files') :
				os.mkdir(f'{p}/Spreadsheet Files')
			if not os.path.exists(f'{p}/Spreadsheet Files/{file}') :
						sh.move(f'{file}',f'{p}/Spreadsheet Files')
						
		elif file.endswith('ppt') or file.endswith('pptx') :
			if not os.path.exists(f'{p}/Presentation Files') :
				os.mkdir(f'{p}/Presentation Files')
			if not os.path.exists(f'{p}/Presentation Files/{file}') :
						sh.move(f'{file}',f'{p}/Presentation Files')
						
		elif file.endswith('mp4') or file.endswith('mkv') or file.endswith('3gp') or file.endswith('flv') or file.endswith('mpeg'):
			if not os.path.exists(f'{p}/Video Files') :
				os.mkdir(f'{p}/Video Files')
			if not os.path.exists(f'{p}/Video Files/{file}') :
						sh.move(f'{file}',f'{p}/Video Files')
						
		elif file.endswith('exe') or file.endswith('iso') or file.endswith('img') or file.endswith('msi'):
			if not os.path.exists(f'{p}/PC Setup Files') :
				os.mkdir(f'{p}/PC Setup Files')
			if not os.path.exists(f'{p}/PC Setup Files/{file}') :
						sh.move(f'{file}',f'{p}/PC Setup Files')
		
		elif file.endswith('zip') or file.endswith('rar') or file.endswith('7z') or file.endswith('gz'):
			if not os.path.exists(f'{p}/Compressed Files') :
				os.mkdir(f'{p}/Compressed Files')
			if not os.path.exists(f'{p}/Compressed Files/{file}') :
						sh.move(f'{file}',f'{p}/Compressed Files')
		
		elif file.endswith('.apk') :
				if  not os.path.exists(f'{p}/Android App Files') :
					os.mkdir(f'{p}/Android App Files')
				if not os.path.exists(f'{p}/Android App Files/{file}') :
						sh.move(f'{file}',f'{p}/Android App Files')
						
		elif file.endswith('png') or file.endswith('jpg') or file.endswith('jpeg') :
			if not os.path.exists(f'{p}/Image Files') :
				os.mkdir(f'{p}/Image Files')
			if not os.path.exists(f'{p}/Image Files/{file}') :
						sh.move(f'{file}',f'{p}/Image Files')

print(f"\n\tAll important files present in '{p}' path & in all its subdirectories were moved to respective folders also present in  '{p}'. ")