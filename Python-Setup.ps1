$version = "3.11.1"
$url = "https://www.python.org/ftp/python/$version/python-$version.exe"
$dest = "$env:TEMP\python-$version.exe"
Invoke-WebRequest -Uri $url -OutFile $dest
Start-Process -FilePath $dest -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait
python -m ensurepip --upgrade
pip install requests
Remove-Item -Path $dest -Force