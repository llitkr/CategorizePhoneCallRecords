import os
import shutil

recExts = ['.m4a']		## 가져올 확장자 목록(오디오 파일 확장자들)
TPhoneCallRecFolder = "/volume1/home/phoneCalls"
from os import listdir
from os.path import isfile, join
files = [f for f in listdir(TPhoneCallRecFolder) if isfile(join(TPhoneCallRecFolder, f))]

def createFolder(directory):
	try:
		os.makedirs(directory)
	except OSError:
		print (directory + '경로 생성 중 에러 발생 : ' + OSError)

orLen = len(files)

for i in (range(orLen)) :
	if os.path.splitext(files[orLen -1 - i])[1] not in recExts : 
		del files[orLen - 1 - i]

for i in range(len(files)) :
	for j in (range(recExts)) :
		orName = files[i].replace(recExts[j], '')
	fullFileName = files[i]
	fileName = files[i].split('_');
	dateTime = fileName[len(fileName)-1].replace(recExts[0], '')
	for j in (range(recExts)) :
		dateTime = dateTime.replace(recExts[j], '')
	if len(dateTime) == 14 :
		newName = dateTime[0:4] + '_' + dateTime[4:6] + '_' + dateTime[6:8] + '_' + dateTime[8:10] + '_' + dateTime[10:12] + '_' + dateTime[12:14] + '_'
	else :
		print('뭔가 에러가 발생했습니다. 파일 스킵 후 텔레그램으로 알림 발송.');
		continue;

	if(len(fileName)-2 > 0) :
		newName += '('
		for j in range(len(fileName)-2) :
			newName += fileName[j] + '_'
		newName = newName.rstrip('_')
		newName += ')'

	newName += fileName[len(fileName)-2]

	newName += '(' + orName + ')' + os.path.splitext(files[i])[1]
	
	folderDir = TPhoneCallRecFolder + '/' + 'T전화-' + dateTime[0:4] + '_' + dateTime[4:6] + '월'

	if(os.path.isdir(folderDir)) :
		print("폴더가 존재하여 '" + fullFileName + "' 파일의 이름을 [" + newName + "]으로 변경 후 [" + folderDir.replace(TPhoneCallRecFolder, '') + "]폴더로 이동")
		shutil.move(TPhoneCallRecFolder + '/' + fullFileName, folderDir + '/' + newName)
	else :
		print("필요한 없음. 폴더 생성 시도.")
		createFolder(folderDir)
		shutil.move(TPhoneCallRecFolder + '/' + fullFileName, folderDir + '/' + newName)
		print("폴더를 성공적으로 생성하고 '" + fullFileName + "' 파일의 이름을 [" + newName + "]으로 변경 후 [" + folderDir.replace(TPhoneCallRecFolder, '') + "]폴더로 이동")
