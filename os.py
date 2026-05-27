import os

dir1 = input("디렉토리 1")
dir2 = input("디렉토리 2")

files1 = {}
files2 = {}

for entry in os.scandir(dir1):
    if entry.is_file():
        files1[entry.name] = entry.stat().st_size

for entry in os.scandir(dir2):
    if entry.is_file():
        files2[entry.name] = entry.stat().st_size

if len(files1) != len(files2):
    print("파일 수가 다름")

elif files1 != files2:
    print("파일 이름 또는 크기 다름")
    
else:
    same = True

    for name in files1:
        path1 = os.path.join(dir1, name)
        path2 = os.path.join(dir2, name)

        with open(path1, "rb") as f1, open(path2, "rb") as f2:
            if f1.read() != f2.read():
                same = False
                print(name, "내용 다름")
                break

    if same:
        print("파일 동일")