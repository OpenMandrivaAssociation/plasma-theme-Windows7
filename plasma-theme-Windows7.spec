Name: plasma-theme-Windows7
Summary: Plasma theme resembling Windows 7
Version: 0.9.4.8
Release: 1
#Url: https://store.kde.org/p/1305103
#Source0: https://dllb2.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE1Nzc3NjYxOTMiLCJ1IjpudWxsLCJsdCI6ImRvd25sb2FkIiwicyI6ImI0YzU4NjExYzcxMjQ2YTZhYjZlMTA4MzA2ZmVhZmI5ZjU0ODFlZWMwMTVkMWUwNTMyM2VhYmIxOTFkYzFmOTBhNzI0M2JjZmM0YWNhZDViMTEzNjk2YzA3OWE3OWU5MDE0Nzk2MjBkYjQxODVlZjVkMzMwYTFjMDM4YmVjYzVmIiwidCI6MTU3OTM4ODI3NSwic3RmcCI6ImMwMzNkZTY2MjM5M2E3NWZjNWM2MmY1MDliZjE3OTY1Iiwic3RpcCI6IjQ2LjkyLjE4MC41MCJ9.emr8U0-52nLB-ZH2dYB_rEDvSWbUjYxncXMtKMcz1ZM/Diamond7_16.tar.gz
Url: https://www.pling.com/p/1002615
Source0: https://dllb2.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE1MjE3NDkyMTIiLCJ1IjpudWxsLCJsdCI6ImRvd25sb2FkIiwicyI6IjhlYzQ5OGJiOGM4Yjk2NTk4ZmM1N2Q1YTJkM2Y0ZDY0OGJjZDkwYjU0NGJlYWRlZGYwM2JlNTRmMjJmYmVlN2MyMmE3MmM1Y2MzZGUzZGJkZDBhNGVjZjAxNDQxODdmMGM0NTY3NTNhZmQxYzY3YWE0OWQzYWRhYTgzYTI0YjZhIiwidCI6MTU3OTM4OTUwNSwic3RmcCI6ImMwMzNkZTY2MjM5M2E3NWZjNWM2MmY1MDliZjE3OTY1Iiwic3RpcCI6IjQ2LjkyLjE4MC41MCJ9.Vth_4amNDd1ZbVHtrZxddLOHcB6IbPZ7a4H5A2CQpXo/Seven-Black.tar.gz
# https://www.pling.com/p/1002615
Source1: https://dllb2.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE0NjA3NDA3MjQiLCJ1IjpudWxsLCJsdCI6ImRvd25sb2FkIiwicyI6ImE1YWJmMDY4YzQ4N2NkMzQ4Y2IyYmJjNjQ0Zjc0YjZhZDIyODA3ODE3Nzk5NGI1MjAxZDk3NWYwMmIxYjMxZDNlNGRmOTI5NmUwYTc3YmI5ZDliOWY5ZGQwZTFiOTUxODM5NWQzYjAyZmM4YWUxYjY5MmM2OTRlMjk5ZjEzNzEzIiwidCI6MTU3OTM4OTA2Miwic3RmcCI6ImMwMzNkZTY2MjM5M2E3NWZjNWM2MmY1MDliZjE3OTY1Iiwic3RpcCI6IjQ2LjkyLjE4MC41MCJ9.9nE4RdTEf69zBnNd4G-xA-7juw2xTNuE859GkXrG1ZY/174336-seven-black.tar.gz
Group: Graphical Desktop/KDE
License: GPLv3
BuildArch: noarch
BuildRequires: distro-theme-OpenMandriva
# For the (not quite fitting, but similar enough) icons
Requires: plasma-theme-Windows10

%description
Plasma theme resembling Windows 7

%prep
# Nothing to do...

%build
# Nothing to do...

%install
mkdir -p %{buildroot}%{_datadir}/plasma/desktoptheme %{buildroot}%{_datadir}/aurorae/themes
cd %{buildroot}%{_datadir}/plasma/desktoptheme
tar xf "%{S:0}"
cd %{buildroot}%{_datadir}/aurorae/themes
tar xf "%{S:1}"

%files
%{_datadir}/plasma/desktoptheme/Seven-Black
%{_datadir}/aurorae/themes/seven-black
