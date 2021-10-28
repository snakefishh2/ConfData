del ConfData.zip
"C:\Program Files\7-Zip\7z.exe" a -tzip -mcu ConfData.zip *\*.txt
git add .
git commit -m "%date% %time:~0,5%"
git push https://snakefishh2@github.com/snakefishh2/ConfData.git