%define gcj_support 1

Name:		pdftk
Version:	2.02
Release:	1
Summary:	PDF Tool Kit
License:	GPLv2+
Group:		Publishing
URL:		http://www.pdfhacks.com/pdftk/
Source0:	http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/%{name}-%{version}-src.zip
Patch0:		pdftk-1.44-makefile-fix.patch
BuildRequires:	gcc-java
BuildRequires:	libgcj-devel
BuildRequires:	unzip
BuildRequires:	fastjar
BuildRequires:	dos2unix
Requires:	bouncycastle

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
%setup -q -n %{name}-%{version}-dist
%patch0 -p0 -b .makefix

perl -pi -e "s/\r$//g" pdftk.1.txt

dos2unix changelog.txt

%build
pushd pdftk
GCJFLAGS="%{optflags} -I`pwd`/../java -Wno-all" %{__make} -f Makefile.Redhat
popd

%install
mkdir -p %{buildroot}%{_bindir}
cp -a pdftk/pdftk %{buildroot}%{_bindir}/pdftk

mkdir -p %{buildroot}%{_mandir}/man1
cp -a pdftk.1 %{buildroot}%{_mandir}/man1/pdftk.1

%files
%doc pdftk.1.html pdftk.1.txt changelog.txt
%attr(0755,root,root) %{_bindir}/pdftk
%{_mandir}/man1/pdftk.1*
