Name:           pdftk
Version:        1.41
Release:        %mkrel 7
Summary:        PDF Tool Kit
License:        GPL
Group:          Publishing
URL:            http://www.pdfhacks.com/pdftk/
Source0:        http://www.pdfhacks.com/pdftk/%{name}-%{version}.tar.bz2
Patch0:         pdftk-1.41-rpmopt.patch
Patch1:         pdftk-1.41-system-libgcj.patch
Patch2:         pdftk-1.41-gcjh.patch
BuildRequires:  java-devel-gcj
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Pdftk is a simple tool for doing everyday things with PDF documents.
Keep one in the top drawer of your desktop and use it to:
- Merge PDF Documents
- Split PDF Pages into a New Document
- Decrypt Input as Necessary (Password Required)
- Encrypt Output as Desired
- Fill PDF Forms with FDF Data and/or Flatten Forms
- Apply a Background Watermark
- Report on PDF Metrics, including Metadata and Bookmarks
- Update PDF Metadata
- Attach Files to PDF Pages or the PDF Document
- Unpack PDF Attachments
- Burst a PDF Document into Single Pages
- Uncompress and Re-Compress Page Streams
- Repair Corrupted PDF (Where Possible)

%prep
%setup -q
%patch0 -p1 -b .rpmopt
%patch1 -p0 -b .system-libgcj
%patch2 -p0 -b .gcjh

%{__perl} -pi -e "s/\r$//g" pdftk.1.txt

%{__rm} -r java_libs/gnu_local java_libs/java_local java_libs/gnu

%build
pushd pdftk
%{__make} GCJ=gcj GCJFLAGS="%{optflags} -I`pwd`/../java_libs -Wno-deprecated -Wno-unused" GCJH=gcjh CXX=%{__cxx} VERSUFF=-$(rpm -q --queryformat "%{VERSION}" gcj-tools) -f Makefile.Mandrake
popd

%install
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -a pdftk/pdftk %{buildroot}%{_bindir}/pdftk

%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__cp} -a debian/pdftk.1 %{buildroot}%{_mandir}/man1/pdftk.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc pdftk.1.html pdftk.1.txt
%attr(0755,root,root) %{_bindir}/pdftk
%{_mandir}/man1/pdftk.1*
