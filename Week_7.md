# Week 7.1

## Task Manger and CMD
We ended processes: Apple Push, iCloud Services, iPod Service, iTunesHelper, Skype, Apple Push, and TeamViewer
We disabled on startup everything except for Microsoft OneDrive and Windows Security notification icon

```console  
echo Bashlining Reporting > report.txt
type report.txt
echo Created by Matthew >> report.txt
echo %OS% system report created on %date% with logged in user %user% >> report.txt       
type report.txt                                                                
dir "\Program Files" >> report.txt
dir "\Program Files (x86)" >> report.txt
Type report.txt
```

## Users, Groups, and Password Policies
```console
net user
Net user Alex >> report.txt
Net localgroup >> report.txt
Net accounts >> report.txt
Type report.txt
```

## Creating Users and Setting Passwrod Policies
```console
Net user alex Ilovesales123! /add
Net user andrew Ilovedevelopment123! /add
Net localgroup administrators andrew /add
Net user andrew
Net accounts - after changing in gpedit
```
