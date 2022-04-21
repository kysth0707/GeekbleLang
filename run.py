from pyautogui import confirm as Alert
import time
import os

print("GeekbleLang By 노잼#3372 Discord")

OriginalFile = None
FileData = None
VariableList = None

FileToAccess = ""


def SelectFile():
	global FileToAccess
	#print(os.getcwd())
	
	RawFiles = os.listdir(os.getcwd())
	ConvertedFiles = []
	cnt = 0
	for i in range(0, len(RawFiles)):
		try:
			if RawFiles[i][len(RawFiles[i])-8:len(RawFiles[i])] == ".geekble":
				ConvertedFiles.append(RawFiles[i])
				print("Num "+str(cnt)+" : "+RawFiles[i])
				cnt += 1
		except:
			pass
	
	while True:
		SuccessToChangeFile = False
		try:
			a = int(input("FILE NUMBER : "))
			print(a)
			if 0 <= a and a < len(ConvertedFiles):
				SuccessToChangeFile = True
				#print("Success")
				FileToAccess = RawFiles[a]
		except:
			pass

		if SuccessToChangeFile == True:
			break
	# for dirName,subDirList, fnames in os.walk('C:\\Windows\\debug'):
	# 	for fname in fnames:
	# 		print(os.path.join(dirName,fname))

def ReturnNumber(txt):
	global VariableList
	val = 0
	for i in range(0, len(txt)):
		if txt[i] == "찬":
			val += 1
		elif txt[i] == "후":
			val -= 1
		elif txt[i] == "차":
			val += 10
		elif txt[i] == "누":
			val -= 10
		elif txt[i] == "촤":
			val += 100
		elif txt[i] == "눙":
			val -= 100
		elif txt[i] == "멀":
			val += 72
		elif txt[i] == "티":
			val -= 72
		elif txt[i] == "탭":
			val += 72*72
		try:
			if txt[i:7] == "긱블질문&답변":
				val = int(input("INPUT : "))
				print("")
		except:
			pass
		try:
			if txt[i:i+2] == "만들":
				save = 0
				for ii in range(i + 2, len(txt)):
					if txt[ii] != "어":
						break
					else:
						save += 1
				save-=1
				#print(str(save)+" 번째 변수")
				val += VariableList[save]
				#print(VariableList[save], save)
		except:
			pass

	#print(val)
	return val










def ErrorInCode(ErrorNumber,Cause,HowToSolve):
	Alert("error (" + ErrorNumber + ")\n\nCause:" + Cause + "\n\nSolution:" + HowToSolve, "오류 발생!")
	raise

def ReadOriginalFile():
	#\n 을 전부 제거한 값을 가져옴
	global FileData, OriginalFile
	try:
		OriginalFile = open(FileToAccess,"r",encoding='utf-8')
		RawFileData = OriginalFile.readlines()

		FileData = []

		for i in range(0, len(RawFileData)):
			# if RawFileData[i] != "\n":
			FileData.append(RawFileData[i].strip("\n"))

		OriginalFile.close()
		#print(FileData)
	except:
		ErrorInCode("0-1", "파일을 찾을 수 없습니다!", "''code.geekble'' 파일을 생성하시거나 파일명을 ''code.geekble'' 로 수정해주세요")
			




def CompileIt():
	global VariableList
	if len(FileData) == 0:
		ErrorInCode("0-2", "코드가 없습니다!", "코드를 작성해주세요!")

	if FileData[0] != "긱" or FileData[len(FileData) - 1] != "블":
		ErrorInCode("0-3", "시작과 끝이 명시되지 않았습니다!", "시작은 ''긱'', 끝은 ''블'' 로 수정해주세요!")


	VariableList = []
	for i in range(0,100):
		VariableList.append(0)

	i = 0
	while True:
		txt = FileData[i]
		#print(txt)
		if len(txt) > 0:
			if txt[0] == "#":
				pass
			elif txt == "키트화공약":
				break
			elif txt == "어?왜안되지?":
				time.sleep(0.1)
				pass
			else:
				if len(txt) >= 3:
					if txt[0:3] == "만들자": # 변수를 만들게요
						if txt[3] != "아": # 첫 변수구나
							#print(txt[3:len(txt)])
							#print(0)
							VariableList[0] = ReturnNumber(txt[3:len(txt)])
							pass
						elif len(txt) == 3:
							VariableList[0] = 0
							pass



						else: # 2 번째 변수 ~ n 까지
							save = 0
							for ii in range(3, len(txt)):
								if txt[ii] == "아":
									save += 1
								else:
									break
							#print(txt[3+save:len(txt)])
							#print(save)
							try:
								VariableList[save] = ReturnNumber(txt[3+save:len(txt)])
							except:
								VariableList[save] = 0
				try:
					if txt[0:2] == "일단" and txt[len(txt) - 2:len(txt)] == "해봐":
						print(chr(  ReturnNumber(txt[2:len(txt) - 2])  ), end="")
						#print(ReturnNumber(txt[2:len(txt) - 2]))

					elif txt[0:3] == "가시죠":
						i = ReturnNumber(txt[3:len(txt)]) - 1
						#print("/"+str(i)+"/")
						pass

					elif txt[0:4] == "납땜꿀잼" and txt.find("?") != -1:
						QuestionLoc = txt.find("?")
						if ReturnNumber(txt[4:QuestionLoc]) == 0: #0이라면, 코드 이동
							i = ReturnNumber(txt[QuestionLoc + 1:len(txt)]) - 1
							pass

					elif txt[0:2] == "작품" and txt[len(txt) - 3:len(txt)] == "시사회":
						print(ReturnNumber(txt[2:len(txt) - 3]),end="")

					elif txt[0:4] == "항공모함":
						print(txt[4:len(txt)])
					
					elif txt[0:2] == "작품" and txt[len(txt) - 4:len(txt)] == "시사회_":
						print(ReturnNumber(txt[2:len(txt) - 4]))
					
					#납땜꿀잼[A]?[B]

				except:
					pass
		#print(i)
		if i >= len(FileData) - 1:
			break
		i+=1
	#print(VariableList)


SelectFile()

#print(ReturnNumber("멀후후후후후후후"))
print("")
RunTime = time.time()
ReadOriginalFile()
CompileIt()
print("")
print("\nRunTime : "+str(time.time()-RunTime)+" sec")
print("ctrl + c 를 눌러 종료")
try:
	while True:
		time.sleep(0.1)
except:
	pass
